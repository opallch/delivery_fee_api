from dateutil import parser
from pydantic import BaseModel, PositiveInt, field_validator


class DeliveryFeeRequestPayload(BaseModel):
    cart_value: PositiveInt # in cents
    delivery_distance: PositiveInt # in meters
    number_of_items: PositiveInt
    time: str # in ISO format, e.g. 2024-01-15T13:00:00Z
    
    @field_validator('time', mode='before')
    @classmethod
    def validate_time(cls, time):
        try:
            parser.isoparse(time)
        except ValueError as e:
            raise ValueError(f"Format of time in payload '{time}' is invalid, make sure it is in ISO format (see https://en.wikipedia.org/wiki/ISO_8601)") from e
        return time

class DeliveryFeeResponsePayload(BaseModel):
    delivery_fee: PositiveInt
