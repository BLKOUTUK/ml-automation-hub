"""
Comprosio API Client for connecting to MCP servers.
"""
import os
import requests
from typing import Dict, Any, Optional

class ComprosioClient:
    """Client for interacting with Comprosio API and MCP servers."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Comprosio client.
        
        Args:
            api_key: API key for Comprosio. If None, looks for COMPROSIO_API_KEY env var.
        """
        self.api_key = api_key or os.environ.get("COMPROSIO_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set as COMPROSIO_API_KEY env var")
            
        self.base_url = "https://api.comprosio.com/v1"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
    
    def connect(self) -> Dict[str, Any]:
        """Establish connection to MCP servers.
        
        Returns:
            Dict containing connection information and status
        """
        response = self.session.get(f"{self.base_url}/connect")
        response.raise_for_status()
        return response.json()
        
    # Add more methods as needed for your specific MCP server interactions