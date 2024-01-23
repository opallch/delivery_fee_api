from flask import Blueprint, request
from wolt_delivery_fee_calculator.structures.payload import DeliveryFeeRequest

delivery_fee_calculator = Blueprint('delivery_fee_calculator', 
                                    __name__, 
                                    url_prefix='/delivery_fee_calculator')


@delivery_fee_calculator.route('/', methods=['POST'], strict_slashes=False)
def calculate_cost():
    json_payload = request.json
    payload = DeliveryFeeRequest.model_validate(json_payload)
    # TODO add class for response
    # response code, with needed message
    return {
        "delivery_fee": payload.total_delivery_fee(),
        "cart_value": payload.cart_value
        } 
