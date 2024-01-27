from pydantic import ValidationError
from flask import Blueprint
from werkzeug.exceptions import HTTPException, BadRequest
from delivery_fee_api.structures.error import ErrorResponse

error_handler = Blueprint('error', __name__)

# TODO extend it to more exception?
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
    response.data = ErrorResponse(
        code=e.code,
        name=e.name,
        description=description,
        ).model_dump_json()
    response.content_type = "application/json"
    return response