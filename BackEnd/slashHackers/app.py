from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Float
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager,jwt_required,create_access_token


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir,'users.db')
app.config['JWT_SECRET_KEY']='super-secret'


db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database Created')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')


@app.cli.command('db_seed')
def db_seed():
    uthpala = User(f_name='uthpala',
                   l_name='bandara',
                   email='uthpala@gmail.com',
                   password='uthpala@123')


    chamodya = User(f_name='chamodya',
                   l_name='lekam',
                   email='chamodya@gmail.com',
                   password='chamodya@123')

    db.session.add(uthpala)
    db.session.add(chamodya)
    db.session.commit()
    print('Database seeded')



@app.route('/register',methods=['POST'])
def register():
    email = request.json['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='email already exists')
    else:
        f_name=request.json['f_name']
        l_name=request.json['f_name']
        password=request.json['password']
        user=User(f_name=f_name,l_name=l_name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User Created successfully")



@app.route('/login',methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']

    test = User.query.filter_by(email=email,password=password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message="login succeeded", access_token=access_token)
    else:
        return jsonify(message="enter Again"),401



#database models
class User(db.Model):
    _tablename_ ='Users'
    id = Column(Integer,primary_key=True)
    f_name = Column(String)
    l_name =Column(String)
    email = Column(String,unique=True)
    password = Column(String)



class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','f_name','l_name','email','password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


if __name__ == '__main__':
    app.run()
