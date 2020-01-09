from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    print("Server Request Recieved")
    return "Welcome to my page!"

if __name__ == "__main__":
    app.run(debug=True)