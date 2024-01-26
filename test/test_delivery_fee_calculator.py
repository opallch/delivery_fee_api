from datetime import datetime

from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters
from delivery_fee_api.delivery_fee_calculator import total_delivery_fee, \
                                                        delivery_fee_distance, \
                                                        delivery_fee_n_items, \
                                                        ordered_in_rush, \
                                                        time_in_time_span \

# TODO make many test cases
PAYLOAD = DeliveryFeeRequestPayload.model_validate(
    {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2024-01-15T13:00:00Z"
    }
)

PAYLOAD_RUSH = DeliveryFeeRequestPayload.model_validate(
    {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2024-01-19T18:59:00Z"
    }
)

with open("delivery_fee_api/config/delivery_fee_parameters.json", 'r') as f_in:
    PARAMS = DeliveryFeeParameters.model_validate_json(f_in.read())


def test_total_delivery_fee():
    assert total_delivery_fee(PARAMS, PAYLOAD) == 790 


def test_delivery_fee_distance_1():
    assert delivery_fee_distance(PARAMS, distance=1499) == 3 * 100

def test_delivery_fee_distance_2():
    assert delivery_fee_distance(PARAMS, distance=1500) == 3 * 100

def test_delivery_fee_distance_3():
    assert delivery_fee_distance(PARAMS, distance=1501) == 4 * 100

def test_delivery_fee_n_items():
    pass


def test_ordered_in_rush_true():
    assert ordered_in_rush(PARAMS, PAYLOAD_RUSH.time) == True

def test_ordered_in_rush_false():
    assert ordered_in_rush(PARAMS, PAYLOAD.time) == False

def test_time_in_time_span_true1_1():
    time = datetime.strptime("12:42", "%H:%M")
    span_start = datetime.strptime("00:00", "%H:%M")
    span_end = datetime.strptime("23:00", "%H:%M")

    assert time_in_time_span(time, span_start, span_end) == True

def test_time_in_time_span_true_2():
    time = datetime.strptime("12:42", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("12:59", "%H:%M")

    assert time_in_time_span(time, span_start, span_end) == True

def test_time_in_time_span_true_3():
    time = datetime.strptime("12:42", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("15:00", "%H:%M")

    assert time_in_time_span(time, span_start, span_end) == True

def test_time_in_time_span_true_4():
    time = datetime.strptime("14:37", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("14:59", "%H:%M")

    assert time_in_time_span(time, span_start, span_end) == True

def test_time_in_time_span_false():
    time = datetime.strptime("20:24", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("17:00", "%H:%M")

    assert time_in_time_span(time, span_start, span_end) == False
