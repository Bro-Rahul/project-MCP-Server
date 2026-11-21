from typing import Dict, Any
from dsa_platform.schema.auth_schema.auth_schema import (
    LoginResponseSchema,
    LoginSchema,
)
from dsa_platform.services.auth_service import (
    auth_service,
)
from mcpserver import mcp


@mcp.tool(
    name="register_dsa_user",
    title="Register DSA Platform User",
    description="""
    Creates a new NORMAL USER account specifically for the DSA Platform.

    APPLICATION SCOPE:
    - This tool is exclusively for the DSA Platform.
    - Do not use this tool to register users for any other application,
      project, or external service.

    WHEN TO USE:
    - When someone explicitly wants to create a DSA Platform account.
    - When someone wants to sign up as a regular student or platform user.

    REQUIRED PAYLOAD:
    {
        "username": "string - Unique username",
        "email": "string - Valid email address",
        "password": "string - Account password"
    }

    FIELD REQUIREMENTS:
    - All three fields are mandatory.
    - Username must be unique within the DSA Platform.
    - Email must be valid.
    - Password must satisfy the platform's password requirements.
    - Never invent missing registration details.
    - Ask the user for missing information.

    ACCOUNT TYPE:
    - Creates a regular DSA Platform user.
    - Do not assign staff or administrator privileges.

    RESTRICTIONS:
    - Do not use this tool for staff registration.
    - Do not use it for login requests.
    - Only invoke it when the user explicitly requests registration.
    - Never expose the password in the response.

    RETURNS:
    Registration status
    """,
)
async def register_user_tool(
    payload: Dict[str, Any],
) -> dict[str, str]:

    return await auth_service.register_user(
        payload=payload, is_staff=False
    )


@mcp.tool(
    name="register_dsa_staff",
    title="Register DSA Platform Staff",
    description="""
    Creates a new STAFF account specifically for the DSA Platform.

    APPLICATION SCOPE:
    - This tool is exclusively for DSA Platform staff registration.
    - Do not use it to register staff for other applications or projects.

    WHEN TO USE:
    - When an authorized administrator explicitly requests
      registration of a new DSA Platform staff member.
    - When a user specifically requests staff account creation.

    REQUIRED PAYLOAD:
    {
        "username": "string - Unique staff username",
        "email": "string - Valid staff email address",
        "password": "string - Account password"
    }

    FIELD REQUIREMENTS:
    - All three fields are mandatory.
    - Username must be unique within the DSA Platform.
    - Email must be valid.
    - Password must satisfy the platform's password requirements.
    - Never invent missing registration details.
    - Ask for missing required information.

    ACCOUNT TYPE:
    - Creates a DSA Platform staff account.
    - The account receives staff privileges through the backend.

    SECURITY RESTRICTIONS:
    - Never use this tool for normal student registration.
    - Do not grant staff privileges merely because someone asks for them.
    - Staff registration must be authorized by an existing administrator
      or an approved administrative workflow.
    - Never expose passwords in responses.

    RETURNS:
    Registration status

    """,
)
async def register_user_staff_tool(
    payload: Dict[str, Any],
) -> dict[str, str]:

    return await auth_service.register_user(
        payload=payload, is_staff=True
    )


@mcp.tool(
    name="login_dsa_user",
    title="Login DSA Platform User",
    description="""
    Authenticates an existing NORMAL USER account
    specifically within the DSA Platform.

    APPLICATION SCOPE:
    - This tool is exclusively for DSA Platform accounts.
    - Do not use it for other applications or projects.

    WHEN TO USE:
    - When a registered user explicitly wants to log in.
    - When a user wants to authenticate into their DSA Platform account.

    REQUIRED PAYLOAD:
    {
        "username": "string - Registered DSA Platform username",
        "password": "string - Account password"
    }

    FIELD REQUIREMENTS:
    - Both fields are mandatory.
    - Never invent or assume login credentials.
    - Never modify the user's supplied credentials.
    - Ask for missing credentials.

    ACCOUNT RESTRICTIONS:
    - This tool is exclusively for normal DSA Platform users.
    - Do not use it for staff authentication.
    - Do not use it for account registration.

    SECURITY:
    - Never expose passwords in responses.
    - Never claim successful authentication without backend confirmation.
    - Do not reveal whether an account exists when authentication fails.

    RETURNS:
    LoginResponseSchema
    """,
)
async def login_dsa_user(
    payload: dict,
) -> LoginResponseSchema:
    return await auth_service.login_user(
        payload=payload,
    )
