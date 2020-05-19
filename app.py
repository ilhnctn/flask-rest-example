import logging
from os import environ as os_environ
from sys import setrecursionlimit

from flask import Flask

from apps.fibonacci.views import fib_bp
from apps.factorial.view import FactorialView
from apps.acckerman.views import AcckermanView

setrecursionlimit(os_environ.get("MAX_RECURSION_LIMIT", 3000))

app = Flask(__name__)
app.register_blueprint(blueprint=fib_bp)

app.add_url_rule('/api/v1/factorial',
                 view_func=FactorialView.as_view('factorial'))

app.add_url_rule('/api/v1/acckerman',
                 view_func=AcckermanView.as_view('acckerman'))

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
