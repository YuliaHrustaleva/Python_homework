import os
import uuid
import pytest
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

BASE_URL = os.getenv("YOUGILE_BASE_URL")
TOKEN = os.getenv("YOUGILE_TOKEN")


if not all([BASE_URL, TOKEN]):
    raise RuntimeError("Не хватает переменных окружения. Проверьте .env")


# фикстура для заголовка с авторизацией
@pytest.fixture(scope="session")
def api_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }


@pytest.fixture
def project_id(api_headers):
    resp = requests.post(
        url=f"{BASE_URL}/projects",
        headers=api_headers,
        json={"title": f"Проект_{uuid.uuid4().hex[:6]}"})
    assert resp.status_code == 201
    pid = resp.json()["id"]
    yield pid
    requests.put(
        url=f"{BASE_URL}/projects/{pid}",
        headers=api_headers,
        json={"deleted": True})


# Позитивный тест: создание проекта с валидными данными.
# Генерируем уникальный ключ и название
def test_positive_create_project(api_headers):
    unique_title = f"Проект_Тест_{uuid.uuid4().hex[:8]}"
    payload = {
        "title": unique_title,
        "users": {},
        "departments": {},
        "idempotencyKey": str(uuid.uuid4()),
    }
    resp = requests.post(
        url=f"{BASE_URL}/projects",
        headers=api_headers,
        json=payload,
    )
    assert resp.status_code == 201, f"Ожидался 201, получен {resp.status_code}"
    data = resp.json()
    assert data.get("id") is not None
    print(unique_title)

    # Удаление созданного проекта
    created_id = data["id"]
    requests.put(
        f"{BASE_URL}/projects/{created_id}",
        headers=api_headers,
        json={"deleted": True}
    )


# Негативный тест: создание проекта без обязательного поля title.
# Генерируем уникальный ключ
def test_negative_create_project_not_title(api_headers):
    payload = {
        "idempotencyKey": str(uuid.uuid4()),
    }
    resp = requests.post(
        url=f"{BASE_URL}/projects",
        headers=api_headers,
        json=payload,
    )
    assert resp.status_code == 400, (f"Ожидалась ошибка 400, "
                                     f"получен статус {resp.status_code}")

    error_body = resp.json()

    error_text = str(error_body).lower()
    assert "title" in error_text, \
        "В ответе об ошибке не упоминается поле title"
    assert ("required" in error_text or "обязательное" in error_text
            ), "В ответе нет указания, что поле обязательно"


# Позитивный тест: изменение проекта с валидным id.
def test_positive_change_project(api_headers, project_id):
    new_title = f"Тестовый проект_{uuid.uuid4().hex[:6]}"
    payload = {"title": new_title, "deleted": False}
    resp = requests.put(
        url=f"{BASE_URL}/projects/{project_id}",
        headers=api_headers, json=payload,
    )
    assert resp.status_code == 200, f"Ожидался 200, получен {resp.status_code}"

    # Проверка, что title изменился
    get_resp = requests.get(
        url=f"{BASE_URL}/projects/{project_id}",
        headers=api_headers
    )
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["title"] == new_title
    assert data["id"] == project_id
    print(data)


# Негативный тест: попытка изменить проект с невалидным id
def test_negative_change_project_invalid_id(api_headers):
    invalid_id = uuid.uuid4().hex[:8]
    payload = {"title": "Тестовый проект", "deleted": False}
    resp = requests.put(
        url=f"{BASE_URL}/projects/{invalid_id}",
        json=payload,
        headers=api_headers,
    )
    assert resp.status_code == 404, f"Ожидался 404, получен {resp.status_code}"

    error_body = resp.json()

    error_text = str(error_body).lower()
    assert (
        "not found" in error_text or "не найден" in error_text
        or "not exist" in error_text
    ), "В ответе нет сообщения о том, что ресурс не найден"


# Позитивный тест: получение проекта по валидному id
def test_positive_get_project_id(api_headers, project_id):
    resp = requests.get(
        url=f"{BASE_URL}/projects/{project_id}",
        headers=api_headers)
    assert resp.status_code == 200, f"Ожидался 200, получен {resp.status_code}"
    data = resp.json()
    assert data["id"] == project_id
    assert data.get("title") is not None
    print(data)


# Негативный тест: запрос без указания ключа авторизации
def test_negative_get_project_unauthorized(project_id):
    headers = {
        "Content-Type": "application/json",
        # намеренно пустой или некорректный токен
        "Authorization": "Bearer invalid_token",
    }
    resp = requests.get(
        url=f"{BASE_URL}/projects/{project_id}",
        headers=headers,
    )
    assert resp.status_code == 401, f"Ожидался 401, получен {resp.status_code}"
    error_body = resp.json()
    error_text = str(error_body).lower()
    assert (
        "unauthorized" in error_text or "не авторизован"
        in error_text or "invalid token" in error_text
    ), "В ответе нет сообщения об ошибке авторизации"
