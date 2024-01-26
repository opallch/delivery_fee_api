from dateutil import parser
from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters


def total_delivery_fee(params:DeliveryFeeParameters, payload:DeliveryFeeRequestPayload) -> float:
    total_in_cents = 0.0
    if payload.cart_value >= params.large_cart_value:
        return total_in_cents
    
    if payload.cart_value < params.small_cart_value:
        total_in_cents += (params.small_cart_value - payload.cart_value)
    
    total_in_cents += delivery_fee_distance(params, payload.delivery_distance)
    total_in_cents += delivery_fee_n_items(params, payload.number_of_items)
    
    if ordered_in_rush(params, payload.time):
        total_in_cents *= params.rush_multiplier

    return min(total_in_cents, params.max_delivery_fee) 

def delivery_fee_distance(params:DeliveryFeeParameters, distance:int) -> float:
        subtotal_in_cent = params.init_distance_fee
        if distance - params.init_distance_meter > 0:
            delivery_distance = distance - params.init_distance_meter
            while delivery_distance > 0:
                subtotal_in_cent += params.distance_fee_per_interval
                delivery_distance -= params.distance_interval_meter
        return subtotal_in_cent

def delivery_fee_n_items(params:DeliveryFeeParameters, n_items:int) -> float:
        subtotal_in_euro = 0.0
        if n_items > params.surcharge_free_n_items:
            subtotal_in_euro += (n_items - params.surcharge_free_n_items) * params.surcharge_per_item
        if n_items > params.extra_surcharge_n_items:
            subtotal_in_euro += params.many_items_surcharge
        return subtotal_in_euro * 100

#TODO 
def ordered_in_rush(params:DeliveryFeeParameters, order_time:str) -> bool:
    return False
    parsed_time = parser.isoparse(order_time)
    # TODO compare
    return time.weekday() in params.rush_days and \
        (time.hour >= params.rush_hours_begin and time.hour <= params.rush_hours_end)