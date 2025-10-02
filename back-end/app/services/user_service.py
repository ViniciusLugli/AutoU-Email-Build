import asyncio
from fastapi import HTTPException
from app.core.security import hash_password, verify_password
from app.crud import create_user, get_user_by_email
from app.models import User
from app.schemas import TokenResponse, UserCreateRequest, UserLoginRequest, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.auth_service import create_access_token


async def register_user(session: AsyncSession, data: UserCreateRequest) -> User | None:
  
  userExist = await get_user_by_email(session, data.email)
  if userExist:
    raise HTTPException(status_code=400, detail="Email already registered")
  
  hash_pw = await asyncio.to_thread(hash_password, data.password)

  db_user = User(
    username=data.username.strip(),
    email=data.email,
    hash_password=hash_pw,
  )
  user = await create_user(session, db_user)
  return UserResponse(
    id=user.id,
    username=user.username,
    email=user.email,
    texts=[],
  )


async def authenticate_user(session: AsyncSession, data: UserLoginRequest) -> TokenResponse | None:
  user = await get_user_by_email(session, data.email)
  if not user:
    return None

  verified = verify_password(data.password, user.hash_password)
  if not verified:
    return None

  token = create_access_token({"sub": str(user.id), "email": user.email})
  return TokenResponse(access_token=token, user_id=user.id)