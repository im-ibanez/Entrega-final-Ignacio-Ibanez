from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "expediente/index.html")

# Create your views here.
# def expediente_categoria_list(request):
#     categorias = models.Expediente.objects.all()
#     context = {"categorias": categorias}
#     return render(request, "expediente/expediente_categoria_list.html", context)


class ExpedienteList(ListView):
    model = models.Expediente


# def expediente_categoria_create(request):
#     if request.method == "POST":
#         form = forms.ExpedienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("expediente:index")
#     else:
#         form = forms.ExpedienteForm()
#     return render(request, "expediente/expediente_categoria_create.html", {"form": form})


class ExpedienteCreate(CreateView):
    model = models.Expediente
    form_class = forms.ExpedienteForm
    success_url = reverse_lazy("expediente:index")


# def expediente_categoria_delete(request, id):
#     categoria = models.Expediente.objects.get(id=id)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("expediente:expediente_categoria_list")
#     return render(request, "expediente/expediente_categoria_delete.html", {"categoria": categoria})


class ExpedienteDelete(DeleteView):
    model = models.Expediente
    success_url = reverse_lazy("expediente:expediente_list")


# def expediente_categoria_update(request, id):
#     categoria = models.Expediente.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.ExpedienteForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("expediente:expediente_categoria_list")
#     else:
#         form = forms.ExpedienteForm(instance=categoria)
#     return render(request, "expediente/expediente_categoria_update.html", {"form": form})


class ExpedienteUpdate(UpdateView):
    model = models.Expediente
    success_url = reverse_lazy("expediente:expediente_list")
    form_class = forms.ExpedienteForm


class ExpedienteDetail(DetailView):
    model = models.Expediente