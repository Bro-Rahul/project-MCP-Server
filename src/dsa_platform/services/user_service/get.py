from config import BASE_URLS
import httpx
from dsa_platform.schema.UserSchema import (
    UserSchema,
)

USER_API = (
    f"{BASE_URLS['DSA_PLATFORM']}/users/"
)


async def get_all_users() -> (
    list[UserSchema]
):
    async with httpx.AsyncClient() as client:
        response = await client.get(USER_API)
        return response.json()
