from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload
from delivery_fee_api.delivery_fee_calculator import DelieveryFeeCalculator

# TODO make many test cases
PAYLOAD = DeliveryFeeRequestPayload.model_validate(
    {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2024-01-15T13:00:00Z"
    }
)


def test_delivery_fee():
    calculator = DelieveryFeeCalculator("delivery_fee_api/config/delivery_fee_parameters.json")
    assert calculator.total_delivery_fee(PAYLOAD) == 790 
