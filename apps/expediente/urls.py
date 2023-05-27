from django.urls import path

from . import views

# *********** URLS basadas en funciones
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("expediente_categorias_listado/", views.expediente_categorias_list, name="expediente_categorias_list"),
#     path("expediente_categorias_create/", views.expediente_categorias_create, name="expediente_categorias_create"),
#     path("expediente_categorias_delete/<int:id>", views.expediente_categorias_delete, name="expediente_categorias_delete"),
#     path("expediente_categorias_update/<int:id>", views.expediente_categorias_delete, name="expediente_categorias_delete"),
# ]

# *********** URLS basadas en clases
urlpatterns = [
    path("", views.index, name="index"),
    path("expediente/list/", views.ExpedienteList.as_view(), name="expediente_list"),
    path("expediente/create/", views.ExpedienteCreate.as_view(), name="expediente_create"),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "expediente/delete/<int:pk>", views.ExpedienteDelete.as_view(), name="expediente_delete"
    ),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "expediente/update/<int:pk>", views.ExpedienteUpdate.as_view(), name="expediente_update"
    ),
    path(
        "expediente/detail/<int:pk>", views.ExpedienteDetail.as_view(), name="expediente_detail"
    ),
]
