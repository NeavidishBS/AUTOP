from django.urls import path

from .views import(
    HomePageView, RefuelEditView, RefuelDeleteView,
    RefuelAddView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("<int:pk>/delete/", RefuelEditView.as_view(), name="refuel_edit"),
    path("<int:pk>/edit_ref/", RefuelDeleteView.as_view(), name="upt_delete"),
    path("add_refuel/", RefuelAddView.as_view(), name="refuel_add"),
]
