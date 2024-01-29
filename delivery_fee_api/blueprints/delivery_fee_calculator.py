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


@delivery_fee_calculator.route('/', methods=['POST'], strict_slashes=False)
def calculate_cost():
    json_payload = request.json
    try:
        payload = DeliveryFeeRequestPayload.model_validate(json_payload)
    except ValidationError as e: 
        raise BadRequest from e

    delivery_fee = total_delivery_fee(params=DELIVERY_FEE_PARAMETERS, payload=payload)
    return DeliveryFeeResponsePayload(delivery_fee=delivery_fee).model_dump_json()
