# 1 4 5 6 8

# Task 6
# from urllib import request, parse
# import json
# import requests
#
# url = "https://jsonplaceholder.typicode.com/posts"
# response = request.urlopen(url)
# data = response.read().decode()
# posts = json.loads(data)
# print(posts[:2])
#
# url = "https://jsonplaceholder.typicode.com/posts"
# data = parse.urlencode({"title": "My Post", "body": "This is a test", "userId": 1}).encode()
# req = request.Request(url, data=data, method="POST")
# req.add_header("Content-Type", "application/json")
# response = request.urlopen(req)
# print(response.read().decode())
#
# url = "https://jsonplaceholder.typicode.com/posts/1"
# data = parse.urlencode({"title": "Updated Title", "body": "Updated content", "userId": 1}).encode()
# req = request.Request(url, data=data, method="PUT")
# req.add_header("Content-Type", "application/json")
# response = request.urlopen(req)
# print(response.read().decode())
#
# url = "https://jsonplaceholder.typicode.com/posts/1"
# req = request.Request(url, method="DELETE")
# response = request.urlopen(req)
# print(f"Статус: {response.status}")
#
# ================================================

# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)
# print(response.status_code)
# print(response.json()[:2])
#
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {"title": "My Post", "body": "This is a test", "userId": 1}
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())
#
# url = "https://jsonplaceholder.typicode.com/posts/1"
# data = {"title": "Updated Title", "body": "Updated content", "userId": 1}
# response = requests.put(url, json=data)
# print(response.status_code)
# print(response.json())
#
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.delete(url)
# print(f"Статус: {response.status_code}")

# ================================================
# Task 8

import requests
import json

def http_client(url, method, data=None):
    try:
        method = method.upper()
        response = None


        if method == "GET":
            response = requests.get(url, params=data)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url, json=data)
        else:
            print(f"Метод {method} не підтримується.")
            return

        # Виведення результатів запиту
        print(f"Статус-код: {response.status_code}")
        print("Заголовки:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print("\nТіло відповіді:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Помилка при виконанні запиту: {e}")

# Приклад використання
if __name__ == "__main__":
    # Вхідні дані
    url = input("Введіть URL ресурсу: ").strip()
    method = input("Введіть метод (GET, POST, PUT, DELETE): ").strip()
    data_input = input("Введіть дані (у форматі JSON, опціонально) або залиште пустим: ").strip()

    data = None
    if data_input:
        try:
            data = json.loads(data_input)
        except json.JSONDecodeError:
            print("Помилка: Невірний формат JSON. Виконуємо запит без даних.")

    # Виконання HTTP-запиту
    http_client(url, method, data)
