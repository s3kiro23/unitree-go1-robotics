import paho.mqtt.client as mqtt
from typing import Any, Callable

class MQTTManager:
    """
    Gère la connexion MQTT et les interactions pour un client MQTT.
    """

    def __init__(self, broker_address: str = "192.168.12.1", port: int = 1883, keepalive: int = 60) -> None:
        """
        Initialise le client MQTT et configure les gestionnaires d'événements.

        :param brokeraddress: Adresse du broker MQTT.
        :param port: Port pour la connexion MQTT.
        :param keepalive: Période de keepalive en secondes.
        """
        self.client = mqtt.Client()
        self.setup_event_handlers()

        self.client.connect(broker_address, port, keepalive)
        self.client.loop_start()

    def setup_event_handlers(self) -> None:
        """
        Configure les gestionnaires d'événements pour le client MQTT.
        """
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe
        self.client.on_log = self.on_log

    def on_connect(self, mqttc: mqtt.Client, obj: Any, flags: dict, rc: int) -> None:
        print("rc: " + str(rc))

    def on_message(self, mqttc: mqtt.Client, obj: Any, msg: mqtt.MQTTMessage) -> None:
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def on_publish(self, mqttc: mqtt.Client, obj: Any, mid: int) -> None:
        print("mid: " + str(mid))

    def on_subscribe(self, mqttc: mqtt.Client, obj: Any, mid: int, granted_qos: int) -> None:
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc: mqtt.Client, obj: Any, level: int, string: str) -> None:
        print(string)

if __name__ == "__main__":
    mqtt_manager = MQTTManager("192.168.12.1")
