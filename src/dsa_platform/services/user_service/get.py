from config import BASE_URLS
import httpx
from dsa_platform.schema import UserSchema
from mcp.server.mcpserver.exceptions import (
    ToolError,
)

USER_API = (
    f"{BASE_URLS['DSA_PLATFORM']}/users/"
)


async def get_all_users() -> (
    list[UserSchema]
):
    try:
        async with (
            httpx.AsyncClient() as client
        ):
            response = await client.get(
                USER_API
            )

            response.raise_for_status()

            return response.json()

    except httpx.HTTPStatusError as exc:
        raise ToolError(
            f"User API Error: {exc.response.status_code} "
            f"- {exc.response.text}"
        ) from exc

    except httpx.RequestError as exc:
        raise ToolError(
            f"User API Connection Error: {exc}"
        )
