from django.urls import path

from .views import(
    HomePageView, RefuelEditView, RefuelDeleteView, 
    MilageDeleteView, MilageEditView,
    RefuelAddView, MilageAddView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("<int:pk>/delete/", RefuelEditView.as_view(), name="refuel_edit"),
    path("<int:pk>/edit_ref/", RefuelDeleteView.as_view(), name="upt_delete"),
    path("<int:pk>/edit_mil/", MilageEditView.as_view(), name="milage_edit"),
    path("<int:pk>/delete/", MilageDeleteView.as_view(), name="upt_delete"),
    path("add_refuel/", RefuelAddView.as_view(), name="refuel_add"),
    path("update_milage/", MilageAddView.as_view(), name="milage_add"),
]
