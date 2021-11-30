from django import template
from Store.models import Product


register = template.Library()


@register.inclusion_tag('store/related_product.html')
def related_post(sub_category):
    products = Product.objects.filter(sub_category=sub_category)[:1]
    return {'products': products}
