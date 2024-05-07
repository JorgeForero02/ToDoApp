import pytest  # type: ignore
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse("prueba:index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_tareaJson_view():
    client = Client()
    response = client.get(reverse("prueba:tareasJson"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_tareaJson_orderList():
    client = Client()
    response = client.get(reverse("prueba:tareasJson"))

    #assert response.status_code == 200
    data = response.json()
    latest_task_list = data["latest_task_list"]

    prioridades = [tarea["priority"] for tarea in latest_task_list]
    assert prioridades == sorted(prioridades, reverse=True)

@pytest.mark.django_db
def test_tareaDetailJson_view():
    client = Client()
    tarea_id = 1
    response = client.get(reverse("prueba:tareaDetail", kwargs={"tarea_id": tarea_id}))
    assert response.status_code == 200



