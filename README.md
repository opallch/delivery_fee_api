# Delivery Fee API
This repository contains the implementation of an HTTP API (single POST endpoint `delivery-fee-calculator`) which could be used for calculating the delivery fee, using Flask. All payloads and parameters needed for calculating the delivery fee are implemented as pydantic classes in order to have a better validation.

## Running the API & Prerequisites
Running the API (with development server) is recommended for local development, but running in Docker (with gunicorn) is also possible (this is implemented mainly as an option for deployment). First, clone this repository and go to the root of this repository.

### Running without Development Server
1. Prerequisites: 
    - `make`
    - `python3.10`
    - `venv`
2. (optional) Set up the API running port: `FLASK_PORT` in [`Makefile`](Makefile)
3. Install python dependencies
```sh
make
```
4. Activate the virtual environment
```sh
source ./venv/bin/activate
```

### Running in Docker (with gunicorn)
1. Prerequisites: 
    - `make`
    - `python3.10`
    - `venv`
    - `docker`
    - `docker-compose`
2. (optional) Set up the Docker port running the API: `FLASK_PORT` in [`.env`](.env)
3. `requirements.in` lists all required packages and `requirement.txt` includes also the exact version of all dependencies. **If you have added any new package to `requirement.in` during development**, update the `requirements.txt` before building the container to ensure development and deployment are using the exact same dependencies:
```
make requirements.txt
```
4. run the docker daemon (if Docker desktop is installed, simply start it)
5. build and run the container 
```
docker compose build
docker compose up
```

## Request and Response Payload
### Sending POST Request
No matter you are running the API in or outside the Docker, you should now be able to send a POST request at `localhost:FLASK_PORT/delivery-fee-calculator` (by default: [localhost:8080/delivery-fee-calculator](localhost:8080/delivery-fee-calculator)). 

The request payload should contain the following fields:
| Field             | Type  | Description                                                               | Example value                             |
|:---               |:---   |:---                                                                       |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                                   |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.      |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.                   |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). |__2024-01-15T13:00:00Z__                   |
For Example:
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
```

### Success Response Payload
| Field         | Type  | Description                           | Example value             |
|:---           |:---   |:---                                   |:---                       |
|delivery_fee   |Integer|Calculated delivery fee __in cents__.  |__710__ (710 cents = 7.10€)|

Example:
```json
{"delivery_fee": 710}
```

### Failure Response Payload
In case of any HTTP Error (e.g. BadRequest is raised when the request payload contains invalid input),
the response payload contains:
| Field         | Type  | Description                           | Example value             |
|:---           |:---   |:---                                   |:---                       |
|code   |Integer|HTTP error code|404|
|name   |String|HTTP error name|Bad Request|
|description   |String|HTTP error description (can also include cause of the error)|(see example)|
|status   |Integer||error|

For instance, if a string `'Hello'` is given as `delivery_instance` in the request payload, the response payload will look like :
```json
{
  "code": 400,
  "name": "Bad Request",
  "description": "1 validation error for DeliveryFeeRequestPayload\ndelivery_distance\n  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='Hello', input_type=str]\n    For further information visit https://errors.pydantic.dev/2.5/v/int_parsing",
  "status": "error"
}
```

## Customizing the Delivery Fee Parameters
There are several parameters for calculating the final delivery cost in the API which are stored in [`delivery_fee_api/config/delivery_fee_parameters.json`](delivery_fee_api/config/delivery_fee_parameters.json), feel free to customize them upon any policy changes:

**Policy regarding cart value**: 
- If the cart value is less than `small_cart_value_cent`, a surcharge of (cart value - `small_cart_value_cent`) is applied.
- If the cart value exceeds `large_cart_value_cent`, delivery will be free.
- Max. of "max_delivery_fee_cent" can be charged for delivery.

**Policy regarding delivery distance**: The first `init_distance_meter` will cost `init_distance_fee_cent`; after that, `distance_fee_per_interval_cent` is charged per `distance_interval_meter`.

**Policy regarding no. of cart items**: When the no. of cart items is more than `surcharge_free_n_items`,
`surcharge_per_item_cent` is charged per item. An extra one-time surcharge `many_items_surcharge_cent` will be charged when there are `extra_surcharge_n_items` or more cart items.

**Policy regarding to order during rush hours**: When the order
is placed during the rush time, the total fee will be multiplied by `rush_multiplier` (result is rounded up if the multiplier is a floating number). Rush hours are defined by `rush_days`, `rush_hours_begin` and `rush_hours_end` (in `time_zone`, by default UTC).

**NOTES**: Parameters regarding charges should be set up **in CENTS**.

## Logging
Extra loggers for HTTP requests, responses & errors are available for docker deployment.
You may configure the `LOG_PATH` for the container and `HOST_LOG_PATH` for the binded volumne on the host machine in [.env](.env). 
Logs can then be found in `delivery_fee_api_http.log` under the configured path.
