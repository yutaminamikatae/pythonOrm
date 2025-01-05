from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/postgres'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(32))
    customer_age = db.Column(db.Integer)
    customer_birthday = db.Column(db.Date)
    customer_gender = db.Column(db.Text)
    customer_location = db.Column(db.Text)

    def __init__(self, customer_id, customer_name,customer_age,
                 customer_birthday,customer_gender,customer_location):
       self.customer_id = customer_id
       self.customer_name = customer_name
       self.customer_age = customer_age
       self.customer_birthday = customer_birthday
       self.customer_gender = customer_gender
       self.customer_location = customer_location

class CustomersSchema(ma.Schema):
   class Meta:
       fields = ("customer_id", "customer_name", "customer_age",
                  "customer_birthday", "customer_gender", "customer_location")

customer_schema = CustomersSchema()
customer_schema = CustomersSchema(many=True)

@app.route("/db", methods=["GET"])
def get_customer():
   customer_users = Customers.query.all()

   return customer_schema.jsonify(customer_users)

# 20240515 追加
@app.route('/create', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    new_customer = Customers(customer_id=data['customer_id'], customer_name=data['customer_name'],
                         customer_age=data['customer_age'], customer_birthday=data['customer_birthday'],
                         customer_gender=data['customer_gender'], customer_location=data['customer_location'])
    db.session.add(new_customer)
    db.session.commit()  

    return jsonify({
        'id': new_customer.customer_id,
        'name': new_customer.customer_name,
        'age': new_customer.customer_age,
        'birthday': new_customer.customer_birthday,
        'gender': new_customer.customer_gender,
        'location': new_customer.customer_location,
    }), 201  

  except Exception as e:
    return make_response(jsonify({'message': 'error creating user', 'error': str(e)}), 500)



app.run()

#    for customer in customer_users:
    #    print(type(customer))
#        print(customer.customer_name)
       
#    print(type(customer_users))
#    print(type(customer_schema.jsonify(customer_users)))
#    print(customer_schema.jsonify(customer_users))

# conn = psycopg2.connect(
#         host='localhost',
#         port=5432,
#         database='postgres',
#         user='postgres',
#         password='root',
#     )
# {database}?charset={charset_type})








