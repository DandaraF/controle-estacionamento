from django.urls import path

from core.views import ParkingViewSet

urlpatterns = [
    path("", ParkingViewSet.get_parkings),
    path("parking", ParkingViewSet.post, name="new-parking"),
    path("parking/<int:id>/out", ParkingViewSet.output, name="out-parking"),
    path("parking/<int:id>/pay", ParkingViewSet.payment, name="pay-parking"),
    path("parking/<str:plate>", ParkingViewSet.historic, name="historic"),
    path("edit/<int:id>", ParkingViewSet.update, name="edit-parking"),
    path("delete/<int:id>", ParkingViewSet.delete, name="delete-parking"),

    # path("salvar/", salvar, name="salvar"),
    # path("update/<int:id>", update, name="update"),
    # path("delete/<int:id>", delete, name="delete")
]
