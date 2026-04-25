"""
Core module for VLESS config generation
"""
import uuid
import base64
import random
import string
from typing import Dict, Optional


class VLESSConfigGenerator:
    """Generate VLESS configuration strings"""
    
    def __init__(self):
        self.alpn_list = ["h2", "http/1.1", "h2,http/1.1"]
        self.fp_list = ["chrome", "firefox", "safari", "ios", "android"]
        
    def generate_uuid(self) -> str:
        """Generate a random UUID"""
        return str(uuid.uuid4())
    
    def generate_remark(self, username: str) -> str:
        """Generate a remark for the config"""
        timestamp = uuid.uuid4().hex[:8]
        return f"{username}-{timestamp}"
    
    def generate_config(
        self,
        address: str,
        port: int,
        path: str,
        sni: str,
        username: str,
        uuid_value: Optional[str] = None
    ) -> str:
        """
        Generate a complete VLESS config URL
        
        Args:
            address: Server address (domain or IP)
            port: Server port
            path: WebSocket path
            sni: Server Name Indication
            username: User identifier for remark
            uuid_value: Optional UUID (generates new one if not provided)
            
        Returns:
            VLESS config URL string
        """
        if uuid_value is None:
            uuid_value = self.generate_uuid()
        
        remark = self.generate_remark(username)
        remark_encoded = base64.b64encode(remark.encode()).decode()
        
        # Build VLESS URL
        config = (
            f"vless://{uuid_value}@{address}:{port}?"
            f"type=ws&path={path}&security=tls&sni={sni}"
            f"&alpn={random.choice(self.alpn_list)}"
            f"&fp={random.choice(self.fp_list)}"
            f"#{remark_encoded}"
        )
        
        return config
    
    def parse_config(self, config_url: str) -> Dict:
        """
        Parse a VLESS config URL into components
        
        Args:
            config_url: VLESS configuration URL
            
        Returns:
            Dictionary with config components
        """
        if not config_url.startswith("vless://"):
            raise ValueError("Invalid VLESS URL")
        
        # Remove vless:// prefix
        url_part = config_url[8:]
        
        # Split by #
        if "#" in url_part:
            main_part, remark_encoded = url_part.split("#", 1)
            remark = base64.b64decode(remark_encoded).decode()
        else:
            main_part = url_part
            remark = ""
        
        # Split by @
        if "@" in main_part:
            uuid_part, rest = main_part.split("@", 1)
        else:
            raise ValueError("Invalid VLESS URL format")
        
        # Parse query parameters
        if "?" in rest:
            address_port, query = rest.split("?", 1)
            params = dict(param.split("=") for param in query.split("&"))
        else:
            address_port = rest
            params = {}
        
        # Split address and port
        if ":" in address_port:
            address, port = address_port.rsplit(":", 1)
            port = int(port)
        else:
            raise ValueError("Invalid address:port format")
        
        return {
            "uuid": uuid_part,
            "address": address,
            "port": port,
            "type": params.get("type", "ws"),
            "path": params.get("path", "/"),
            "security": params.get("security", "tls"),
            "sni": params.get("sni", address),
            "alpn": params.get("alpn", ""),
            "fp": params.get("fp", ""),
            "remark": remark
        }
