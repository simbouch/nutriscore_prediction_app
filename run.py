# run.py
from app import create_app
import os

app = create_app()

def open_browser():
    if os.environ.get("FLASK_RUN_IN_DOCKER") != "1":
        import webbrowser
        from threading import Timer
        Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000/")).start()

if __name__ == "__main__":
    open_browser()
    # Lancer l'application sur toutes les interfaces
    app.run(host="0.0.0.0", port=5000, debug=True)
