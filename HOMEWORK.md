# Тема 15 Потоки. Асинхронность

### Задача 1
Есть следующий код:
```python



file_name = input("Имя файла: ") + ".txt"

file_data = []

print("[Начало записи]")
while True:
    line = input(">>> ")

    if (line.strip().lower()) == "#end":
        break

    file_data.append(line)

print("[Запись завершена]")

with open(file_name, "w") as file:
    text = "\n".join(file_data)
    file.write(text)

print(f"[Сохранено в файл {file_name}]")

```

Создайте поток, который будет раз в 5 (или другое значение) секунд записывать данные из списка file_data в файл, к названию которого добавлено "_autosave". В конце работы программы удалить файл резервной копии. 

\* Учтите, что программа может завершится преждевременно, в таком должен быть создан файл с указанным именем и в него должны быть записаны данные из резервного файла. Резервный файл удалить


### Задача 2
Есть следующий код:
```python
import random
import time

some_titles = [
    "Cool title",
    "Generic title",
    "Boring title"
]

some_descriptions = [
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAWESOME",
    "IAMMMMMMMMMMMBOREDSOMETIMES",
    "HOMEWORKISMOREFUNWHENITLIKETHIS"
]

def get_data(url):
    time.sleep(5)
    return {
        "source": url,
        "title": random.choice(some_titles),
        "content": random.choice(some_descriptions)
    }


def main():
    print("Startin data collection")
    a1 = get_data("https://articles.com")
    a2 = get_data("https://sport-news.net")
    a3 = get_data("https://you-know-what.dev")

    # If you want you can save this data to file



if __name__ == "__main__":
    main()

```
Переработайте его, используя асинхронный подход. Вы можете использовать `asyncio.create_task()` или `asyncio.gather()` по вашему усмотрению.

### Задача 3

Есть следующий код:
```python
import time


def data_collection():
    result = []
    # Имитируем чтение больших данных из файла
    print("[Читаем из файла]")
    time.sleep(10)
    result.append("Data from file")
    # Имитируем запрос на сервер
    print("[Получаем данные из https://data_online.com]")
    time.sleep(10)
    result.append("Data from data server")
    # Имитируем запрос в базу данных
    print("[Запрашиваем данные из базы users_db]")
    time.sleep(10)
    result.append("Data about user from database")

    return result
    

def main():
    data = data_collection()

    print(f"Result is: {data}")


if __name__ == "__main__":
    main()

```

Каки образом мы можем ускорить процесс получения данных из разных источников? Напишите свою реализацию кода в качестве решения задачи
