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
    deer_data = Trail.objects.filter(name='Deer Leap')
    return render_to_response("deer_leap_view.html", {"deer_data": deer_data})


def pico_view(request):
    return render_to_response("pico_view.html", {})


def mbr_view(request):
    return render_to_response("mbr.html", {})