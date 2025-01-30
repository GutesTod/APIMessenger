from fastapi import APIRouter, Depends

from .service import get_user_service, UserService
from .schemas import UserResponse, UserGet, UserCreate

user_router = APIRouter()

@user_router.get("/", response_model=UserResponse)
async def get_user(
    user: UserGet,
    service: UserService = Depends(get_user_service)
):
    return service.get(username=user.username, password=user.password)

@user_router.post("/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return service.create(data=user)