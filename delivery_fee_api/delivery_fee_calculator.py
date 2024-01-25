from dateutil import parser
import configparser
from delivery_fee_api.structures.payload import DeliveryFeeRequestPayload
from delivery_fee_api.structures.constants import DeliveryFeeParameters


class DelieveryFeeCalculator:
    
    def __init__(self, path_to_params_ini:str):
        # TODO load constants from delivery_fee_parameters.ini into a dict
        # validate the loaded dict with DeliveryFeeParameters
        # use it in the DelieveryFeeCalculator class
        config_parser = configparser.ConfigParser()
        with open(path_to_params_ini, 'r') as f_in:
            config_parser.read_file(f_in)
        output_dict= {s:dict(config_parser.items(s)) 
                      for s in config_parser.sections()}
        # print(output_dict)
        self.params = DeliveryFeeParameters.model_validate(output_dict["Parameters"])
    
    # TODO rewrite logic, beware of the unit
    def total_delivery_fee(self, payload:DeliveryFeeRequestPayload) -> float:
        total_in_cents = 0.0
        if payload.cart_value >= self.params.large_cart_value:
            return total_in_cents
        if payload.cart_value < self.params.small_cart_value:
            total_in_cents += (self.params.small_cart_value - payload.cart_value)
        total_in_cents += self._delivery_fee_distance(payload)
        total_in_cents += self._delivery_fee_n_items(payload)
        if self._ordered_in_rush(payload):
            total_in_cents *= self.params.rush_multiplier
        return min(total_in_cents, self.params.max_delivery_fee) / 100

    def _delivery_fee_distance(self, payload:DeliveryFeeRequestPayload) -> float:
        subtotal_in_cent = self.params.init_distance_fee
        if payload.delivery_distance - self.params.init_distance_meter > 0:
            delivery_distance = payload.delivery_distance - self.params.init_distance_meter
            while delivery_distance > 0:
                subtotal_in_cent += 1000
                delivery_distance -= self.params.distance_interval_meter
        return subtotal_in_cent
    
    def _delivery_fee_n_items(self, payload:DeliveryFeeRequestPayload) -> float:
        subtotal_in_euro = 0.0
        if payload.number_of_items > self.params.surcharge_free_n_items:
            subtotal_in_euro += (payload.number_of_items - self.params.surcharge_free_n_items) * self.params.surcharge_per_item
        if payload.number_of_items > self.params.extra_surcharge_n_items:
            subtotal_in_euro += self.params.many_items_surcharge
        return subtotal_in_euro * 100

    #TODO cleaner comparison
    def _ordered_in_rush(self, payload:DeliveryFeeRequestPayload) -> bool:
        time = parser.isoparse(payload.time)
        return time.weekday() in self.params.rush_days and \
            (time.hour >= self.params.rush_hours_begin and time.hour <= self.params.rush_hours_end)
