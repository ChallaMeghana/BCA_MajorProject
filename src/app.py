from flask import Flask, jsonify

app = Flask(__name__)

# Welcome page route
@app.route('/')
def welcome():
    return "<h1>Welcome to My Application</h1>"

# Health check route
@app.route('/health')
def health():
    return jsonify(status="UP")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

