from datetime import datetime

from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters
from delivery_fee_api.delivery_fee_calculator import total_delivery_fee, \
    delivery_surcharge_small_cart_value, \
    delivery_fee_distance, \
    delivery_fee_n_items, \
    ordered_in_rush, \
    _time_in_time_span
from delivery_fee_api.constants import DELIVERY_FEE_PARAMETERS as PARAMS


with open('test/test_delivery_params/multiple_rush_hours.json', 'r') as f_in:
    PARAMS_MULTI_RUSH_HOURS = DeliveryFeeParameters.model_validate_json(
        f_in.read())

with open('test/test_delivery_params/no_rush_hours.json', 'r') as f_in:
    PARAMS_NO_RUSH_HOURS = DeliveryFeeParameters.model_validate_json(
        f_in.read())

PAYLOAD = DeliveryFeeRequestPayload.model_validate(
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    }
)

PAYLOAD_RUSH_FOR_PARAMS = DeliveryFeeRequestPayload.model_validate(
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-19T18:59:00Z"
    }
)

PAYLOAD_RUSH_FOR_PARAMS_MULTI_RUSH_HOURS = DeliveryFeeRequestPayload.model_validate(
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-06T22:00:07Z"
    }
)

PAYLOAD_LARGE_CART_VAL = DeliveryFeeRequestPayload.model_validate(
    {
        "cart_value": 201 * 100,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-19T18:59:00Z"
    }
)


def test_total_delivery_fee_1():
    assert total_delivery_fee(PARAMS, PAYLOAD) == 710


def test_total_delivery_fee_2():
    assert total_delivery_fee(PARAMS, PAYLOAD_LARGE_CART_VAL) == 0


def test_total_delivery_fee_3():
    assert total_delivery_fee(PARAMS, PAYLOAD_RUSH_FOR_PARAMS) == 852


def test_delivery_surcharge_small_cart_value():
    assert delivery_surcharge_small_cart_value(PARAMS, 890) == 110


def test_delivery_fee_distance_1():
    assert delivery_fee_distance(PARAMS, distance=1499) == 3 * 100


def test_delivery_fee_distance_2():
    assert delivery_fee_distance(PARAMS, distance=1500) == 3 * 100


def test_delivery_fee_distance_3():
    assert delivery_fee_distance(PARAMS, distance=1501) == 4 * 100


def test_delivery_fee_n_items_1():
    assert delivery_fee_n_items(PARAMS, n_items=4) == 0


def test_delivery_fee_n_items_2():
    assert delivery_fee_n_items(PARAMS, n_items=5) == 0.5 * 100


def test_delivery_fee_n_items_3():
    assert delivery_fee_n_items(PARAMS, n_items=10) == 3 * 100


def test_delivery_fee_n_items_4():
    assert delivery_fee_n_items(PARAMS, n_items=13) == 5.7 * 100


def test_delivery_fee_n_items_5():
    assert delivery_fee_n_items(PARAMS, n_items=14) == 6.2 * 100


def test_ordered_in_rush_true_1():
    assert ordered_in_rush(PARAMS, PAYLOAD_RUSH_FOR_PARAMS.time) == True


def test_ordered_in_rush_true_2():
    assert ordered_in_rush(
        PARAMS_MULTI_RUSH_HOURS,
        PAYLOAD_RUSH_FOR_PARAMS_MULTI_RUSH_HOURS.time) == True


def test_ordered_in_rush_false_1():
    assert ordered_in_rush(PARAMS, PAYLOAD.time) == False


def test_ordered_in_rush_false_2():
    assert ordered_in_rush(PARAMS_MULTI_RUSH_HOURS, PAYLOAD.time) == False


def test_ordered_in_rush_false_3():
    assert ordered_in_rush(PARAMS_NO_RUSH_HOURS, PAYLOAD.time) == False


def test_ordered_in_rush_false_4():
    assert ordered_in_rush(
        PARAMS_NO_RUSH_HOURS,
        PAYLOAD_RUSH_FOR_PARAMS_MULTI_RUSH_HOURS.time) == False


def test_time_in_time_span_true1_1():
    time = datetime.strptime("12:42", "%H:%M")
    span_start = datetime.strptime("00:00", "%H:%M")
    span_end = datetime.strptime("23:00", "%H:%M")

    assert _time_in_time_span(time, span_start, span_end) == True


def test_time_in_time_span_true_2():
    time = datetime.strptime("12:42", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("12:59", "%H:%M")

    assert _time_in_time_span(time, span_start, span_end) == True


def test_time_in_time_span_true_3():
    time = datetime.strptime("12:42", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("15:00", "%H:%M")

    assert _time_in_time_span(time, span_start, span_end) == True


def test_time_in_time_span_true_4():
    time = datetime.strptime("14:37", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("14:59", "%H:%M")

    assert _time_in_time_span(time, span_start, span_end) == True


def test_time_in_time_span_false():
    time = datetime.strptime("20:24", "%H:%M")
    span_start = datetime.strptime("12:00", "%H:%M")
    span_end = datetime.strptime("17:00", "%H:%M")

    assert _time_in_time_span(time, span_start, span_end) == False
