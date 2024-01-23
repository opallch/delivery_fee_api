from dateutil import parser
import delivery_fee_api.constants as c
from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload

# TODO one class handle delivery calculation
class DelieveryFeeCalculator:

    # TODO rewrite logic, beware of the unit
    @classmethod
    def total_delivery_fee(cls, payload:DeliveryFeeRequestPayload) -> float:
        total_in_cents = 0.0
        if payload.cart_value >= c.LARGE_CART_VAL * 100:
            return total_in_cents
        if payload.cart_value < c.SMALL_CART_VAL * 100:
            total_in_cents += (c.SMALL_CART_VAL - payload.cart_value) * 100
        total_in_cents += cls._delivery_fee_distance(payload)
        total_in_cents += cls._delivery_fee_n_items(payload)
        if cls._ordered_in_rush(payload):
            total_in_cents *= c.RUSH_MULTIPLIER
        return min(total_in_cents, c.MAX_DELIEVERY_FEE * 100)

    @classmethod
    def _delivery_fee_distance(cls, payload:DeliveryFeeRequestPayload) -> float:
        subtotal_in_euro = c.INIT_DISTANCE_FEE_EURO
        if payload.delivery_distance - c.INIT_DISTANCE > 0:
            delivery_distance = payload.delivery_distance - c.INIT_DISTANCE
            while delivery_distance > 0:
                subtotal_in_euro += 1
                delivery_distance -= c.REGULAR_DISTANCE
        return subtotal_in_euro * 100
    
    @classmethod
    def _delivery_fee_n_items(cls, payload:DeliveryFeeRequestPayload) -> float:
        subtotal_in_euro = 0.0
        if payload.number_of_items > c.SURCHARGE_FREE_N_ITEMS:
            subtotal_in_euro += (payload.number_of_items - c.SURCHARGE_FREE_N_ITEMS) * c.SURCHARGE_PER_ITEM_EURO
        if payload.number_of_items > c.EXTRA_SURCHARGE_N_ITEMS:
            subtotal_in_euro += c.MANY_ITEMS_SURCHARGE_EURO
        return subtotal_in_euro * 100

    #TODO cleaner comparison
    @classmethod
    def _ordered_in_rush(cls, payload:DeliveryFeeRequestPayload) -> bool:
        time = parser.isoparse(payload.time)
        return time.weekday() in c.RUSH_DAYS and \
            (time.hour >= c.RUSH_HOURS_BEGIN and time.hour <= c.RUSH_HOURS_END)