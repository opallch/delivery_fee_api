from pydantic import ValidationError
import pytest
from delivery_fee_api.structures.delivery_fee_params import TimeSlot

def test_parsing():
    example = {
        "day_of_week": "Friday",
        "begin_time": "15:00",
        "end_time": "19:00"
    }
    
    timeslot = TimeSlot.model_validate(example)
    
    assert timeslot.day_of_week == "Friday"
    assert timeslot.begin_time == "15:00"
    assert timeslot.end_time == "19:00"
    
    assert isinstance(timeslot.day_of_week, str)
    assert isinstance(timeslot.begin_time, str)
    assert isinstance(timeslot.begin_time, str)

def test_missing_day_of_week():
    example = {
        "begin_time": "15:00",
        "end_time": "19:00"
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_missing_begin_time():
    example = {
        "day_of_week": "Friday",
        "end_time": "19:00"
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_missing_end_time():
    example = {
        "day_of_week": "Friday",
        "begin_time": "15:00",
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_invalid_value_day_of_week():
    example = {
        "day_of_week": "Fri",
        "begin_time": "15:00",
        "end_time": "19:00"
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_invalid_value_begin_time():
    example = {
        "day_of_week": "Friday",
        "begin_time": "1500",
        "end_time": "19:00"
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_invalid_value_end_time():
    example = {
        "day_of_week": "Friday",
        "begin_time": "15:00",
        "end_time": "2500"
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_invalid_type_day_of_week():
    example = {
        "day_of_week": 5,
        "begin_time": "15:00",
        "end_time": "19:00"
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_invalid_type_begin_time():
    example = {
        "day_of_week": "Friday",
        "begin_time": 1500,
        "end_time": "19:00"
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)

def test_invalid_type_end_time():
    example = {
        "day_of_week": "Friday",
        "begin_time": "15:00",
        "end_time": 2500
    }
    with pytest.raises(ValidationError):
        TimeSlot.model_validate(example)
 