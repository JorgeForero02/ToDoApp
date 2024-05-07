from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Task, User


def index(request):
    return render(request, "index.html")


def tareaJson(request):
    latest_task_list = list(Task.objects.order_by("-id").values())
    return JsonResponse({"latest_task_list": latest_task_list})


# tareas_data = list(Task.objects.values())
# return JsonResponse(tareas_data, safe=False)


def tareaDetailJson(request, tarea_id):
    task = get_object_or_404(Task, pk=tarea_id)
    task_data = [
        {
            "id": task.id,
            "nombre": task.nombre,
            "descripcion": task.descripcion,
        }
    ]
    return JsonResponse(task_data, safe=False)

def usersJson(request):
    user_data = list(User.objects.values())
    return JsonResponse(user_data, safe=False)


def userDetailJson(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user_data = {
        "id": user.id,
        "nombre": user.user_name,
        "email": user.email,
    }
    return JsonResponse(user_data)


# -----------------------------------------------------------------


def tarea(request):
    latest_task_list = Task.objects.order_by("-fecha_realizar")[:5]
    context = {"latest_task_list": latest_task_list}
    return render(request, "task/tasks.html", context)


def tareaDetail(request, tarea_id):
    task = get_object_or_404(Task, pk=tarea_id)
    return render(request, "task/task_detail.html", {"task": task})


def users(request):
    user_list = User.objects.order_by("-id")
    context = {"user_list": user_list}
    return render(request, "user/users.html", context)


def userDetail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "user/user_detail.html", {"user": user})


# ------------------------------------------------------------------
