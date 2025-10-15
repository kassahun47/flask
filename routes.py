from flask import jsonify

def register_routes(app):
    @app.route('/')
    def ping():
        return jsonify({'status': 'pong'})
