from pydantic import BaseModel, field_validator, ConfigDict, Field
from typing import List

class DeliveryFeeParameters(BaseModel):
    """Dataclass for storing parameters 
    needed for calculating the delievery fee."""
    model_config = ConfigDict(frozen=True)

    # TODO change data type (float instead of int?)
    small_cart_value: int = Field(alias="small_cart_value_euro")
    large_cart_value: int = Field(alias="large_cart_value_euro")
    max_delivery_fee: int = Field(alias="max_delivery_fee_euro")
    rush_multiplier: float
    init_distance_meter: int
    init_distance_fee: int = Field(alias="init_distance_fee_euro")
    distance_interval_meter: int 
    surcharge_free_n_items: int 
    surcharge_per_item: float = Field(alias="surcharge_per_item_euro")
    many_items_surcharge: float = Field(alias="many_items_surcharge_euro")
    extra_surcharge_n_items: int
    rush_days: List[int] # or list of string?
    rush_hours_begin: int # TODO maybe other structure?
    rush_hours_end: int # TODO maybe other structure? 

    @field_validator(
            'small_cart_value',
            'large_cart_value',
            'max_delivery_fee',
            'surcharge_per_item',
            'many_items_surcharge'
            )
    @classmethod
    def _parse_euro_to_cent(cls, value_euro, values):
        return value_euro * 100

