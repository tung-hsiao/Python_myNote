
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json

mqtt_client_id = "my_id"
mqtt_server = 'MQTT_SERVER_NAME'
mqtt_client = mqtt.Client(client_id=mqtt_client_id, clean_session=True)
mqtt_client.connect(mqtt_server)

fake_signal = { 'key1':'xxx',
                'key2':2,
                'dict1':{'height': 179, 'weight':66},
                'list1':[7,77,777]
                }

# Approach 1
publish.single("topic1", json.dumps(fake_signal), qos=1, hostname=mqtt_server)

# Approach 2
mqtt_client.publish("topic1", json.dumps(payload), qos=1)