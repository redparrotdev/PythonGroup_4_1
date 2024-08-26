# Есть следующий код:
#
# import random
# import time
#
# some_titles = [
#     "Cool title",
#     "Generic title",
#     "Boring title"
# ]
#
# some_descriptions = [
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAWESOME",
#     "IAMMMMMMMMMMMBOREDSOMETIMES",
#     "HOMEWORKISMOREFUNWHENITLIKETHIS"
# ]
#
# def get_data(url):
#     time.sleep(5)
#     return {
#         "source": url,
#         "title": random.choice(some_titles),
#         "content": random.choice(some_descriptions)
#     }
#
#
# def main():
#     print("Startin data collection")
#     a1 = get_data("https://articles.com")
#     a2 = get_data("https://sport-news.net")
#     a3 = get_data("https://you-know-what.dev")
#
#     # If you want you can save this data to file
#
#
#
# if __name__ == "__main__":
#     main()
#
# Переработайте его, используя асинхронный подход.
#  Вы можете использовать asyncio.create_task() или asyncio.gather() по вашему усмотрению.

import random
import time
import asyncio

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


async def get_data(url):
    await asyncio.sleep(5)
    source = url
    title = random.choice(some_titles)
    content = random.choice(some_descriptions)

    with open("__task_15_2.txt", "a") as file:
        file.write(f"source: {source}, title: {title}, content: {content}\n")

    return {
        "source": source,
        "title": title,
        "content": content
    }


async def main():
    print("Startin data collection")
    task1 = asyncio.create_task(get_data("https://articles.com"))
    task2 = asyncio.create_task(get_data("https://sport-news.net"))
    task3 = asyncio.create_task(get_data("https://you-know-what.dev"))

    await task1
    await task2
    await task3

    # If you want you can save this data to file


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))
