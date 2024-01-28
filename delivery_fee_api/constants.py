import os
from delivery_fee_api.structures.delivery_fee_params import DeliveryFeeParameters

with open(os.getenv("PATH_TO_DELIVERY_PARAMS"), 'r') as f_in:
    DELIVERY_FEE_PARAMETERS = DeliveryFeeParameters.model_validate_json(f_in.read())
