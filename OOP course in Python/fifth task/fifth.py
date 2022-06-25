class Book:
    def __init__(self, title, author='None', language='None', genre='None', cover='None', pub_year='None'):
        self.__title = title
        self.__author = author
        self.__language = language
        self.__genre = genre
        self.__cover = cover
        self.__pub_year = pub_year

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_language(self, language):
        self.__language = language

    def get_language(self):
        return self.__language

    def set_genre(self, genre):
        self.__genre = genre

    def get_genre(self):
        return self.__genre

    def set_cover(self, cover):
        self.__cover = cover

    def get_cover(self):
        return self.__cover

    def set_pub_year(self, pub_year):
        self.__pub_year = int(pub_year)

    def get_pub_year(self):
        return self.__pub_year

    def __setattr__(self, attr, value):
        if attr in ['_Book__title', '_Book__author', '_Book__language', '_Book__genre', '_Book__cover']:
            if type(value) == str:
                self.__dict__[attr] = value
            else:
                raise TypeError
        elif attr == '_Book__pub_year':
            self.__dict__[attr] = value
        else:
            raise AttributeError


book = Book('Little women', 'Alcott Louisa May', 'eng', 'classical prose', 'softcover')
