from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delete/<int:id>/", views.delete_note, name="delete_note"),
    path("edit/<int:id>/", views.edit_note, name="edit_note"),
    path(
    "extract/<int:id>/",
    views.extract_action_items,
    name="extract_action_items",
)
]