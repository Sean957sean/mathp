from flask import Flask, send_from_directory

# Flask application instance
app = Flask(__name__)

# Route to serve the HTML file
@app.route("/")
def serve_html():
    return send_from_directory(".", "people_info_webpage.html")

# Main function to run the server
if __name__ == "__main__":
    app.run(debug=True, port=8000)
