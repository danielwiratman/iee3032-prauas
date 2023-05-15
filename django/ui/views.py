from django.http import JsonResponse
from django.shortcuts import render
from .models import Sensor


def index(request):
    return render(request, "ui/index.html")


# Create your views here.
# create a new view returning a json response


def api():
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
                ).reverse()[0],
                "kekentalansusu": Sensor.objects.filter(
                    pabrik=1, subsistem=1, name="kekentalansusu"
                ).reverse()[0],
                "jumlahkuningtelur": Sensor.objects.filter(
                    pabrik=1, subsistem=1, name="jumlahkuningtelur"
                ).reverse()[0],
            },
            "subsistem2": {
                "kemerahandaging": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kemerahandaging"
                ).reverse()[0],
                "kadarlemak": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kadarlemak"
                ).reverse()[0],
                "kadarair": Sensor.objects.filter(
                    pabrik=1, subsistem=2, name="kadarair"
                ).reverse()[0],
            },
            "subsistem3": {
                "microbacteria": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="microbacteria"
                ).reverse()[0],
                "kadarprotein": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="kadarprotein"
                ).reverse()[0],
                "keasamandaging": Sensor.objects.filter(
                    pabrik=1, subsistem=3, name="keasamandaging"
                ).reverse()[0],
            },
        },
        "pabrik2": {
            "subsistem1": {
                "kekuninganpadi": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kekuninganpadi"
                ).reverse()[0],
                "kebulatanpadi": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kebulatanpadi"
                ).reverse()[0],
                "kadarkarbohidrat": Sensor.objects.filter(
                    pabrik=2, subsistem=1, name="kadarkarbohidrat"
                ).reverse()[0],
            },
            "subsistem2": {
                "kehijauan": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="kehijauan"
                ).reverse()[0],
                "kadarklorofil": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="kadarklorofil"
                ).reverse()[0],
                "amonia": Sensor.objects.filter(
                    pabrik=2, subsistem=2, name="amonia"
                ).reverse()[0],
            },
            "subsistem3": {
                "etilen": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="etilen"
                ).reverse()[0],
                "kadargula": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="kadargula"
                ).reverse()[0],
                "kepadatan": Sensor.objects.filter(
                    pabrik=2, subsistem=3, name="kepadatan"
                ).reverse()[0],
            },
        },
        "pabrik3": {
            "subsistem1": {
                "suhu": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="suhu"
                ).reverse()[0],
                "arahangin": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="arahangin"
                ).reverse()[0],
                "curahhujan": Sensor.objects.filter(
                    pabrik=3, subsistem=1, name="curahhujan"
                ).reverse()[0],
            },
            "subsistem2": {
                "kasiridle": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="kasiridle"
                ).reverse()[0],
                "ratepenjualan": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="ratepenjualan"
                ).reverse()[0],
                "jumlahpembayaran": Sensor.objects.filter(
                    pabrik=3, subsistem=2, name="jumlahpembayaran"
                ).reverse()[0],
            },
            "subsistem3": {
                "waiteridle": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="waiteridle"
                ).reverse()[0],
                "okupansirestoran": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="okupansirestoran"
                ).reverse()[0],
                "stokpiring": Sensor.objects.filter(
                    pabrik=3, subsistem=3, name="stokpiring"
                ).reverse()[0],
            }
        },
    }

    return JsonResponse(data)
