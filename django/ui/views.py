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
                ).last().value,
                "kekentalansusu": Sensor.objects.filter(
                    pabrik=1, subsistem=1, name="kekentalansusu"
                ).last().value,
                "jumlahkuningtelur": Sensor.objects.filter(
                    pabrik=1, subsistem=1, name="jumlahkuningtelur"
                ).last().value,
            },
            "subsistem2": {
                "kemerahandaging": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kemerahandaging"
                ).last().value,
                "kadarlemak": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kadarlemak"
                ).last().value,
                "kadarair": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kadarair"
                ).last().value,
            },
            "subsistem3": {
                "microbacteria": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="microbacteria"
                ).last().value,
                "kadarprotein": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="kadarprotein"
                ).last().value,
                "keasamandaging": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="keasamandaging"
                ).last().value,
            },
        },
        "pabrik2": {
            "subsistem1": {
                "kekuninganpadi": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kekuninganpadi"
                ).last().value,
                "kebulatanpadi": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kebulatanpadi"
                ).last().value,
                "kadarkarbohidrat": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kadarkarbohidrat"
                ).last().value,
            },
            "subsistem2": {
                "kehijauan": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="kehijauan"
                ).last().value,
                "kadarklorofil": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="kadarklorofil"
                ).last().value,
                "amonia": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="amonia"
                ).last().value,
            },
            "subsistem3": {
                "etilen": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="etilen"
                ).last().value,
                "kadargula": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="kadargula"
                ).last().value,
                "kepadatan": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="kepadatan"
                ).last().value,
            },
        },
        "pabrik3": {
            "subsistem1": {
                "suhu": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="suhu"
                ).last().value,
                "arahangin": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="arahangin"
                ).last().value,
                "curahhujan": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="curahhujan"
                ).last().value,
            },
            "subsistem2": {
                "kasiridle": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="kasiridle"
                ).last().value,
                "ratepenjualan": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="ratepenjualan"
                ).last().value,
                "jumlahpembayaran": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="jumlahpembayaran"
                ).last().value,
            },
            "subsistem3": {
                "waiteridle": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="waiteridle"
                ).last().value,
                "okupansirestoran": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="okupansirestoran"
                ).last().value,
                "stokpiring": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="stokpiring"
                ).last().value,
            }
        },
    }

    return JsonResponse(data)


client = mqtt.Client("danielw12345")
client.message_callback_add("prauas/pabrik1/subsistem1/kadarproteinsusu", on_message_111)
client.message_callback_add("prauas/pabrik1/subsistem1/kekentalansusu", on_message_112)
client.message_callback_add("prauas/pabrik1/subsistem1/jumlahkuningtelur", on_message_113)

client.message_callback_add("prauas/pabrik1/subsistem2/kemerahandaging", on_message_121)
client.message_callback_add("prauas/pabrik1/subsistem2/kadarlemak", on_message_122)
client.message_callback_add("prauas/pabrik1/subsistem2/kadarair", on_message_123)

client.message_callback_add("prauas/pabrik1/subsistem3/microbacteria", on_message_131)
client.message_callback_add("prauas/pabrik1/subsistem3/kadarprotein", on_message_132)
client.message_callback_add("prauas/pabrik1/subsistem3/keasamandaging", on_message_133)

client.message_callback_add("prauas/pabrik2/subsistem1/kekuninganpadi", on_message_211)
client.message_callback_add("prauas/pabrik2/subsistem1/kebulatanpadi", on_message_212)
client.message_callback_add("prauas/pabrik2/subsistem1/kadarkarbohidrat", on_message_213)

client.message_callback_add("prauas/pabrik2/subsistem2/kehijauan", on_message_221)
client.message_callback_add("prauas/pabrik2/subsistem2/kadarklorofil", on_message_222)
client.message_callback_add("prauas/pabrik2/subsistem2/amonia", on_message_223)

client.message_callback_add("prauas/pabrik2/subsistem3/etilen", on_message_231)
client.message_callback_add("prauas/pabrik2/subsistem3/kadargula", on_message_232)
client.message_callback_add("prauas/pabrik2/subsistem3/kepadatan", on_message_233)

client.message_callback_add("prauas/pabrik3/subsistem1/suhu", on_message_311)
client.message_callback_add("prauas/pabrik3/subsistem1/arahangin", on_message_312)
client.message_callback_add("prauas/pabrik3/subsistem1/curahhujan", on_message_313)

client.message_callback_add("prauas/pabrik3/subsistem2/kasiridle", on_message_321)
client.message_callback_add("prauas/pabrik3/subsistem2/ratepenjualan", on_message_322)
client.message_callback_add("prauas/pabrik3/subsistem2/jumlahpembayaran", on_message_323)

client.message_callback_add("prauas/pabrik3/subsistem3/waiteridle", on_message_331)
client.message_callback_add("prauas/pabrik3/subsistem3/okupansirestoran", on_message_332)
client.message_callback_add("prauas/pabrik3/subsistem3/stokpiring", on_message_333)

client.connect("localhost", 1883)
client.subscribe("prauas/#")
client.loop_start()
