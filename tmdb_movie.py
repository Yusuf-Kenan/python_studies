import json
import requests as re


class TheMovieDataBase ():
    def __init__(self):
        self.url = "https://api.themoviedb.org/3"
        self.headers = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNmMwZjc3YTA3MGVhMDM1MDYwYzQwMzdlNjI5ODY3MSIsInN1YiI6IjY1NTYxMjkzYjU0MDAyMTRkODJiYjVhOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LDvVQGHH4OPZgMxX9VD5HWdQxxs4jUrNT2wy5j5TgE8"
        }
        
    def getPopular(self):
        response = re.get(url = f"{self.url}/movie/popular?language=en-US&page=1", headers = self.headers)
        response=json.loads(response.text)
        count=1
        for movie in response["results"]:
            print(f"{count}=> ", "Movie name:", movie["title"])
            print("      Rate: ", movie["vote_average"], "/10\n")
            count+=1

    def getSearch(self, keyword):
        response = re.get(url = f"{self.url}/search/keyword?query={keyword}&page=1", headers = self.headers)
        response=json.loads(response.text)
        count=1
        for movie in response["results"]:
            print(f'{count}=> Movie name: {movie["name"]}')
            count+=1

theMovie = TheMovieDataBase()

while True:
    print("Welcome to The Movie App ".center(100))
    choice = input("1- Popular \n2- Playing \n0- Exit \n\n- Your Choice: ")

    if choice == "0":
        break
    elif choice == "1":
        theMovie.getPopular()
        
    elif choice == "2":
        keyword = input("keyword: ")
        theMovie.getSearch(keyword)
    else:
        print("Wrong choice please try again!!! ")

