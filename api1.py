from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/username', methods=['POST'])
def post_username():
    data = request.get_json()
    username = data.get('username')
    response = {'message': 'Username received', 'username': username}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
