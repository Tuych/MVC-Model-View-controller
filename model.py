import pickle
import os.path


class Film:
    def __init__(self, name, director, year, study, actor):
        self.name = name
        self.director = director
        self.year = year
        self.study = study
        self.actor = actor

    def __str__(self):
        return f"{self.name} ({self.year})"


class FilmModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.films = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())   # *dict_film.values() listdan har bit valueni olib beradi
        self.films[film.name] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, film_name):
        film = self.films[film_name]
        dict_film = {
            'названия фильма': film.name,
            'режиссер': film.director,
            'год випуска': film.year,
            'студия': film.study,
            'актеры': film.actor,

        }
        return dict_film

    def remove_film(self, film_name):
        return self.films.pop(film_name)

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()