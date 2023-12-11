# routes.py
from flask import Flask, jsonify, request
from flask_redis import FlaskRedis

from src.models import Item, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@127.0.0.1:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Configuração do Redis
app.config['REDIS_URL'] = "redis://localhost:6379/0"  # Atualize com as informações corretas do seu servidor Redis
redis_store = FlaskRedis(app)


# Rota para obter todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    # Tentar obter dados do cache do Redis
    items_data = redis_store.get('all_items')
    if items_data:
        # Se os dados estiverem no cache, retornar diretamente do cache
        items = items_data.decode('utf-8')
        return items, 200, {'Content-Type': 'application/json'}

    # Se os dados não estiverem no cache, consultar o banco de dados
    items = Item.query.all()
    result = [{'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price, 'email': item.email} for item in items]

    # Armazenar dados no cache do Redis por 60 segundos (ou o tempo desejado)
    redis_store.setex('all_items', 60, jsonify(result).data)

    return jsonify(result)

# Rota para obter detalhes de um item específico
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Tentar obter dados do cache do Redis
    item_data = redis_store.get(f'item_{item_id}')
    if item_data:
        # Se os dados estiverem no cache, retornar diretamente do cache
        item = item_data.decode('utf-8')
        return item, 200, {'Content-Type': 'application/json'}

    # Se os dados não estiverem no cache, consultar o banco de dados
    item = Item.query.get_or_404(item_id)
    result = {'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price, 'email': item.email}

    # Armazenar dados no cache do Redis por 60 segundos (ou o tempo desejado)
    redis_store.setex(f'item_{item_id}', 60, jsonify(result).data)

    return jsonify(result)

@app.route('/items', methods=['POST'])  # Adicione este bloco para aceitar POST
def create_item():
    data = request.json
    new_item = Item(name=data['name'], description=data['description'], price=data['price'], email=data['email'])
    db.session.add(new_item)
    db.session.commit()

    # Limpar o cache do Redis após adicionar um novo item
    redis_store.delete('all_items')

    return jsonify({'id': new_item.id}), 201
