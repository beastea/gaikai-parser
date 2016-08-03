import pytest
import gaikai_app

@pytest.fixture
def app():
    return gaikai_app.app

@pytest.fixture
def test_client(app):
    return app.test_client()

def test_root_route(test_client):
    response = test_client.get('/')
    assert response.status_code == 302
    assert 'Redirecting...' in response.data
    assert 'You should be redirected automatically to target URL' in response.data

def test_root_route_follow(test_client):
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.data == test_client.get('/games').data
    assert not response.data == None

def test_games_route(test_client):
    response = test_client.get('/games')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert not response.data == None
    assert 'title' in response.data
    assert 'score' in response.data

def test_game_name(test_client):
    response = test_client.get('/games/The Awakened Fate: Ultimatum')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert not response.data == None
    assert 'The Awakened Fate: Ultimatum' in response.data

def test_404(test_client):
    response = test_client.get('/404')
    assert response.status_code == 400
