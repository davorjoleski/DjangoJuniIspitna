from django.shortcuts import render, redirect

from .models import Parce, Dizajner
from .form import PapaForm


def index(request):
    return render(request, 'index.html')


def papa(request):
    if request.method == "POST":
        form_data = PapaForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            repair = form_data.save(commit=False)
            repair.user = request.user
            repair.image = form_data.cleaned_data['image']
            repair.cena = form_data.cleaned_data['cena']
            repair.ime = form_data.cleaned_data['ime']
            repair.boja = form_data.cleaned_data['boja']

            repair.save()
            return redirect("/papa")

    query = Parce.objects.filter(user=request.user).all()
    context = {"parce": query, "form": PapaForm}

    return render(request, 'papa.html', context=context)

def blog(request):
    # Retrieve all Parce objects for display on the blog page
    parces = Parce.objects.all()
    context = {"parce": parces}
    return render(request, 'blog.html', context=context)
# Create your views here.
