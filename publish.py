import time
from random import random
import paho.mqtt.client as mqtt


def str_to_bytes(s: str) -> bytes:
    return s.encode('utf8')


def publish_2(client):
    value = 10 + (random() * 10)
    client.publish("energydata/room1/power1", payload=value, qos=0, retain=False)


def main():
    client = mqtt.Client()

    client.connect("100.64.201.29", 1883, 60)
    for k in range(0, 3600):
        if k % 100 == 0:
            print(".", end="")
            time.sleep(0.2)
        publish_2(client)
        time.sleep(0.01)
    print()


if __name__ == '__main__':
    main()
