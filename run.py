from app import create_app
import webbrowser
from threading import Timer

app = create_app()

# Open the app in a web browser
def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)
