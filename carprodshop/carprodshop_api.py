from fastapi import Body

from carprodshop import shop_router

from database.shopservice import (add_product_db, update_product_db, delete_product_db,
                                  list_products_db, add_to_cart_db, checkout_db)


@shop_router.post('/add-new-product')
async def add_product(product_name: str = Body(...), car_id: int = Body(...), product_price: float = Body(...),
                      product_describe: str = Body(...), product_qty: int = Body(...)):
    result = add_product_db(product_name=product_name, car_id=car_id, product_price=product_price,
                            product_describe=product_describe, product_qty=product_qty)

    return {'status': 1, 'message': result}


@shop_router.put('/update-product')
async def update_product(product_id: int = Body(...), edit_product: str = Body(...), new_product: str = Body(...)):
    result = update_product_db(product_id=product_id, edit_product=edit_product, new_product=new_product)

    return {'status': 1, 'message': result}


@shop_router.delete('/delete-product')
async def delete_product(product_id: int):
    result = delete_product_db(product_id=product_id)

    return {'status': 1, 'message': result}


@shop_router.get('/product-list')
async def list_products(product_id: int):
    result = list_products_db(product_id=product_id)

    return {'status': 1, 'message': result}


@shop_router.put('/add-to-cart')
async def add_to_cart(product_id: int = Body(...), product_qty: int = Body(...)):
    result = add_to_cart_db(product_id=product_id, product_qty=product_qty)

    return {'status': 1, 'message': result}


@shop_router.put('/checkout')
async def checkout(self):
    result = checkout_db(self=self)

    return {'status': 1, 'message': result}
