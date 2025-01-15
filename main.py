from flask import Flask, jsonify, request, make_response
from bd import carros 


# foi feita a importação.


app =  Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def getCarros():
    return make_response (jsonify(carros), 200)


@app.route('/carros', methods=['POST'])
def createCar():
    Car = request.json
    carros.append(Car)
    return make_response (
        jsonify(
            Mensagem= 'Carro criado com sucesso',
            Carro=Car
        )
    )

app.run()


