from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from bootstrap_app.models import Trail


def index_view(request):
    return render_to_response("index.html", {})
    # return HttpResponse("OMGITSAWEBSITE!!!!!!")


def about_me_view(request):
    return render_to_response("about_me.html", {})


def deer_leap_view(request):
    deer_data = Trail.objects.get(name='Deer Leap')
    print(deer_data)
    return render_to_response("deer_leap_view.html", {"deer_data": deer_data})


def pico_view(request):
    pico_data = Trail.objects.get(name='Pico Peak')
    return render_to_response("pico_view.html", {'pico': pico_data})


def mbr_view(request):
    mbr_data = Trail.objects.get(name="Mount Tom")
    return render_to_response("mbr.html", {'mbr': mbr_data})