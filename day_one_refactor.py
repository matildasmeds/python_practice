import requests
import sys

# Introducing classes and custom exceptions

API_URL = "https://api.github.com/search/repositories"


class Repository():
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.language = kwargs.get("language", None)
        self.stars = kwargs.get("stars", None)

    def __str__(self):
        return f"{self.name} is a {self.language} repo with {self.stars} stars."


class ApiException(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again"
        else:
            message = f"Unexpected HTTP Status Code: {status_code}"
        super().__init__(message)


class Github():
    @staticmethod
    def create_query(languages):
        query = "stars:>50000 "
        for language in languages:
            query += f"language:{language} "
        return query


    @staticmethod
    def repos_with_most_stars(languages):
        params = {
            "q": Github.create_query(languages),
            "sort": "stars",
            "order": "desc"
        }
        print(params)
        response = requests.get(API_URL, params=params)
        status_code = response.status_code
        if status_code != 200:
            raise ApiException(status_code)

        response_json = response.json()
        repos = [
            Repository(
                name=repo["name"],
                language=repo["language"],
                stars=repo["stargazers_count"]
            ) for repo in response_json["items"]
        ]
        return repos

if __name__ == "__main__":
    arguments = sys.argv
    languages = ["python"]  # set some default
    if len(arguments) > 1:
        languages = arguments[1:]
    repos = Github.repos_with_most_stars(languages)
    for repo in repos:
        print(f"-> {repo}")
