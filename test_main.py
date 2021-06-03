'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'YourJWTSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjM5NjYxNzIsIm5iZiI6MTYyMjc1NjU3MiwiZW1haWwiOiJwcmFkZWVwa3VtYXI5NHBAZ21haWwuY29tIn0.ZJA0bXbq4m78r-_biusQ2kmdChEFaNuV77aSnxp0uYo'
EMAIL = 'pradeepkumar94p@gmail.com'
PASSWORD = 'asifiwillgivemypasswordtoyou'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
