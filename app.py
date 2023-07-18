import mysql.connector
from flask import Flask, jsonify, request

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'MyUser',
    password='MainPassword',
    database = 'MaisTodosTeste',
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# Consultar (todos)
@app.route('/api/v1/credit-card', methods=['GET'])
def get_all_credit_cards():
    
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM credit_cards')
    credit_cards_db = my_cursor.fetchall()
    
    credit_cards = list()
    for credit_card in credit_cards_db:
        credit_cards.append(
            {
                'id':credit_card[0],
                'exp_date': credit_card[1],
                'holder': credit_card[2],
                'card_number': credit_card[3],
                'cvv': credit_card[4]
            }
        )
    
    return jsonify(credit_cards=credit_cards)


# Consultar(id)
@app.route('/api/v1/credit-card/<int:id>', methods=['GET'])
def get_credit_card(id):
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM credit_cards WHERE id={}'.format(id))
    credit_cards_db = my_cursor.fetchall()
    credit_cards = list()
    for credit_card in credit_cards_db:
        credit_cards.append(
            {
                'id':credit_card[0],
                'exp_date': credit_card[1],
                'holder': credit_card[2],
                'card_number': credit_card[3],
                'cvv': credit_card[4]
            }
        )
    return jsonify(credit_card=credit_cards[0])


# Editar(id)
@app.route('/api/v1/credit-card/<int:id>', methods=['PUT'])
def edit_credit_card(id):
    new_credit_card = request.get_json()
    # my_cursor = mydb.cursor()
    # my_cursor.execute('UPDATE MaisTodosTeste.credit_cards SET {} WHERE id={}'.format(new_credit_card,id))
    # mydb.commit()
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
    
    my_cursor = mydb.cursor()
    sql = f"INSERT INTO MaisTodosTeste.credit_cards (exp_date, holder, card_number, cvv) VALUES ('{new_credit_card['exp_date']}','{new_credit_card['holder']}','{new_credit_card['card_number']}','{new_credit_card['cvv']}');"
    my_cursor.execute(sql)
    mydb.commit()

    
    return jsonify(
        message='Cartão cadastrado com sucesso.',
        credit_cards = new_credit_card
        )
    
    
# Excluir(id)
@app.route('/api/v1/credit-card/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    my_cursor = mydb.cursor()
    my_cursor.execute('DELETE FROM MaisTodosTeste.credit_cards WHERE id={}'.format(id))
    mydb.commit()
    return jsonify(
        message='Cartão excluido com sucesso.',
        )
            
    


app.run(port=5000, host='localhost',debug=True)
