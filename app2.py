from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String ,Date ,Text
from sqlalchemy.orm import sessionmaker
from flask import Flask,jsonify
from flask_cors import CORS
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
import json
from app import mma
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# conn = psycopg2.connect(
#         host='localhost',
#         port=5432,
#         database='postgres',
#         user='postgres',
#         password='root',
#     )
# {database}?charset={charset_type})



# meta = MetaData(engine)
# meta.reflect()  
# Base = declarative_base(metadata=meta)
Base = declarative_base()
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Customers(Base):
    __tablename__ = "customers"  # テーブル名を指定
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(32))
    customer_age = Column(Integer)
    customer_birthday = Column(Date)
    customer_gender = Column(Text)
    customer_location = Column(Text)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("customer_id", "customer_name", "customer_age",
                  "customer_birthday", "customer_gender", "customer_location")
        
users_schema = UserSchema(many=True)


@app.route('/db')
def index():
    engine = create_engine("postgresql://postgres:root@localhost:5432/postgres")
    SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
    session = SessionClass()
    customers = session.query(Customers).all()
    print(type(customers))
    # jsonify(customers)
    
    a = []
    
    
    for customer in customers:
        print('-------')
        # print(customer.customer_name)        
        customer_json = users_schema.dumps(customer)
        print(customer_json)
        a.append(customer_json)
        print('-------')
    
    # print('-------')
    # print(customers)
    # print('-------')
    return a

app.run()











