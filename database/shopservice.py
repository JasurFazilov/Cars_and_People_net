from database.models import CarProductShop
from database import get_db


def add_item_db(product_name, product_price, product_describe, product_qty):
    db = next(get_db())

    if:
        new_product = CarProductShop(product_name=product_name, product_price=product_price, product_describe=product_describe, product_qty=product_qty)

        db.add(new_product)
        db.commit()
        return new_product.product_id

