from jose import jwt
from jose.exceptions import JWTError
import os
from typing import Dict, Any

class JWTValidator:
    def __init__(self):
        self.issuer = os.getenv("KEYCLOAK_ISSUER")
        self.audience = os.getenv("KEYCLOAK_AUDIENCE")
        self.public_key = os.getenv("KEYCLOAK_PUBLIC_KEY")
        self.algorithms = ["RS256"]

    def verify(self, token: str) -> Dict[str, Any]:
        try:
            payload = jwt.decode(
                token,
                self.public_key,
                algorithms=self.algorithms,
                audience=self.audience,
                issuer=self.issuer
            )
            return payload
        except JWTError as e:
            raise Exception(f"Invalid token: {str(e)}")