def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, '='))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title('Редактированние данних католога фильмов')
    def user_answer(self):
        print("Действия с фильмами: ")
        print(
            "1 - добавление филма\n2 - каталог фильма\n3 - прасмотр определинного филма\n4 - удалиние фильма\nq - выход из программы")
        user_naswer = input('Вибирите вариант действия: ')
        return user_naswer

    @add_title('Создания филм')
    def add_film(self):
        dict_film = {
            'названия фильма': None,
            'режиссер': None,
            'год випуска': None,
            'студия': None,
            'актеры': None,

        }
        for key in dict_film:
            dict_film[key] = input(f"ввидите {key}: ")
        return dict_film

    @add_title('Каталог фильма')
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    @add_title('Ввод названия филм')
    def get_user_film(self):
        film_name = input('Ввидите название филм: ')
        return film_name

    @add_title('Прасмотр филм')
    def show_single_film(self, film):
        for key in film:
            print(f'{key} филм  - {film[key]}')

    @add_title('Собщения об ошибке ')
    def show_encorrect_name_error(self, film_name):
        print(f"Филм с названием {film_name} не сушествует")

    @add_title("Удалина филм")
    def remove_single_film(self,film):
        print(f"Филм {film} - была удалин")

    @add_title('Собщения об ошибке ')
    def show_incorrect_answer_error(self, answer):
        print(f"вариант {answer} не сушествует")

