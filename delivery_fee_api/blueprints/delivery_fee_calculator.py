from flask import Blueprint, request
from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload
from delivery_fee_api.structures.response import DeliveryFeeResponse
from delivery_fee_api.delivery_fee_calculator import DelieveryFeeCalculator

delivery_fee_calculator = Blueprint('delivery_fee_calculator', 
                                    __name__, 
                                    url_prefix='/delivery-fee-calculator')


@delivery_fee_calculator.route('/', methods=['POST'], strict_slashes=False)
def calculate_cost():
    json_payload = request.json
    payload = DeliveryFeeRequestPayload.model_validate(json_payload)
    delivery_fee = DelieveryFeeCalculator.total_delivery_fee(payload)
    # TODO better way to initialize response
    response = DeliveryFeeResponse.model_validate({'delivery_fee': int(delivery_fee)})
    return response.model_dump_json()
