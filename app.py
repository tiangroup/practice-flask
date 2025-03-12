from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    test_var = os.getenv('TEST_VAR', 'Переменная не задана.')
    return f'<h2>{test_var}</h2>'


if __name__ == '__main__':
    app.run()
