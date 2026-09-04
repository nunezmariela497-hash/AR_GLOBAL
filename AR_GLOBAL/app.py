import webbrowser
from threading import Timer

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000/")


if __name__ == "__main__":
    Timer(1, abrir_navegador).start()

    app.run(
        debug=False,
        host="0.0.0.0",
        port=5000
    )
