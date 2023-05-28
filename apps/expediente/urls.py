from django.urls import path

from . import views

# *********** URLS basadas en funciones
urlpatterns = [
    path("", views.index, name="index"),
    path("expediente_listado/", views.expediente_list, name="expediente_list"),
    path("expediente_create/", views.expediente_create, name="expediente_create"),
    path("expediente_confirm_delete/<int:id>", views.expediente_delete, name="expediente_delete"),
    path("expediente_update/<int:id>", views.expediente_update, name="expediente_update"),
    path("expediente_detail/<int:id>", views.expediente_detail, name="expediente_detail"),
    path("juzgado/", views.juzgado, name="juzgado"),
    path("juzgado/create/", views.juzgado_create, name="juzgado_create"),
    path("evidencia/", views.evidencia, name="evidencia"),
    path("evidencia_create/", views.evidencia_create, name="evidencia_create"),
    path("evidencia_confirm_delete/<int:id>", views.evidencia_delete, name="evidencia_confirm_delete"),
    path("evidencia_update/<int:id>", views.evidencia_update, name="evidencia_update"),
    path("evidencia_detail/<int:id>", views.evidencia_detail, name="evidencia_detail"),
    path("evidencia_listado/", views.evidencia_list, name="evidencia_list"),
]

# *********** URLS basadas en clases
#urlpatterns = [
 #   path("", views.index, name="index"),
  #  path("expediente/list/", views.ExpedienteList.as_view(), name="expediente_list"),
   # path("expediente/create/", views.ExpedienteCreate.as_view(), name="expediente_create"),
    ## ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
   # path(
   #     "expediente/delete/<int:pk>", views.ExpedienteDelete.as_view(), name="expediente_delete"
   # ),
   # # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
   # path(
   #     "expediente/update/<int:pk>", views.ExpedienteUpdate.as_view(), name="expediente_update"
   # ),
   # path(
   #     "expediente/detail/<int:pk>", views.ExpedienteDetail.as_view(), name="expediente_detail"
   # ),
#]
#
# urlpatterns += [
   # path("", views.index_evidencia, name="index_evidencia"),
   # path("evidencia/list/", views.ExpedienteList.as_view(), name="evidencia_list"),
   # path("evidencia/create/", views.ExpedienteCreate.as_view(), name="evidencia_create"),
   # # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
  #  path(
  #      "evidencia/delete/<int:pk>", views.ExpedienteDelete.as_view(), name="evidencia_delete"
   # ),
  #  # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
   # path(
    #    "evidencia/update/<int:pk>", views.ExpedienteUpdate.as_view(), name="evidencia_update"
   # ),
    #path(
    #    "evidencia/detail/<int:pk>", views.ExpedienteDetail.as_view(), name="evidencia_detail"
    #),    
