import paho.mqtt.client as mqtt

broker = 'broker.hivemq.com'  # Broker publik, bisa diganti sesuai kebutuhan
topic = 'universitas teknologi yogyakarta/sahwan'

def on_connect(client, userdata, flags, rc):
    print('Terhubung ke broker dengan kode:', rc)
    client.subscribe(topic)
    print(f'Berlangganan ke topik: {topic}')

def on_message(client, userdata, msg):
    print(f"Pesan diterima di topik {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

print('Menunggu pesan... Tekan Ctrl+C untuk keluar.')
client.loop_forever()
