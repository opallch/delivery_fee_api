from datetime import datetime
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
        subtotal_in_cent = 0.0
        if n_items > params.surcharge_free_n_items:
            subtotal_in_cent += (n_items - params.surcharge_free_n_items) * params.surcharge_per_item
        if n_items > params.extra_surcharge_n_items:
            subtotal_in_cent += params.many_items_surcharge
        return subtotal_in_cent

def time_in_time_span(time:datetime, time_span_start: datetime, time_span_end: datetime):
    if time.hour == time_span_start.hour and time.hour == time_span_end.hour:
        return time.minute >= time_span_start.minute and time.minute <= time_span_end.minute
    return (time.hour >= time_span_start.hour and time.hour < time_span_end.hour) or \
        (time.hour > time_span_start.hour and time.hour <= time_span_end.hour) 

def ordered_in_rush(params:DeliveryFeeParameters, order_time:str) -> bool:
    parsed_order_time = parser.isoparse(order_time)
    rush_hours_begin = datetime.strptime(params.rush_hours_begin, "%H:%M")
    rush_hours_end = datetime.strptime(params.rush_hours_end, "%H:%M")
    
    return time_in_time_span(parsed_order_time, rush_hours_begin, rush_hours_end)
