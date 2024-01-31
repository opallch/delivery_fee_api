import pytest
from pydantic import ValidationError

from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload, DeliveryFeeResponsePayload

def test_request_payload_parsing():
    payload_json = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-06T22:00:07Z"
    }
    payload = DeliveryFeeRequestPayload.model_validate(payload_json)
    assert payload.cart_value == 790
    assert payload.delivery_distance == 2235
    assert payload.number_of_items == 4
    assert payload.time == "2024-01-06T22:00:07Z"

    assert isinstance(payload.cart_value, int)
    assert isinstance(payload.delivery_distance, int)
    assert isinstance(payload.number_of_items, int)
    assert isinstance(payload.time, str)


def test_request_missing_cart_value():
    payload_json = {
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-06T22:00:07Z"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_request_missing_delivery_distance():
    payload_json = {
        "cart_value": 790,
        "number_of_items": 4,
        "time": "2024-01-06T22:00:07Z"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_request_missing_number_of_items():
    payload_json = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "time": "2024-01-06T22:00:07Z"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_request_missing_time():
    payload_json = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_request_invalid_cart_value():
    payload_json = {
        "cart_value": -790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-06T22:00:07Z"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_request_invalid_delivery_distance():
    payload_json = {
        "cart_value": 790,
        "delivery_distance": -2235,
        "number_of_items": 4,
        "time": "2024-01-06T22:00:07Z"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_request_invalid_number_of_items():
    payload_json = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": -4,
        "time": "2024-01-06T22:00:07Z"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_request_invalid_time():
    payload_json = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-06T55:00:07Z"
    }
    with pytest.raises(ValidationError):
        DeliveryFeeRequestPayload.model_validate(payload_json)


def test_response_payload_parsing():
    payload_json = {"delivery_fee": 710}
    payload = DeliveryFeeResponsePayload.model_validate(payload_json)
    
    assert payload.delivery_fee == 710
    assert isinstance(payload.delivery_fee, int)


def test_response_missing_delivery_fee():
    payload_json = {}

    with pytest.raises(ValidationError):
        DeliveryFeeResponsePayload.model_validate(payload_json)

def test_response_invalid_delivery_fee():
    payload_json = {"delivery_fee": -710}
    
    with pytest.raises(ValidationError):
        DeliveryFeeResponsePayload.model_validate(payload_json)
