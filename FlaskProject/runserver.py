"""
This script runs the FlaskProject application using a development server.
"""

from os import environ
from FlaskProject import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
