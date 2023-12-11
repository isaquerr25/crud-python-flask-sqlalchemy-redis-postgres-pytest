import pytest

from src.models import Item, db
from src.routes import app

db_initialized = False

@pytest.fixture(scope='session', autouse=True)
def client():
    global db_initialized
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'
    
    with app.app_context():
        if not db_initialized:
            db.init_app(app)
            db.create_all()
            db_initialized = True

    with app.test_client() as client:
        yield client
   
    with app.app_context():
        db.drop_all()
        
        
def test_create_item(client):
    response = client.post('/items', json={'name': 'Test Item', 'description': 'Test Description', 'price': 19.99, 'email': 'test@example.com'})
    assert response.status_code == 201
    assert 'id' in response.json

def test_get_items(client):
    # Remova a criação de itens aqui

    response = client.get('/items')
    assert response.status_code == 200
    assert len(response.json) == 1  # Agora espera apenas 1 item

def test_get_item(client):
    # Criar um item para testar a obtenção
    create_response = client.post('/items', json={'name': 'Single Item', 'description': 'Single Description', 'price': 25.99, 'email': 'single@example.com'})
    item_id = create_response.json['id']

    response = client.get(f'/items/{item_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Single Item'
    assert response.json['description'] == 'Single Description'
    assert response.json['price'] == 25.99
    assert response.json['email'] == 'single@example.com'