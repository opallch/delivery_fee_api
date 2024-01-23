from flask import Blueprint, request
from delivery_fee_api.structures.payload import DeliveryFeeRequest

delivery_fee_calculator = Blueprint('delivery_fee_calculator', 
                                    __name__, 
                                    url_prefix='/delivery-fee-calculator')


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
