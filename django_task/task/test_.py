import pytest # type: ignore
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
def test_tareaDetailJson_view():
    client = Client()
    tarea_id = int(1)
    response = client.get(reverse("prueba:tareaDetailJson", kwargs={"tarea_id": tarea_id}))
    assert response.status_code == 200

"""
@pytest.mark.django_db
def test_tareasvencidas():
        client = Client()
        all_tasks = Task.objects.all()
        for task in all_tasks:
                response = client.get(reverse('prueba:tareaDetailJson', args=(task.id,)))
                pytest.assertEqual(response.status_code, 200)
                pytest.assertFalse(task.was_published_recently)

@pytest.mark.django_db
def test_completed():
        client = Client()
        all_tasks = Task.objects.all()
        for task in all_tasks:
                response = client.get(reverse('prueba:tareaDetailJson', args=(task.id,)))
                assert response.status_code == 200
                assert task.completed
                assert "Completado" in response.content.decode()
# Create your tests here.
"""