from flask import Flask, jsonify, request

app = Flask(__name__)

game_state = {
    'spheres': [],
    'territory': 0,
    'reset_count': 0
}

@app.route('/build_sphere', methods=['POST'])
def build_sphere():
    data = request.json
    if 'name' in data:
        game_state['spheres'].append(data['name'])
        return jsonify({'message': 'Sphere created', 'spheres': game_state['spheres']}), 201
    return jsonify({'message': 'Sphere name required'}), 400

@app.route('/expand_territory', methods=['POST'])
def expand_territory():
    game_state['territory'] += 1
    return jsonify({'message': 'Territory expanded', 'territory': game_state['territory']}), 200

@app.route('/reset_game', methods=['POST'])
def reset_game():
    game_state['spheres'] = []
    game_state['territory'] = 0
    game_state['reset_count'] += 1
    return jsonify({'message': 'Game reset', 'reset_count': game_state['reset_count']}), 200

if __name__ == '__main__':
    app.run(debug=True)