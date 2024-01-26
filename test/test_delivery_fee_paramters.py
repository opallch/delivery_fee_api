import json
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters

PATH_TO_PARAMS_JSON = "delivery_fee_api/config/delivery_fee_parameters.json"

def test_parse_euro_to_cent():
    with open(PATH_TO_PARAMS_JSON, 'r') as f_in:
        params = json.load(f_in)
        validated_params = DeliveryFeeParameters.model_validate_json(json.dumps(params))
    with open(PATH_TO_PARAMS_JSON, 'r') as f_in:
        validated_params = DeliveryFeeParameters.model_validate_json(f_in.read())
    
    assert validated_params.small_cart_value == params["small_cart_value_euro"] * 100
    assert validated_params.large_cart_value == params["large_cart_value_euro"] * 100
    assert validated_params.max_delivery_fee == params["max_delivery_fee_euro"] * 100
    assert validated_params.init_distance_fee == params["init_distance_fee_euro"] * 100
    assert validated_params.distance_fee_per_interval == params["distance_fee_per_interval_euro"] * 100
    assert validated_params.surcharge_per_item == params["surcharge_per_item_euro"] * 100
    assert validated_params.many_items_surcharge == params["many_items_surcharge_euro"] * 100


