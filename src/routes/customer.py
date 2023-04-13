from flask import Blueprint,jsonify
import jsonpickle
# Models
from models.customer_model import customerModel
from models.entities import customer
main = Blueprint('customer_blueprint', __name__)


@main.route('/')
def get_customers():
    try:
        customers = customerModel.get_customers() 
        #return jsonpickle.encode(customers)
        return jsonify(customers)
    except Exception as ex:
        return jsonify({'message':"customers test"})
    
@main.route('/<id>')
def get_customer(id):
    try:
        customer = customerModel.get_customer(id)
        if customer != None:
            return jsonify(customer)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500