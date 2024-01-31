import os
import json
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters
from delivery_fee_api.constants import DELIVERY_FEE_PARAMETERS

def test_parse_euro_to_cent():
    with open(os.getenv("PATH_TO_DELIVERY_PARAMS"), 'r') as f_in:
        non_validated_params = json.load(f_in)
    
    validated_params = DELIVERY_FEE_PARAMETERS

    assert validated_params.small_cart_value == non_validated_params["small_cart_value_euro"] * 100
    assert validated_params.large_cart_value == non_validated_params["large_cart_value_euro"] * 100
    assert validated_params.max_delivery_fee == non_validated_params["max_delivery_fee_euro"] * 100
    assert validated_params.init_distance_fee == non_validated_params["init_distance_fee_euro"] * 100
    assert validated_params.distance_fee_per_interval == non_validated_params["distance_fee_per_interval_euro"] * 100
    assert validated_params.surcharge_per_item == non_validated_params["surcharge_per_item_euro"] * 100
    assert validated_params.many_items_surcharge == non_validated_params["many_items_surcharge_euro"] * 100

def test_if_float_price_params_in_json_converted_to_int():
    """In the json file, price parameters can be stored as floating numbers,
    but they should be converted to int for further calculation. 
    """
    path_to_params_json = 'test/test_delivery_params/price_params_as_float.json'
    with open(path_to_params_json, 'r') as f_in:
        non_validated_params = json.load(f_in)
    with open(path_to_params_json, 'r') as f_in:
        validated_params = DeliveryFeeParameters.model_validate_json(f_in.read())

    assert isinstance(validated_params.small_cart_value, int)
    assert isinstance(validated_params.large_cart_value, int)
    assert isinstance(validated_params.max_delivery_fee, int)
    assert isinstance(validated_params.init_distance_fee, int)
    assert isinstance(validated_params.distance_fee_per_interval, int)
    assert isinstance(validated_params.surcharge_per_item, int)
    assert isinstance(validated_params.many_items_surcharge, int)

    assert validated_params.small_cart_value == non_validated_params["small_cart_value_euro"] * 100
    assert validated_params.large_cart_value == non_validated_params["large_cart_value_euro"] * 100
    assert validated_params.max_delivery_fee == non_validated_params["max_delivery_fee_euro"] * 100
    assert validated_params.init_distance_fee == non_validated_params["init_distance_fee_euro"] * 100
    assert validated_params.distance_fee_per_interval == non_validated_params["distance_fee_per_interval_euro"] * 100
    assert validated_params.surcharge_per_item == non_validated_params["surcharge_per_item_euro"] * 100
    assert validated_params.many_items_surcharge == non_validated_params["many_items_surcharge_euro"] * 100
