from flask import Flask, jsonify, request, json

server_port = 5000
app = Flask(__name__)
app.config["DEBUG"] = True

users = [
    {'name': 'John', 'email': 'john@gmail.com', 'salary': 1000}
]


@app.route('/')
def get_usere():
    return users[0]


@app.route('/users')
def get_user():
    return jsonify({'users': users})


@app.route('/users', methods=['POST'])
def add_user():
    usr = request.get_json()
    for u in users:
        if usr['email'] == u['email']:
            return f'{usr["email"]} taken', 200
    else:
        users.append(request.get_json())
        return '', 201


@app.route('/users', methods=['DELETE'])
def delete_user():
    for u in users:
        print(u['email'])
        if request.get_json()['email'] == u['email']:
            users.remove(u)
    return 'email deleted', 410


@app.route('/users', methods=['PUT'])
def update_user():
    req = request.get_json()
    print(f'user input {req}')
    print('List of users ', users)
    for u in users:
        if req['email'] == u['email']:
            u['salary'] = req['salary']
            return 'put', 201
        else:
            return 'put', 200


if __name__ == '__main__':
    app.run('localhost', port=server_port, debug=True)
