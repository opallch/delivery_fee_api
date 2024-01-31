from pydantic import BaseModel, field_validator, ConfigDict, Field, PositiveInt, PositiveFloat
from datetime import datetime
from dateutil import tz
from typing import List

class TimeSlot(BaseModel):
    day_of_week: str
    begin_time: str
    end_time:str 
    
    @field_validator(
        'begin_time',
        'end_time'
    )
    @classmethod
    def validate_time(cls, time):
        datetime_obj = datetime.strptime(time, "%H:%M")
        if datetime_obj.strftime("%H:%M") != time:
            raise ValueError(f"Time given '{time}' does not match the format 'HOUR:MINUTE'")
        return time
    
    @field_validator('day_of_week')
    @classmethod
    def validate_day_of_week(cls, day):
        try:
            datetime.strptime(day, "%A")
        except ValueError:
            raise ValueError(f"The given day of week {day} is invalid. Any spelling mistake?")
        return day

class DeliveryFeeParameters(BaseModel):
    """Data class for storing parameters 
    needed for calculating the delievery fee."""
    model_config = ConfigDict(frozen=True)

    small_cart_value: PositiveInt = Field(alias="small_cart_value_cent")
    large_cart_value: PositiveInt = Field(alias="large_cart_value_cent")
    max_delivery_fee: PositiveInt = Field(alias="max_delivery_fee_cent")
    
    init_distance_meter: PositiveInt
    init_distance_fee: PositiveInt = Field(alias="init_distance_fee_cent")
    distance_interval_meter: PositiveInt 
    distance_fee_per_interval: PositiveInt = Field(alias="distance_fee_per_interval_cent")

    surcharge_free_n_items: PositiveInt 
    surcharge_per_item: PositiveInt = Field(alias="surcharge_per_item_cent")
    extra_surcharge_n_items: PositiveInt
    many_items_surcharge: PositiveInt = Field(alias="many_items_surcharge_cent")

    rush_multiplier: PositiveFloat
    rush_hours: List[TimeSlot]
    time_zone: str

    @field_validator('rush_hours')
    @classmethod
    def validate_rush_hours(cls, rush_hours_list):
        validate_rush_hours = []
        for item in rush_hours_list:
            validate_rush_hours.append(
                TimeSlot.model_validate(item)
                )
        return validate_rush_hours
    
    @field_validator('time_zone')
    @classmethod
    def validate_timezone(cls, timezone):
        if tz.gettz(timezone) is None:
            raise ValueError(f"time_zone defined in the config file '{timezone}' cannot be found, make sure it is on the list at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
