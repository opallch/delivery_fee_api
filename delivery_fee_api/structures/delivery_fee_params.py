from pydantic import BaseModel, field_validator, ConfigDict, Field
from datetime import datetime
from dateutil import tz
from typing import List

class DeliveryFeeParameters(BaseModel):
    """Data class for storing parameters 
    needed for calculating the delievery fee."""
    model_config = ConfigDict(frozen=True)

    small_cart_value: float = Field(alias="small_cart_value_euro")
    large_cart_value: float = Field(alias="large_cart_value_euro")
    max_delivery_fee: float = Field(alias="max_delivery_fee_euro")
    
    init_distance_meter: int
    init_distance_fee: float = Field(alias="init_distance_fee_euro")
    distance_interval_meter: int 
    distance_fee_per_interval: float = Field(alias="distance_fee_per_interval_euro")

    surcharge_free_n_items: int 
    surcharge_per_item: float = Field(alias="surcharge_per_item_euro")
    extra_surcharge_n_items: int
    many_items_surcharge: float = Field(alias="many_items_surcharge_euro")

    rush_multiplier: float
    rush_days: List[str]
    rush_hours_begin: str 
    rush_hours_end: str
    time_zone: str

    @field_validator(
            'small_cart_value',
            'large_cart_value',
            'max_delivery_fee',
            'init_distance_fee',
            'distance_fee_per_interval',
            'surcharge_per_item',
            'many_items_surcharge',
            mode='before'
            )
    @classmethod
    def _parse_euro_to_cent(cls, value_euro, values):
        return value_euro * 100

    @field_validator('time_zone')
    @classmethod
    def validate_timezone(cls, timezone):
        if tz.gettz(timezone) is None:
            raise ValueError(f"time_zone defined in the config file '{timezone}' cannot be found, make sure it is on the list at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")

    @field_validator(
        'rush_hours_begin',
        'rush_hours_end',
        mode='before'
        )
    @classmethod
    def validate_time(cls, time):
        datetime_obj = datetime.strptime(time, "%H:%M")
        if datetime_obj.strftime("%H:%M") != time:
            raise ValueError(f"Time given '{time}' does not match the format 'HOUR:MINUTE'")
        return time
    
    @field_validator('rush_days', mode='after')
    @classmethod
    def validate_days_of_week(cls, days):
        formatted_days = []
        for day in days:
            datetime_obj = datetime.strptime(day, "%A")
            formatted_days.append(datetime_obj.strftime("%A"))
        return formatted_days
