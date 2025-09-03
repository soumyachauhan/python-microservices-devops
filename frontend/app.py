from flask import Flask, render_template
import requests

app = Flask(__name__)

# Backend API URL (can be set via ENV VAR in Compose)
BACKEND_URL = "http://backend:5001/api/data"

@app.route("/")
def index():
    try:
        response = requests.get(BACKEND_URL, timeout=3)
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)