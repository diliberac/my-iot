# Mqtt Client

Client of mosquitto MQTT Protocol with history on mongo and state on redis

**Mongo**
    docker run -itd --name mongo -p 27017:27017 --restart on-failure -v mongo_database:/data/db mongo

**Redis**
    docker run -itd --name redis -p 6379:6379/tcp --restart on-failure redis

**mqtt_client**
   docker build -t mqtt_client .
   docker run -d --rm --link redis --link mongo --name mqtt_client mqtt_client
