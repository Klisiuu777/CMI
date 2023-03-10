# Importowanie klasy Flask
from flask import Flask

# Utworzenie instancji klasy Flask
app = Flask(__name__)

# Definiowanie funkcji obsługującej żądanie GET na adresie głównym
@app.route("/")
def hello():
    return "Hello, World!"

# Uruchomienie serwera na porcie 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)