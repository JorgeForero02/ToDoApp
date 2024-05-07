from django.urls import path

from . import views

app_name = "prueba"
urlpatterns = [
    path("", views.index, name="index"),
    path("tasksJson/", views.tareaJson, name="tareasJson"),
    path("tasksJson/<int:tarea_id>/", views.tareaDetailJson, name="tareaDetailJson"),
    path("usersJson/", views.usersJson, name="usersJson"),
    path("usersJson/<int:user_id>/", views.userDetailJson, name="usersDetailJson"),
    # --------------------------------------------------------
    path("tasks/", views.tarea, name="tareas"),
    path("tasks/<int:tarea_id>/", views.tareaDetail, name="tareaDetail"),
    path("users/", views.users, name="users"),
    path("users/<int:user_id>/", views.userDetail, name="userDetail"),
]
