from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("detail/<int:course_id>/", views.detail, name="detail"),
    path("edit/<int:course_id>/", views.edit, name="edit"),
    path("remove/<int:course_id>/", views.remove, name="remove"),

]