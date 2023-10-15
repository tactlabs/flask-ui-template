
from flask import Flask
from rest_api import *

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":

    host = '0.0.0.0'
    port = PORT_NO

    app.run(
        host            = host, 
        port            = port, 
        debug           = True,
        use_reloader    = False
    )