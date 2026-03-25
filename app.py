from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from your real-world Docker container!"

if __name__ == "__main__":
    # host=0.0.0.0 allows access from outside container
    # port=8080 is what we’ll expose in Docker
    app.run(host='0.0.0.0', port=8080)
