from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#from django.urls import reverse_lazy
#from django.views.generic import DetailView, ListView
#from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "expediente/index.html")

# Create your views here.
def expediente_create(request):
    if request.method == "POST":
        form = forms.ExpedienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expediente:index")
    else:
        form = forms.ExpedienteForm()
        return render(request, "expediente/expediente_create.html", {"form": form})


def expediente_list(request):
    expedientes = models.Expediente.objects.all()
    context = {"expedientes": expedientes}
    return render(request, "expediente/expediente_list.html", context)

def expediente_detail(request, id):
    expediente = models.Expediente.objects.get(id=id)
    context = {"expediente": expediente}
    return render(request, "expediente/expediente_detail.html", context)



#class ExpedienteCreate(CreateView):
#    model = models.Expediente
 #   form_class = forms.ExpedienteForm
  #  success_url = reverse_lazy("expediente:index")


def expediente_delete(request, id):
    expediente = models.Expediente.objects.get(id=id)
    if request.method == "POST":
        expediente.delete()
        return redirect("expediente:expediente_list")
    return render(request, "expediente/expediente_confirm_delete.html", {"expediente": expediente})


#class ExpedienteDelete(DeleteView):
 #   model = models.Expediente
  #  success_url = reverse_lazy("expediente:expediente_list")


def expediente_update(request, id):
    expediente = models.Expediente.objects.get(id=id)
    if request.method == "POST":
        form = forms.ExpedienteForm(request.POST, instance=expediente)
        if form.is_valid():
            form.save()
            return redirect("expediente:expediente_list")
    else:
        form = forms.ExpedienteForm(instance=expediente)
    return render(request, "expediente/expediente_update.html", {"form": form})


#class ExpedienteUpdate(UpdateView):
 #   model = models.Expediente
  #  success_url = reverse_lazy("expediente:expediente_list")
   # form_class = forms.ExpedienteForm


#class ExpedienteDetail(DetailView):
 #   model = models.Expediente
def juzgado(request: HttpRequest) -> HttpResponse:
    return render(request, "expediente/juzgado.html")

def juzgado_create(request):
    if request.method == "POST":
        form = forms.JuzgadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expediente:index")
    else:
        form = forms.JuzgadoForm()
        return render(request, "expediente/juzgado_create.html", {"form": form})


def evidencia(request: HttpRequest) -> HttpResponse:
    return render(request, "expediente/evidencia.html")


def evidencia_list(request):
    evidencias = models.Evidencia.objects.all()
    context = {"evidencias": evidencias}
    return render(request, "expediente/evidencia_list.html", {"evidencias": evidencias})

def evidencia_detail(request, id):
    evidencia = models.Evidencia.objects.get(id=id)
    context = {"evidencia": evidencia}
    return render(request, "expediente/evidencia_detail.html", context)

def evidencia_create(request):
    if request.method == "POST":
        form = forms.EvidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expediente:evidencia")
    else:
        form = forms.EvidenciaForm()
    return render(request, "expediente/evidencia_create.html", {"form": form})




def evidencia_delete(request, id):
    evidencia = models.Evidencia.objects.get(id=id)
    if request.method == "POST":
        evidencia.delete()
        return redirect("expediente:evidencia_list")
    return render(request, "expediente/evidencia_confirm_delete.html", {"evidencia": evidencia})


def evidencia_update(request, id):
    evidencia = models.Evidencia.objects.get(id=id)
    if request.method == "POST":
        form = forms.EvidenciaForm(request.POST, instance=evidencia)
        if form.is_valid():
            form.save()
            return redirect("expediente:evidencia_list")
    else:
        form = forms.EvidenciaForm(instance=evidencia)
    return render(request, "expediente/evidencia_update.html", {"form": form})

   