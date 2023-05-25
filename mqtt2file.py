import datetime
import paho.mqtt.client as mqtt
import csv

MQTTTOPICPREFIX = "energydata"
FILEPATHPREFIX = "csv"
MQTTHOST = "100.64.201.29"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(f"{MQTTTOPICPREFIX}/#", 0)


def on_disconnect(client, userdata, rc):
    print(f"Disconnect with result code {rc}")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # logger.debug(f"Received message on topic {msg.topic}: {msg.payload}")
    dt = datetime.datetime.utcnow()
    day_date = dt.strftime("%Y-%m-%d")
    file_name = f"{topic_to_filename(msg.topic)}_{day_date}.csv"
    file_path = f"/home/pi/energydata/{FILEPATHPREFIX}/{file_name}"
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([dt.isoformat(), bytes_to_str(msg.payload)])


def topic_to_filename(topic: str) -> str:
    return topic.replace("/", ".")


def bytes_to_str(b: bytes) -> str:
    return b.decode('utf8')


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(MQTTHOST, 1883, 60)
    client.loop_forever(retry_first_connection=True)


if __name__ == '__main__':
    main()
