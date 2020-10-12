from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'photos/home.html', {'images':images})


def search_image(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("article")
        images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message, "images":images})

    else:
        message = "Enter search item!"
        return render(request, 'photos/search.html', {"message":message})