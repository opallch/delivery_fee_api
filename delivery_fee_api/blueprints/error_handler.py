from logging import getLogger
from pydantic import ValidationError
from flask import Blueprint
from werkzeug.exceptions import HTTPException, BadRequest
from delivery_fee_api.structures.error import HTTPErrorResponse

error_handler = Blueprint('error', __name__)

_LOGGER = getLogger(__name__)


@error_handler.app_errorhandler(HTTPException)
def handle_error(e):
    """
    Return JSON instead of HTML for HTTP errors.
    https://flask.palletsprojects.com/en/2.3.x/errorhandling/#generic-exception-handlers
    """
    response = e.get_response()
    description = e.description

    if isinstance(e, BadRequest):
        if isinstance(e.__cause__, ValidationError):
            description = str(e.__cause__)
    # replace the body with ErrorResponse json
    response.data = HTTPErrorResponse(
        code=e.code,
        name=e.name,
        description=description,
        ).model_dump_json()
    response.content_type = "application/json"
    
    _LOGGER.error(
        msg="HTTP Error",
        extra={
            "code": str(e.code),
            "error_name": e.name,
            "description": description,
    })

    return response
