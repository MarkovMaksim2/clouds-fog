import os
import random
import time

import paho.mqtt.client as mqtt


def main() -> None:
    host = os.environ.get("FOG_BROKER_HOST", "fog-broker")
    port = int(os.environ.get("FOG_BROKER_PORT", "1883"))
    topic = os.environ.get("TOPIC", "factory/temperature")
    sleep_seconds = float(os.environ.get("SLEEP_SECONDS", "1"))

    client = mqtt.Client()
    while True:
        try:
            print(f"Trying to connect to {host}:{port}", flush=True)
            client.connect(host, port, keepalive=60)
            break
        except OSError:
            print("Connection error, timeout 1s", flush=True)
            time.sleep(1)

    while True:
        temperature = random.randint(60, 100)
        client.publish(topic, temperature)
        print(f"temperature={temperature}", flush=True)
        time.sleep(sleep_seconds)


if __name__ == "__main__":
    print("Starting sensor...", flush=True)
    main()
