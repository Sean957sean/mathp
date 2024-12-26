from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "people_info_webpage.html")

if __name__ == "__main__":
    # Render에서 제공하는 PORT 환경 변수를 사용
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
