from pydantic import BaseModel, Field


class DeliveryFeeResponse(BaseModel):
    delivery_fee: int
