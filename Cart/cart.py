from Store.models import Product
CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add_product(self, product, quantity):
        product_id = str(product.pk)
        if product_id not in self.cart:
            self.cart[product_id] = {'id': product.pk, 'name': product.name, 'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove_product(self, product):
        product_id = str(product.pk)
        if product_id in self.cart.keys():
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True
