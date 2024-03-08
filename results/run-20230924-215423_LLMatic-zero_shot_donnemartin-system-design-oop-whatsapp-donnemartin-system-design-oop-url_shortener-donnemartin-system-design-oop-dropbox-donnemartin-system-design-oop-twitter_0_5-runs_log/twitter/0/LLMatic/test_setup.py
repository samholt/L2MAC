import sys
sys.path.append('.')

import pytest
import flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate

def test_imports():
	assert flask
	assert SQLAlchemy
	assert flask_migrate
