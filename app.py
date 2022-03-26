from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy.sql import func

# initialize flask
app = Flask(__name__)

api = Api(app)

# create db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# create users table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)  # verification of only one such email in db
    credit_card = db.Column(db.Integer, nullable=True)
    created_on = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    street_num = db.Column(db.String(150), nullable=False)
    post_code = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(150), nullable=False)


# create products table
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(2), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

db.create_all()


# verify if it's a valid credit card number
def verify_credit_card(card_num):
    if len(card_num) != 16:
        return False
    else:
        if card_num[0] not in (4, 5, 6):
            return False
        #TODO: finish it



# creating a resource
class AddUser(Resource):

    def post(self):
        # get posted data
        posted_data = request.get_json()

        #check if user exist
        user_email = posted_data["email"]
        if Users.query.filter_by(email=user_email).first():
            return_map = {
                "status code": 403,
                "msg": "User with that email already exists"
            }
            return jsonify(return_map)

        #add user to db
        new_user = Users(
            name=posted_data["name"],
            last_name=posted_data["last name"],
            email=posted_data["email"],
            credit_card=posted_data["credit card"],
            street_num=posted_data["street and number"],
            post_code=posted_data["post code"],
            city=posted_data["city"],
            country=posted_data["country"]
        )
        db.session.add(new_user)
        db.session.commit()

        return_map = {
            "status code": 200,
            "msg": "Successfuly added new user."
        }
        return jsonify(return_map)


class RemoveUser(Resource):

    def delete(self):
        posted_data = request.get_json()

        user_email = posted_data["email"]
        user = Users.query.filter_by(email=user_email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return_map = {
                "status code": 200,
                "msg": f"Successfuly removed user with email: {user_email}."
            }
            return jsonify(return_map)
        else:
            return_map = {
                "status code": 404,
                "msg": "No such user in db."
            }
            return jsonify(return_map)


class AddProduct(Resource):

    def post(self):
        posted_data = request.get_json()

        #check if valid catogory
        if posted_data["category"] not in ("trenerki", "pizami", "bluzi"):
            return_map = {
                "status code": 402,
                "msg": "Not a valid product category."
            }
            return jsonify(return_map)

        #check if valid size
        if posted_data["size"] not in ("S", "M", "L", "XL"):
            return_map = {
                "status code": 405,
                "msg": "Not a valid size description."
            }
            return jsonify(return_map)

        new_product = Products (
            name=posted_data["name"],
            category=posted_data["category"],
            amount=posted_data["amount"],
            size=posted_data["size"],
            price=posted_data["price"]
        )
        db.session.add(new_product)
        db.session.commit()
        return_map = {
            "status code": 200,
            "msg": "New item added"
        }
        return jsonify(return_map)


class RemoveProduct(Resource):

    def delete(self):
        posted_data = request.get_json()

        product_name = posted_data["name"]
        product = Products.query.filter_by(name=product_name).first()  # there might be more items with the same name
        if product:
            db.session.delete(product)
            db.session.commit()
            return_map = {
                "status code": 200,
                "msg": f"Successfuly removed product: {product_name}."
            }
            return jsonify(return_map)
        else:
            return_map = {
                "status code": 404,
                "msg": f"No such product in db: {product_name}."
            }
            return jsonify(return_map)


class ListProducts(Resource):

    def get(self):
        all_products = Products.query.order_by(Products.price)
        return jsonify(products_by_price=[product.to_dict() for product in all_products])



api.add_resource(AddUser, "/add_user")
api.add_resource(RemoveUser, "/remove_user")
api.add_resource(AddProduct, "/add_product")
api.add_resource(RemoveProduct, "/remove_product")
api.add_resource(ListProducts, "/list_products")



if __name__ == "__main__":
    app.run(debug=True)