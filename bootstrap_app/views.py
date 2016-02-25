from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.

def index_view(request):
    return render_to_response("index.html", {})
    # return HttpResponse("OMGITSAWEBSITE!!!!!!")


def about_me_view(request):
    return render_to_response("about_me.html", {})


def deer_leap_view(request):
    return render_to_response("deer_leap_view.html", {})


def pico_view(request):
    return render_to_response("pico_view.html", {})


def mbr_view(request):
    return render_to_response("mbr.html", {})