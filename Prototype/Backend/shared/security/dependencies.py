from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from shared.security.jwt import JWTValidator

security = HTTPBearer()
jwt_validator = JWTValidator()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt_validator.verify(token)
        return payload
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )

def require_roles(required_roles: list[str]):
    def role_checker(user=Depends(get_current_user)):
        roles = user.get("realm_access", {}).get("roles", [])
        if not any(role in roles for role in required_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden"
            )
        return user
    return role_checker