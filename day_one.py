import requests

API_URL = "https://api.github.com/search/repositories"

def create_query(languages):
    query = "stars:>50000 "
    for language in languages:
        query += f"language:{language} "
    return query


def repos_with_most_stars(languages):
    params = {
        "q": create_query(languages),
        "sort": "stars",
        "order": "desc"
    }
    print(params)
    response = requests.get(API_URL, params=params)
    status_code = response.status_code
    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again")
    if status_code != 200:
        raise RuntimeError(f"Unexpected HTTP Status Code: {status_code}")

    response_json = response.json()

    return response_json["items"]

if __name__ == "__main__":
    repos = repos_with_most_stars(["go", "rust"])

    for repo in repos:
        language = repo["language"]
        stars = repo["stargazers_count"]
        name = repo["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
