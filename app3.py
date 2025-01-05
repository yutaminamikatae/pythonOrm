from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String ,Date ,Text
from sqlalchemy.orm import sessionmaker
from flask import Flask,jsonify, request
from flask_cors import CORS
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
import json
from app import mma
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

Base = declarative_base()
db = SQLAlchemy(app)
ma = Marshmallow(app)

class C_date(Base):
    __tablename__ = "c_date"  # テーブル名を指定
    customer_id = Column(String, primary_key=True)
    customer_date = Column(Date)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("customer_id","customer_date")
        
users_schema = UserSchema(many=True)


@app.route('/create', methods=['POST'])
def create_user():
    try:
        print("start")
        data = request.get_json()
        print(data)
        engine = create_engine("postgresql://postgres:root@localhost:5432/postgres")
        # セッションを作るクラスを作成
        SessionClass = sessionmaker(engine)  
        cdate = C_date(customer_id=data['customer_id'],customer_date=data['customer_date'])
        session = SessionClass()
        session.add(cdate)
        session.commit()
        
        # jsonify(customers)
        a = []
        return request.form['message']
    except Exception as e:
        return a

app.run()