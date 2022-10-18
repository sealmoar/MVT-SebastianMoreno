from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from family.models import Family

def create_familiar(request, name: str = "nombre", last_name: str = "apellido", email: str = 0, birth_day: str = 0):


    template = loader.get_template("template_family.html")

    familiar = Family(name=name, last_name=last_name, email=email, birth_day=birth_day)
    familiar.save()  # save into the DB

    context_dict = {"familiar": familiar}
    render = template.render(context_dict)
    return HttpResponse(render)

# Create your views here.
