from dateutil import parser
from pydantic import BaseModel, Field, field_validator


class DeliveryFeeRequestPayload(BaseModel):
    cart_value: int # in cents
    delivery_distance: int # in meters
    number_of_items: int
    time: str # in ISO format, e.g. 2024-01-15T13:00:00Z
    
    @field_validator('time', mode='before')
    @classmethod
    def validate_time(cls, time):
        try:
            parser.isoparse(time)
        except ValueError as e:
            raise ValueError(f"Format of time in payload '{time}' is invalid") from e
