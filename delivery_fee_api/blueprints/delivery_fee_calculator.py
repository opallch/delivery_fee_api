from logging import getLogger
from pydantic import ValidationError
from flask import Blueprint, request
from werkzeug.exceptions import BadRequest

from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload, DeliveryFeeResponsePayload
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters
from delivery_fee_api.delivery_fee_calculator import total_delivery_fee
from delivery_fee_api.constants import DELIVERY_FEE_PARAMETERS

delivery_fee_calculator = Blueprint('delivery_fee_calculator', 
                                    __name__, 
                                    url_prefix='/delivery-fee-calculator')

_REQUEST_LOGGER = getLogger(__name__ + ".request")
_RESPONSE_LOGGER = getLogger(__name__ + ".response")

@delivery_fee_calculator.route('/', methods=['POST'], strict_slashes=False)
def calculate_cost():
    json_payload = request.json
    _REQUEST_LOGGER.info(msg="", extra={'method':'POST', 'payload':json_payload})
    
    try:
        payload = DeliveryFeeRequestPayload.model_validate(json_payload)
    except ValidationError as e: 
        raise BadRequest from e

    delivery_fee = total_delivery_fee(params=DELIVERY_FEE_PARAMETERS, payload=payload)
    response_payload = DeliveryFeeResponsePayload(delivery_fee=delivery_fee).model_dump_json()
    _RESPONSE_LOGGER.info(msg="", extra={'payload':response_payload})
    return response_payload
