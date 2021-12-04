from django import template
from Store.models import Product


register = template.Library()


@register.inclusion_tag('store/related_product.html')
def related_product(sub_category, name=None):
    products = Product.objects.filter(sub_category=sub_category).exclude(sub_category=sub_category, name=name)[:1]
    return {'products': products}
