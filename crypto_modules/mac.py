# Message Authentication Code (MAC)
# Using HMAC-SHA256

import hmac
import hashlib
import base64
import os

def generate_mac(message: str, key: bytes) -> str:
    """Generate HMAC-SHA256 for the message."""
    mac = hmac.new(key, message.encode('utf-8'), hashlib.sha256)
    return mac.hexdigest()

def verify_mac(message: str, key: bytes, mac: str) -> bool:
    """Verify HMAC-SHA256 for the message."""
    expected_mac = generate_mac(message, key)
    return hmac.compare_digest(expected_mac, mac)

def process_text(text: str) -> str:
    """
    Process text using MAC (Message Authentication Code) for Flask app.
    Generates HMAC-SHA256 for the text.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        # Generate a random 32-byte key
        key = os.urandom(32)
        
        # Generate MAC
        mac = generate_mac(text, key)
        
        # Encode key in base64 for display
        key_b64 = base64.b64encode(key).decode('utf-8')
        
        result = f"MAC (HMAC-SHA256): {mac}\n\nKey (base64): {key_b64}\n\nMessage: {text}"
        return result
        
    except Exception as e:
        return f"ERROR: MAC generation failed: {str(e)}"

