from django.shortcuts import render
from models import Rapor
from django.http import Http404


def img(request,img_id):
    image = Rapor.objects.get(pk=img_id)
    if image is not None:
        return render(request,'img/img.html',{'image':image})
    else:
        raise Http404('Fotoğraf Yok')

# Create your views here.
