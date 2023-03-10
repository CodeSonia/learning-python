def sorter(item):
    return item["title"]

movies = [
    {"title": "Twilight", "rating": 13},
    {"title": "Mean Girls", "rating": 12},
    {"title": "Jaws", "rating": 15}
]

movies.sort(key=sorter)
print(movies)

movies.sort(key=lambda item: item["rating"])
print(movies)


def my_func(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=my_func)
print(cars)
