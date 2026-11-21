import httpx
from typing import Dict, Any
from mcp.server.mcpserver.exceptions import (
    ToolError,
)
from config import BASE_URLS
from pydantic import ValidationError
from dsa_platform.schema import (
    RegisterSchema,
)
from dsa_platform.schema.auth_schema.auth_schema import (
    LoginResponseSchema,
    LoginSchema,
)

AUTH_URL = (
    f"{BASE_URLS['DSA_PLATFORM']}/users/auth"
)


async def register_user(
    payload: Dict[str, Any],
    is_staff: bool = False,
):
    try:
        register_data = RegisterSchema(
            **payload
        )

        async with httpx.AsyncClient(
            timeout=10.0
        ) as client:

            url = f"{AUTH_URL}/registe/"
            if is_staff:
                url = f"{url}staff/"

            response = await client.post(
                url,
                json=register_data.model_dump(),
            )

            response.raise_for_status()

            return {"info": "success"}

    except ValidationError as ve:
        raise ToolError(
            f"Validations Err {ve}"
        )

    except httpx.TimeoutException:
        raise ToolError(
            "Authentication service timed out"
        )

    except httpx.ConnectError:
        raise ToolError(
            "Unable to connect to authentication service"
        )

    except httpx.HTTPStatusError as exc:
        raise ToolError(
            f"Registration failed: {exc.response.status_code} "
            f"- {exc.response.text}"
        )


async def login_user(
    payload: dict,
) -> LoginResponseSchema:

    try:

        login_payload = LoginSchema(
            **payload
        )

        async with httpx.AsyncClient(
            timeout=10.0,
        ) as client:
            response = await client.post(
                url=f"{AUTH_URL}/login",
                json=login_payload.model_dump(),
            )
            response.raise_for_status()
            data = LoginResponseSchema(
                **response.json()
            )
            return data
    except ValidationError as ve:
        raise ToolError(
            f"Validations Err {ve}"
        )

    except httpx.TimeoutException:
        raise ToolError(
            "Authentication service timed out"
        )

    except httpx.ConnectError:
        raise ToolError(
            "Unable to connect to authentication service"
        )

    except httpx.HTTPStatusError as exc:
        raise ToolError(
            f"Registration failed: {exc.response.status_code} "
            f"- {exc.response.text}"
        )
