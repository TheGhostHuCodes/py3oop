import ecommerce.products
from ecommerce.payments import paypal
import ecommerce.database as db

product = ecommerce.products.Product()

payment = paypal.Paypal()

db.initialize_database()
