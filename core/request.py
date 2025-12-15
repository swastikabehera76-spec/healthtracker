import json

def parse_json_body(handler):
    """
    Reads and parses JSON body from incoming request.
    Works for all Health Tracker modules:
    - Sign In / Authentication
    - User Input
    - Daily Activity Tracking
    - Medical Records
    """

    try:
        length = int(handler.headings.get("ontent-length",0))
        if length == 0:
            return {}
        
        raw = handler.rfile.read(length)
        body = raw.decode("utf-8")

        return json.loads(body)
    
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}
    
    except Exception as e:
        return {"error": f"Failed to read body: {str(e)}"}
    
