import os
import uuid
import pytest
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

BASE_URL = os.getenv("YOUGILE_BASE_URL")
TOKEN = os.getenv("YOUGILE_TOKEN")
VALID_PROJECT_ID = os.getenv("YOUGILE_VALID_PROJECT_ID")
INVALID_PROJECT_ID = os.getenv("YOUGILE_INVALID_PROJECT_ID")


if not all([BASE_URL, TOKEN, VALID_PROJECT_ID, INVALID_PROJECT_ID]):
    raise RuntimeError("Не хватает переменных окружения. Проверьте .env")

# фикстура для заголовка с авторизацией
@pytest.fixture(scope="session")
def api_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

# Позитивный тест: создание проекта с валидными данными. Генерируем уникальный ключ и название
def test_positive_create_project(api_headers):
    unique_title = f"Проект_Тест_{uuid.uuid4().hex[:8]}"
    payload = {
        "title": unique_title,
        "users": {},
        "departments": {},
        "idempotencyKey": str(uuid.uuid4()),
    }
    resp = requests.post(
        f"{BASE_URL}/projects",
        headers=api_headers,
        json=payload,
    )
    assert resp.status_code == 201, f"Ожидался 201, получен {resp.status_code}. Ответ: {resp.text}"



# Негативный тест: создание проекта без обязательного поля title. Генерируем уникальный ключ
def test_negative_create_project_without_title(api_headers):
    payload = {
        "users": {},
        "departments": {},
        "idempotencyKey": str(uuid.uuid4()),
    }
    resp = requests.post(
        f"{BASE_URL}/projects",
        headers=api_headers,
        json=payload,
    )
    assert resp.status_code >= 400, f"Ожидалась ошибка, получен статус {resp.status_code}"


# Позитивный тест: изменение проекта с валидным id. Генерируем уникальное название
def test_positive_change_project(api_headers):
    payload = {"title": f"Тестовый проект_{uuid.uuid4().hex[:6]}", "deleted": False}
    resp = requests.put(
        f"{BASE_URL}/projects/{VALID_PROJECT_ID}",
        headers=api_headers,
        json=payload,
    )
    assert resp.status_code == 200, f"Ожидался 200, получен {resp.status_code}"


# Негативный тест: попытка изменить проект с невалидным id
def test_negative_change_project_invalid_id(api_headers):
    payload = {"title": "Тестовый проект", "deleted": False}
    resp = requests.put(
        f"{BASE_URL}/projects/{INVALID_PROJECT_ID}",
        headers=api_headers,
        json=payload,
    )
    assert resp.status_code == 404, f"Ожидался 404, получен {resp.status_code}"


# Позитивный тест: получение проекта по валидному id
def test_positive_get_project_id(api_headers):
    resp = requests.get(
        f"{BASE_URL}/projects/{VALID_PROJECT_ID}",
        headers=api_headers,
    )
    assert resp.status_code == 200, f"Ожидался 200, получен {resp.status_code}"

# Негативный тест: запрос без указания ключа авторизации
def test_negative_get_project_unauthorized():
    headers={
        "Content-Type": "application/json",
        # намеренно пустой или некорректный токен
        "Authorization": "Bearer invalid_token",
    }
    resp = requests.get(
        f"{BASE_URL}/projects/{VALID_PROJECT_ID}",
        headers=headers,
    )
    assert resp.status_code in (401, 403), f"Ожидался 401/403, получен {resp.status_code}"
