import db

def delete_product(product_id):
    db.connect()
    db.delete_product(product_id)
    print("Product ID " + str(product_id) + " was deleted from database.\n")
