from api import create_app

mi_app = create_app()

if __name__ == "__main__":
    mi_app.run(debug=True)