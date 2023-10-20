from flask import Flask, request, jsonify

import util




app = Flask(__name__)

@app.route('/get_all_names', methods=['GET'])
def get_all_names():
    response = jsonify({
        'locations': util.get_all_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/get_estimated_rent', methods=['GET', 'POST'])
def get_estimated_rent():
    address = (request.form['address'])
    bedroom = (request.form['bedroom'])
    area = (request.form['area'])
    parking = (request.form['parking'])
    furnishing = (request.form['furnishing'])
    available_for = request.form['available_for']
    facing = request.form['facing']
    propertyage_encoded = (request.form['propertyage_encoded'])

    response = jsonify({
        'estimated_price': util.get_estimated_rent(address, bedroom, area, parking, furnishing, available_for, facing, propertyage_encoded)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()    