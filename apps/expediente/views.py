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


def index_evidencia(request: HttpRequest) -> HttpResponse:
    return render(request, "expediente/index_evidencia.html")


 # def evidencia_list(request):
#     categorias = models.Evidencia.objects.all()
#     context = {"categorias": categorias}
#     return render(request, "expediente/evidencia_list.html", {"categorias": categorias})


# def expediente_create(request):
#     if request.method == "POST":
#         form = forms.ExpedienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("expediente:index")
#     else:
#         form = forms.ExpedienteForm()
#     return render(request, "expediente/expediente_create.html", {"form": form})




# def expediente_delete(request, id):
#     categoria = models.Expediente.objects.get(id=id)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("expediente:expediente_list")
#     return render(request, "expediente/expediente_delete.html", {"categoria": categoria})


#def evidencia_update(request, id):
#     categoria = models.Expediente.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.ExpedienteForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("expediente:expediente_list")
#     else:
#         form = forms.ExpedienteForm(instance=categoria)
#     return render(request, "expediente/expediente_update.html", {"form": form})

   