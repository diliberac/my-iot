FROM python:3.9-slim-buster
LABEL description="MQTT_CLIENT"
LABEL maintainer="cfreire@cfreire.com.pt"
ARG MQTT_VERSION='DEV'
ENV MQTT_VERSION=${MQTT_VERSION}
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV TZ=Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["python3", "sensors.py"]

# docker run --rm -it --link redis mqtt_client:0.1.0