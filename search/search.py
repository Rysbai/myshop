import re
from shop.models import Product

def search(pattern):
    products_after_result = []
    products = Product.objects.all()
    for product in products:
        result = re.findall(pattern, product)
        if result:
            product_after_result.append(result)

    return products_after_result
