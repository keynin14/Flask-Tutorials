"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Routes_and_URLs.views
