import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def check(name, condition):
    if not condition:
        raise AssertionError(f"FAILED: {name}")
    print(f"PASS: {name}")


def test_get_post():
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=TIMEOUT
    )

    check("GET post status 200", response.status_code == 200)
    check("post id is 1", response.json().get("id") == 1)


def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=TIMEOUT
    )

    check("GET user status 200", response.status_code == 200)
    check("email exists", "email" in response.json())


def test_create_post():
    payload = {
        "title": "QA practice",
        "body": "Python API testing exercise",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=TIMEOUT
    )

    check("POST status 201", response.status_code == 201)
    check(
        "response title matches",
        response.json().get("title") == payload["title"]
    )


def test_missing_post():
    response = requests.get(
        f"{BASE_URL}/posts/999999",
        timeout=TIMEOUT
    )

    check("missing post returns 404", response.status_code == 404)


if __name__ == "__main__":
    test_get_post()
    test_get_user()
    test_create_post()
    test_missing_post()
    print("\nAPI practice checks completed.")
