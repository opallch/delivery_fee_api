from dateutil import parser
from pydantic import BaseModel, Field

from wolt_delivery_fee_calculator.constants import *


class DeliveryFeeRequest(BaseModel):
    cart_value: int # in cents
    delivery_distance: int # in meters
    number_of_items: int
    time: str # in ISO format, e.g. 2024-01-15T13:00:00Z

    def total_delivery_fee(self) -> float:
        total_in_cents = 0.0
        if self.cart_value >= LARGE_CART_VAL:
            return total_in_cents
        if self.cart_value < SMALL_CART_VAL:
            total_in_cents += (SMALL_CART_VAL - self.cart_value) * 100
        total_in_cents += self._delivery_fee_distance()
        if self._ordered_in_rush():
            total_in_cents *= RUSH_MULTIPLIER
        return min(total_in_cents, MAX_DELIEVERY_FEE)

    def _delivery_fee_distance(self) -> float:
        subtotal_in_euro = INIT_DISTANCE_FEE_EURO
        if self.delivery_distance - INIT_DISTANCE > 0:
            delivery_distance = self.delivery_distance - INIT_DISTANCE
            while delivery_distance > 0:
                subtotal_in_euro += 1
                delivery_distance -= REGULAR_DISTANCE
        return subtotal_in_euro * 100
    
    def _delivery_fee_n_items(self) -> float:
        subtotal_in_euro = 0.0
        if self.number_of_items > SURCHARGE_FREE_N_ITEMS:
            subtotal_in_euro += (self.number_of_items - SURCHARGE_FREE_N_ITEMS) * SURCHARGE_PER_ITEM_EURO
        if self.number_of_items > EXTRA_SURCHARGE_N_ITEMS:
            subtotal_in_euro += MANY_ITEMS_SURCHARGE_EURO
        return subtotal_in_euro * 100

    #TODO cleaner comparison
    def _ordered_in_rush(self) -> bool:
        time = parser.isoparse(self.time)
        return time.weekday() in RUSH_DAYS and \
            (time.hour >= RUSH_HOURS_BEGIN and time.hour <= RUSH_HOURS_END)