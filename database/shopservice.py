from database.models import CarProductShop
from database import get_db


def add_product_db(product_name, car_id, product_price, product_describe, product_qty):
    db = next(get_db())

    product = CarProductShop(car_id=car_id, product_name=product_name, product_price=product_price,
                             product_describe=product_describe, product_qty=product_qty)

    db.add(product)
    db.commit()


def update_product_db(product_id, edit_product, new_product):
    db = next(get_db())

    product = db.query(CarProductShop).filter_by(product_id=product_id).first()

    if product:
        if edit_product == 'product_name':
            product.product_name = new_product

        elif edit_product == 'product_price':
            product.product_price = new_product

        elif edit_product == 'product_describe':
            product.product_describe = new_product

        elif edit_product == 'product_qty':
            product.product_qty = new_product

        db.commit()


def delete_product_db(product_id):
    db = next(get_db())

    product = db.query(CarProductShop).filter_by(product_id=product_id).first()

    if product:
        db.delete(product)
        db.commit()


def list_products_db(product_id):
    db = next(get_db())

    products = db.query(CarProductShop).filter_by(product_id=product_id).all()

    return products


def add_to_cart_db(product_id, product_qty):
    db = next(get_db())

    product = db.query(CarProductShop).filter_by(product_id=product_id).first()

    if product:
        if product.product_qty >= product_qty:
            if product_id in db.cart:
                db.cart[product_id] += product_qty
            else:
                db.cart[product_id] = product_qty
                product.product_qty -= product_qty
                db.commit()


def checkout_db(self):
    db = next(get_db())

    total_cost = 0.0
    for product_id, quantity in self.cart.items():
        product = db.query(CarProductShop).filter_by(product_id=product_id).first()
        if product:
            total_cost += product.product_price * quantity
            product.product_qty -= quantity
            self.session.commit()
    self.cart.clear()

    return total_cost
