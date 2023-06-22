from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route and its corresponding handler
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run()
