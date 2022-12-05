from django.urls import path, include
from .views import (home,  newParking, editParking, deleteParking,
                    outParking, payParking, historicParking)

urlpatterns = [
    path("", home),
    path("parking", newParking, name="new-parking"),
    path("parking/<int:id>/out", outParking, name="out-parking"),
    path("parking/<int:id>/pay", payParking, name="pay-parking"),
    path("parking/<str:plate>", historicParking, name="historic-parking"),
    path("edit/<int:id>", editParking, name="edit-parking"),
    path("delete/<int:id>", deleteParking, name="delete-parking"),

    # path("salvar/", salvar, name="salvar"),
    # path("update/<int:id>", update, name="update"),
    # path("delete/<int:id>", delete, name="delete")
]
