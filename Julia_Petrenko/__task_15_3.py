# Есть следующий код:
#
# import time
#
#
# def data_collection():
#     result = []
#     # Имитируем чтение больших данных из файла
#     print("[Читаем из файла]")
#     time.sleep(10)
#     result.append("Data from file")
#     # Имитируем запрос на сервер
#     print("[Получаем данные из https://data_online.com]")
#     time.sleep(10)
#     result.append("Data from data server")
#     # Имитируем запрос в базу данных
#     print("[Запрашиваем данные из базы users_db]")
#     time.sleep(10)
#     result.append("Data about user from database")
#
#     return result
#
#
# def main():
#     data = data_collection()
#
#     print(f"Result is: {data}")
#
#
# if __name__ == "__main__":
#     main()
#
# Каким образом мы можем ускорить процесс получения данных из разных источников?
# Напишите свою реализацию кода в качестве решения задачи


import time
import asyncio

# result = []

# def data_collection():
#     result = []
#     # Имитируем чтение больших данных из файла
#     print("[Читаем из файла]")
#     time.sleep(10)
#     result.append("Data from file")
#     # Имитируем запрос на сервер
#     print("[Получаем данные из https://data_online.com]")
#     time.sleep(10)
#     result.append("Data from data server")
#     # Имитируем запрос в базу данных
#     print("[Запрашиваем данные из базы users_db]")
#     time.sleep(10)
#     result.append("Data about user from database")
#
#     return result


async def read_file():
    file_result = []
    # Имитируем чтение больших данных из файла
    print("[Читаем из файла]")
    await asyncio.sleep(5)
    file_result.append("Data from file")

    return file_result


async def get_url_data():
    url_result = []
    # Имитируем запрос на сервер
    print("[Получаем данные из https://data_online.com]")
    await asyncio.sleep(5)
    url_result.append("Data from data server")

    return url_result


async def get_data_from_db():
    db_result = []
    # Имитируем запрос в базу данных
    print("[Запрашиваем данные из базы users_db]")
    await asyncio.sleep(5)
    db_result.append("Data about user from database")

    return db_result


async def main():
    # data = data_collection()

    task1 = asyncio.create_task(read_file())
    task2 = asyncio.create_task(get_url_data())
    task3 = asyncio.create_task(get_data_from_db())

    res1 = await task1
    res2 = await task2
    res3 = await task3

    data = []
    data.extend(res1)
    data.extend(res2)
    data.extend(res3)

    print(f"Result is: {data}")

print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))

