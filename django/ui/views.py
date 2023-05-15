from django.http import JsonResponse
from django.shortcuts import render

import paho.mqtt.client as mqtt

from .models import Sensor
from helpers.ml import *
from helpers.mqtthandlers import *

def index(request):
    return render(request, "ui/index.html")

def api(request):
    (
        ml_pabrik1_subsistem1,
        ml_pabrik1_subsistem2,
        ml_pabrik1_subsistem3,
    ) = get_ml_pabrik1_subsistem()
    (
        ml_pabrik2_subsistem1,
        ml_pabrik2_subsistem2,
        ml_pabrik2_subsistem3,
    ) = get_ml_pabrik2_subsistem()
    (
        ml_pabrik3_subsistem1,
        ml_pabrik3_subsistem2,
        ml_pabrik3_subsistem3,
    ) = get_ml_pabrik3_subsistem()
    ml_pabrik1, ml_pabrik2, ml_pabrik3 = get_ml_pabrik()
    ml_all = get_ml_all()

    data = {
        "ml_pabrik1_subsistem1": ml_pabrik1_subsistem1,
        "ml_pabrik1_subsistem2": ml_pabrik1_subsistem2,
        "ml_pabrik1_subsistem3": ml_pabrik1_subsistem3,
        "ml_pabrik2_subsistem1": ml_pabrik2_subsistem1,
        "ml_pabrik2_subsistem2": ml_pabrik2_subsistem2,
        "ml_pabrik2_subsistem3": ml_pabrik2_subsistem3,
        "ml_pabrik3_subsistem1": ml_pabrik3_subsistem1,
        "ml_pabrik3_subsistem2": ml_pabrik3_subsistem2,
        "ml_pabrik3_subsistem3": ml_pabrik3_subsistem3,
        "ml_pabrik1": ml_pabrik1,
        "ml_pabrik2": ml_pabrik2,
        "ml_pabrik3": ml_pabrik3,
        "ml_all": ml_all,
        "pabrik1": {
            "subsistem1": {
                "kadarproteinsusu": Sensor.objects.filter(
                    pabrik=1, subsistem=1, name="kadarproteinsusu"
                ).reverse()[0].value,
                "kekentalansusu": Sensor.objects.filter(
                    pabrik=1, subsistem=1, name="kekentalansusu"
                ).reverse()[0].value,
                "jumlahkuningtelur": Sensor.objects.filter(
                    pabrik=1, subsistem=1, name="jumlahkuningtelur"
                ).reverse()[0].value,
            },
            "subsistem2": {
                "kemerahandaging": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kemerahandaging"
                ).reverse()[0].value,
                "kadarlemak": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kadarlemak"
                ).reverse()[0].value,
                "kadarair": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kadarair"
                ).reverse()[0].value,
            },
            "subsistem3": {
                "microbacteria": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="microbacteria"
                ).reverse()[0].value,
                "kadarprotein": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="kadarprotein"
                ).reverse()[0].value,
                "keasamandaging": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="keasamandaging"
                ).reverse()[0].value,
            },
        },
        "pabrik2": {
            "subsistem1": {
                "kekuninganpadi": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kekuninganpadi"
                ).reverse()[0].value,
                "kebulatanpadi": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kebulatanpadi"
                ).reverse()[0].value,
                "kadarkarbohidrat": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kadarkarbohidrat"
                ).reverse()[0].value,
            },
            "subsistem2": {
                "kehijauan": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="kehijauan"
                ).reverse()[0].value,
                "kadarklorofil": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="kadarklorofil"
                ).reverse()[0].value,
                "amonia": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="amonia"
                ).reverse()[0].value,
            },
            "subsistem3": {
                "etilen": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="etilen"
                ).reverse()[0].value,
                "kadargula": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="kadargula"
                ).reverse()[0].value,
                "kepadatan": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="kepadatan"
                ).reverse()[0].value,
            },
        },
        "pabrik3": {
            "subsistem1": {
                "suhu": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="suhu"
                ).reverse()[0].value,
                "arahangin": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="arahangin"
                ).reverse()[0].value,
                "curahhujan": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="curahhujan"
                ).reverse()[0].value,
            },
            "subsistem2": {
                "kasiridle": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="kasiridle"
                ).reverse()[0].value,
                "ratepenjualan": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="ratepenjualan"
                ).reverse()[0].value,
                "jumlahpembayaran": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="jumlahpembayaran"
                ).reverse()[0].value,
            },
            "subsistem3": {
                "waiteridle": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="waiteridle"
                ).reverse()[0].value,
                "okupansirestoran": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="okupansirestoran"
                ).reverse()[0].value,
                "stokpiring": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="stokpiring"
                ).reverse()[0].value,
            }
        },
    }

    return JsonResponse(data)


client = mqtt.Client("danielw12345")
client.message_callback_add("prauas/pabrik1/subsistem1/kadarproteinsusu", on_message_111)
client.message_callback_add("prauas/pabrik1/subsistem1/kekentalansusu", on_message_112)
client.message_callback_add("prauas/pabrik1/subsistem1/jumlahkuningtelur", on_message_113)

client.message_callback_add("prauas/pabrik1/subsistem2/kadarproteinsusu", on_message_121)
client.message_callback_add("prauas/pabrik1/subsistem2/kekentalansusu", on_message_122)
client.message_callback_add("prauas/pabrik1/subsistem2/jumlahkuningtelur", on_message_123)

client.message_callback_add("prauas/pabrik1/subsistem3/kadarproteinsusu", on_message_131)
client.message_callback_add("prauas/pabrik1/subsistem3/kekentalansusu", on_message_132)
client.message_callback_add("prauas/pabrik1/subsistem3/jumlahkuningtelur", on_message_133)

client.message_callback_add("prauas/pabrik2/subsistem1/kadarproteinsusu", on_message_211)
client.message_callback_add("prauas/pabrik2/subsistem1/kekentalansusu", on_message_212)
client.message_callback_add("prauas/pabrik2/subsistem1/jumlahkuningtelur", on_message_213)

client.message_callback_add("prauas/pabrik2/subsistem2/kadarproteinsusu", on_message_221)
client.message_callback_add("prauas/pabrik2/subsistem2/kekentalansusu", on_message_222)
client.message_callback_add("prauas/pabrik2/subsistem2/jumlahkuningtelur", on_message_223)

client.message_callback_add("prauas/pabrik3/subsistem3/kadarproteinsusu", on_message_231)
client.message_callback_add("prauas/pabrik3/subsistem3/kekentalansusu", on_message_232)
client.message_callback_add("prauas/pabrik3/subsistem3/jumlahkuningtelur", on_message_233)

client.message_callback_add("prauas/pabrik3/subsistem1/kadarproteinsusu", on_message_311)
client.message_callback_add("prauas/pabrik3/subsistem1/kekentalansusu", on_message_312)
client.message_callback_add("prauas/pabrik3/subsistem1/jumlahkuningtelur", on_message_313)

client.message_callback_add("prauas/pabrik3/subsistem2/kadarproteinsusu", on_message_321)
client.message_callback_add("prauas/pabrik3/subsistem2/kekentalansusu", on_message_322)
client.message_callback_add("prauas/pabrik3/subsistem2/jumlahkuningtelur", on_message_323)

client.message_callback_add("prauas/pabrik3/subsistem3/kadarproteinsusu", on_message_331)
client.message_callback_add("prauas/pabrik3/subsistem3/kekentalansusu", on_message_332)
client.message_callback_add("prauas/pabrik3/subsistem3/jumlahkuningtelur", on_message_333)

client.connect("localhost", 1883)
client.subscribe("prauas/#")
client.loop_start()
