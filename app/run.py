from core import create_app
from controllers.actor import add_actor
app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8000)
    