from flask import Flask
import pytest

@pytest.fixture
def app():
  app = Flask(__name__)
  return app

def test_home_page(app):
  with app.test_client() as client:
    response = client.get('/')
    assert response.status_code == 200
