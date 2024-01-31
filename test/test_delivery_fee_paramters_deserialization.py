from pydantic import ValidationError
import pytest
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters, TimeSlot
from delivery_fee_api.constants import DELIVERY_FEE_PARAMETERS

def test_parsing_params_in_config():
    assert DELIVERY_FEE_PARAMETERS.small_cart_value == 1000
    assert DELIVERY_FEE_PARAMETERS.large_cart_value == 20000
    assert DELIVERY_FEE_PARAMETERS.max_delivery_fee == 1500
    assert DELIVERY_FEE_PARAMETERS.init_distance_meter == 1000
    assert DELIVERY_FEE_PARAMETERS.init_distance_fee == 200
    assert DELIVERY_FEE_PARAMETERS.distance_interval_meter == 500
    assert DELIVERY_FEE_PARAMETERS.distance_fee_per_interval == 100
    assert DELIVERY_FEE_PARAMETERS.surcharge_free_n_items == 4
    assert DELIVERY_FEE_PARAMETERS.surcharge_per_item == 50
    assert DELIVERY_FEE_PARAMETERS.extra_surcharge_n_items == 12
    assert DELIVERY_FEE_PARAMETERS.many_items_surcharge == 120
    assert DELIVERY_FEE_PARAMETERS.rush_multiplier == 1.2
    assert DELIVERY_FEE_PARAMETERS.time_zone == "Europe/Berlin"

    assert DELIVERY_FEE_PARAMETERS.rush_hours == [
        TimeSlot.model_validate({
            "day_of_week": "Friday",
            "begin_time": "15:00",
            "end_time": "19:00"
        })
    ]

    assert isinstance(DELIVERY_FEE_PARAMETERS.small_cart_value, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.large_cart_value, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.max_delivery_fee, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.init_distance_meter, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.init_distance_fee, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.distance_interval_meter, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.surcharge_free_n_items, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.surcharge_per_item, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.extra_surcharge_n_items, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.many_items_surcharge, int)
    assert isinstance(DELIVERY_FEE_PARAMETERS.rush_multiplier, float)
    assert isinstance(DELIVERY_FEE_PARAMETERS.time_zone, str)

    assert all([timeslot for timeslot in DELIVERY_FEE_PARAMETERS.rush_hours if isinstance(timeslot, TimeSlot)])

def test_missing_small_cart_value_cent():
    params = {
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
    "time_zone": "Europe/Berlin"
}

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_large_cart_value_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_max_delivery_fee_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_init_distance_meter():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_init_distance_fee_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_distance_interval_meter():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_distance_fee_per_interval_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_surcharge_free_n_items():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_surcharge_per_item_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_extra_surcharge_n_items():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_many_items_surcharge_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_rush_multiplier():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_rush_hours():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_missing_time_zone():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_empty_rush_hours():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [],
        "time_zone": "Europe/Berlin"
    }
    assert DeliveryFeeParameters.model_validate(params)

def test_empty_rush_hours_day_of_week():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [{
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }],
        "time_zone": "Europe/Berlin"
    }
    assert DeliveryFeeParameters.model_validate(params)
    
def test_invalid_value_small_cart_value_cent():
    params = {
        "small_cart_value_cent": -1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_large_cart_value_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": -20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_max_delivery_fee_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": -1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_init_distance_meter():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": -1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_init_distance_fee_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": -200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_distance_interval_meter():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": -500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_distance_fee_per_interval_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": -100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_surcharge_free_n_items():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": -4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_surcharge_per_item_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": -50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_extra_surcharge_n_items():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": -12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_many_items_surcharge_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": -120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_rush_hours():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {},
        ],
        "time_zone": "Europe/Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_value_time_zone():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Berlin"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

##### 

def test_invalid_type_small_cart_value_cent():
    params = {
        "small_cart_value_cent": "A", 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_large_cart_value_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": "A",
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_max_delivery_fee_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": "A",
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_init_distance_meter():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": "A",
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_init_distance_fee_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": "A",
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_distance_interval_meter():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": "A",
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_distance_fee_per_interval_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": "A",

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_surcharge_free_n_items():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": "A",
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_surcharge_per_item_cent():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": "A",
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_extra_surcharge_n_items():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": "A",
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_many_items_surcharge_cent():
    params = {
        "small_cart_value_cent": "A", 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": "A",
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_rush_multiplier():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": "A",
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_rush_hours():
    params = {
        "small_cart_value_cent": 1000, 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            "Hello", "wrong inputs"
        ],
        "time_zone": "Europe/Berlin"
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)

def test_invalid_type_time_zone():
    params = {
        "small_cart_value_cent": "A", 
        "large_cart_value_cent": 20000,
        "max_delivery_fee_cent": 1500,
        "init_distance_meter": 1000,
        "init_distance_fee_cent": 200,
        "distance_interval_meter": 500,
        "distance_fee_per_interval_cent": 100,

        "surcharge_free_n_items": 4,
        "surcharge_per_item_cent": 50,
        "extra_surcharge_n_items": 12,
        "many_items_surcharge_cent": 120,
        
        "rush_multiplier": 1.2,
        "rush_hours": [
            {
                "day_of_week": "Friday",
                "begin_time": "15:00",
                "end_time": "19:00"
            }
        ],
        "time_zone": 12345678
    }

    with pytest.raises(ValidationError):
        DeliveryFeeParameters.model_validate(params)


