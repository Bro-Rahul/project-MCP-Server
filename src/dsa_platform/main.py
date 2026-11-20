from dsa_platform.schema.UserSchema import (
    UserSchema,
)
from mcpserver import mcp
from dsa_platform.services.user_service.get import (
    get_all_users,
)


@mcp.tool()
async def calculate_from_dsa() -> (
    list[UserSchema]
):
    return await get_all_users()
