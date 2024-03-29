
import paho.mqtt.client as mqtt
import json

mqtt_client_id = "my_id"
mqtt_server = 'MQTT_SERVER_NAME'
mqtt_client = mqtt.Client(client_id=mqtt_client_id, clean_session=True)

def on_message(client,userdata,msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    payload = json.loads(payload)    # String to dict

    if topic == 'topic1':
        pass

def on_connect(client,userdata,flags,rc):
    print(f"......... Connected to MQTT server ......... {rc}")
    topic_list = [
                  'topic1',
                  'topic2',
                  'topic3/#',
                 ]
    for topic in topic_list:
        logger.info("subscribe:\t"+topic)
        mqtt_client.subscribe(topic)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_server)
mqtt_client.loop_forever()