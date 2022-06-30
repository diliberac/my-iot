import logging
import datetime
from os import environ

import paho.mqtt.client as mqtt
import redis

import settings as sets
import database

connection = redis.Redis(host=sets.REDIS_SERVER, 
    port=sets.REDIS_PORT,
    decode_responses=True, 
    db=sets.REDIS_DB_DEFAULT)

print(connection.ping())

# logging
log = logging.getLogger("mqtt_client")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        log.info('Connection OK')
        client.subscribe(sets.CFREIRE_FEED)
        client.message_callback_add(sets.CFREIRE_FEED, on_message)
        
def on_message(client, userdata, msg):
    log.debug("topic: %s \t value: %s" % (msg.topic, msg.payload))
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    topic = msg.topic.split('/')[3]
    database.insert(topic, dict(timestamp = now, value = float(msg.payload)))
    connection.set(topic, float(msg.payload))
    
def main():
    if "MQTT_VERSION" in environ:
        __version__ = environ["MQTT_VERSION"]
    else:
        __version__ = 'DEV'

    log.info(f'Starting "mqtt_client" version: {__version__}')
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(sets.CFREIRE_IP, sets.CFREIRE_PORT, 60)
    client.loop_forever()

if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)-15s %(levelname)-8s %(name)-20s %(message)s",
    level=logging.DEBUG)
    main()


