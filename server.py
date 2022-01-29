from surveys_app import app
from surveys_app.controllers import surveysController

if __name__ == '__main__':
    app.run( debug = True, port = 8091 )