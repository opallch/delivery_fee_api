from dateutil import parser
from pydantic import BaseModel, Field

from delivery_fee_api.constants import *

 
class DeliveryFeeRequestPayload(BaseModel):
    cart_value: int # in cents
    delivery_distance: int # in meters
    number_of_items: int
    time: str # in ISO format, e.g. 2024-01-15T13:00:00Z
    
    # TODO custom validators