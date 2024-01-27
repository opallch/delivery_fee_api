from pydantic import ValidationError
from flask import Blueprint, request
from werkzeug.exceptions import BadRequest

from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters
from delivery_fee_api.structures.response import DeliveryFeeResponse
from delivery_fee_api.delivery_fee_calculator import total_delivery_fee

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

    path_to_params = "delivery_fee_api/config/delivery_fee_parameters.json"
    with open(path_to_params, 'r') as f_in:
        params = DeliveryFeeParameters.model_validate_json(f_in.read())

    delivery_fee = total_delivery_fee(params=params, payload=payload)
    return DeliveryFeeResponse(delivery_fee=delivery_fee).model_dump_json()
