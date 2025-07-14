from Blueprints.app import create_app

flas_app = create_app()

if __name__ == '__name__':
    flas_app.run(host='0.0.0.0', debug=True) 



