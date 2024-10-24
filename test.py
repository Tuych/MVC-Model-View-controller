class Film:
    def __init__(self, name, director, actor, year, ):
        self.name = name
        self.director = director
        self.actor = actor
        self.year = year

    def __str__(self):
        return self.name

    def add_film(self, dict_film):
        films = Film(dict_film.values())
        print(films)

x = {'name': 'Troya', 'director': 'hhhh', 'actor': 'Brit Pit', 'year': '2004'}
print(*x.values())