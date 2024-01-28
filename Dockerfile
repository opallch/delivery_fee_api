FROM python:3.10-slim

WORKDIR /delivery_fee_api

# install python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy source files to docker
COPY . .

CMD gunicorn --config python:delivery_fee_api.config.gunicorn_config "delivery_fee_api:create_app()"
