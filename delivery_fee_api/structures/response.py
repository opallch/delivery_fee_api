from pydantic import BaseModel, Field

# TODO create Parent Response Class (Success, Failure)
class DeliveryFeeResponse(BaseModel):
    delivery_fee: int