import paho.mqtt.client as mqtt
import time

broker = 'broker.hivemq.com'  # Broker publik, bisa diganti sesuai kebutuhan
topic = 'universitas teknologi yogyakarta/sahwan'

client = mqtt.Client()
client.connect(broker, 1883, 60)

for i in range(1, 6):
    pesan = f"Pesan ke-{i} dari UTY Sahwan"
    client.publish(topic, pesan)
    print(f"Terkirim: {pesan}")
    time.sleep(1)

client.disconnect()
print("Selesai mengirim 5 pesan.")
