import requests
import json


def call_get_method():
    print('\n <<<<< Get method started >>>>> \n')
    url = "http://localhost:5000/users"

    payload = {}
    headers = {}

    # response = requests.request("GET", url, headers=headers, data=payload)
    response = requests.get(url, headers=headers, data=payload)
    print(response.headers, response.json(), sep='\n')
    return response.json(), response.status_code


def call_post_method(name, email, salary):
    print('\n <<<<< Post method started >>>>> \n')
    url = "http://localhost:5000/users"

    payload = json.dumps({
        "name": name,
        "email": email,
        "salary": salary
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept-Language': 'en-EN'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f'Post method test')
    print(response.text)
    print(response.status_code)
    return response.status_code


def call_delete_method(name, email, salary):
    print('\n <<<<< Delete method started >>>>> \n')
    url = "http://localhost:5000/users"

    payload = json.dumps({
        "email": email,
        "name": name,
        "salary": salary
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)
    return response.status_code


def call_put_method(name, email, salary):
    print('\n <<<<< Put method started >>>>> \n')
    url = "http://localhost:5000/users"

    payload = json.dumps({
        "email": name,
        "name": email,
        "salary": salary
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

    return response.status_code


# {'users': [{'email': 'john@gmail.com', 'name': 'John', 'salary': 1000}]}
x = call_get_method()
print()

# call_post_method('Paulaner', 'paaul@gmail.com', 1000)
# call_get_method()
# call_delete_method('John', 'john@gmail.com', 1000)
# call_get_method()
# call_post_method('Paulaner', 'paaul@gmail.com', 1000)
# call_get_method()
# call_put_method('john@gmail.com', 'john@gmail.com', 5)
# call_get_method()
