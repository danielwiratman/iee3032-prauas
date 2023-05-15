from ui.models import Sensor

def on_message_111(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=1, name="kadarproteinsusu", value=message.payload.decode())

def on_message_112(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=1, name="kekentalansusu", value=message.payload.decode())

def on_message_113(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=1, name="jumlahkuningtelur", value=message.payload.decode())

def on_message_121(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=2, name="kemerahandaging", value=message.payload.decode())

def on_message_122(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=2, name="kadarlemak", value=message.payload.decode())

def on_message_123(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=2, name="kadarair", value=message.payload.decode())

def on_message_131(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=3, name="microbacteria", value=message.payload.decode())

def on_message_132(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=3, name="kadarprotein", value=message.payload.decode())

def on_message_133(client, userdata, message):
    Sensor.objects.create(pabrik=1, subsistem=3, name="keasamandaging", value=message.payload.decode())

def on_message_211(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=1, name="kekuninganpadi", value=message.payload.decode())

def on_message_212(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=1, name="kebulatanpadi", value=message.payload.decode())

def on_message_213(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=1, name="kadarkarbohidrat", value=message.payload.decode())

def on_message_221(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=2, name="kehijauan", value=message.payload.decode())

def on_message_222(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=2, name="kadarklorofil", value=message.payload.decode())
    
def on_message_223(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=2, name="amonia", value=message.payload.decode())

def on_message_231(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=3, name="etilen", value=message.payload.decode())

def on_message_232(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=3, name="kadargula", value=message.payload.decode())

def on_message_233(client, userdata, message):
    Sensor.objects.create(pabrik=2, subsistem=3, name="kepadatan", value=message.payload.decode())

def on_message_311(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=1, name="suhu", value=message.payload.decode())

def on_message_312(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=1, name="arahangin", value=message.payload.decode())

def on_message_313(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=1, name="curahhujan", value=message.payload.decode())

def on_message_321(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=2, name="kasiridle", value=message.payload.decode())

def on_message_322(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=2, name="ratepenjualan", value=message.payload.decode())

def on_message_323(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=2, name="jumlahpembayaran", value=message.payload.decode())

def on_message_331(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=3, name="waiteridle", value=message.payload.decode())

def on_message_332(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=3, name="okupansirestoran", value=message.payload.decode())

def on_message_333(client, userdata, message):
    Sensor.objects.create(pabrik=3, subsistem=3, name="stokpiring", value=message.payload.decode())
