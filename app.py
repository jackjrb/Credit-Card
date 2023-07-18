# import mysql.connector
from flask import Flask, jsonify, request

credit_cards = [
        {
            "card_number": "5436575218035610",
            "cvv": "593",
            "exp_date": "2025-06-30",
            "holder": "Jackeline Brito",
            "id": 1
        },
        {
            "card_number": "5493787031323780",
            "cvv": "269",
            "exp_date": "2025-02-28",
            "holder": "Ana Joana",
            "id": 2
        },
        {
            "card_number": "5164300972138585",
            "cvv": "472",
            "exp_date": "2024-07-31",
            "holder": "Flavio Coelho",
            "id": 3
        }
]

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# Consultar (todos)
@app.route('/api/v1/credit-card', methods=['GET'])
def get_all_credit_cards():
    return jsonify(credit_cards)
# Consultar(id)
@app.route('/api/v1/credit-card/<int:id>', methods=['GET'])
def get_credit_card(id):
    for credit_card in credit_cards:
        if credit_card.get('id') == id:
            return jsonify(credit_card)
# Editar(id)
@app.route('/api/v1/credit-card/<int:id>', methods=['PUT'])
def edit_credit_card(id):
    new_credit_card = request.get_json()
    for index,credit_card in enumerate(credit_cards):
        if credit_card.get('id') == id:
            credit_cards[index].update(new_credit_card)
            return jsonify(
                message='Cartão editado com sucesso.',
                credit_card=credit_cards[index]
                )
# Criar
@app.route('/api/v1/credit-card', methods=['POST'])
def incluir_novo_livro():
    new_credit_card = request.get_json()
    credit_cards.append(new_credit_card)
    return jsonify(
        message='Cartão cadastrado com sucesso.',
        credit_cards = credit_cards
        )
# Excluir(id)
@app.route('/api/v1/credit-card/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for index,credit_card in enumerate(credit_cards):
        if credit_card.get('id') == id:
            del credit_cards[index]
    return jsonify(
        message='Cartão excluido com sucesso.',
        credit_cards = credit_cards
        )
            
    


app.run(port=5000, host='localhost',debug=True)

