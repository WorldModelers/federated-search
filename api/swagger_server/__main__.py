import connexion

from swagger_server import encoder

from flask_cors import CORS

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'World Modelers Federated Search API'}, pythonic_params=True)
    cors = CORS(app.app, supports_credentials=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
