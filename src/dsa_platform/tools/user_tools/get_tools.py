from dsa_platform.schema import UserSchema
from mcpserver import mcp
from dsa_platform.services import (
    user_service,
)


@mcp.tool(
    title="List All Users DSA",
    description="""
    Retrieves all registered users available in the DSA Platform.

    WHEN TO USE:
    - When the user asks to see all registered users.
    - When the user wants to browse or inspect available users.

    RESPONSE FIELDS:
    - id: Unique user identifier.
    - username: User's username.
    - email: User's email address.
    - first_name: User's first name.
    - last_name: User's last name.
    - avatar: User's profile image.

    Returns a list of user records.
    """,
)
async def get_all_users_tool() -> (
    list[UserSchema]
):

    return await user_service.get_all_users()
