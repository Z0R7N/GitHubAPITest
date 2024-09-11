import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение данных из переменных окружения
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

# URL для работы с GitHub API
BASE_URL = "https://api.github.com"
REPO_URL = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_repository():
    """Создание репозитория на GitHub."""
    url = f"{BASE_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "private": False
    }
    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code == 201:
        print(f"Репозиторий '{REPO_NAME}' создан.")
    else:
        print(f"Ошибка при создании репозитория: {response.status_code}, {response.text}")

def check_repository_exists():
    """Проверка, существует ли репозиторий."""
    response = requests.get(REPO_URL, headers=HEADERS)
    if response.status_code == 200:
        print(f"Репозиторий '{REPO_NAME}' существует.")
        return True
    else:
        print(f"Репозиторий '{REPO_NAME}' не найден.")
        return False

def delete_repository():
    """Удаление репозитория на GitHub."""
    response = requests.delete(REPO_URL, headers=HEADERS)
    if response.status_code == 204:
        print(f"Репозиторий '{REPO_NAME}' удален.")
    else:
        print(f"Ошибка при удалении репозитория: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Создание репозитория
    create_repository()

    # Проверка существования репозитория
    if check_repository_exists():
        # Удаление репозитория
        delete_repository()
