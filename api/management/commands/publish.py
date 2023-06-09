import logging
import time

import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand

from settings import SECRETS

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc):
            print(f"Connected with result code {rc}")

        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect(SECRETS['mqtt']['host'], SECRETS['mqtt']['port'], 60)
        for i in range(3):
            client.publish('a/b', payload=i, qos=0, retain=False)
            print(f"send {i} to a/b")
            time.sleep(1)

        client.loop_forever()
