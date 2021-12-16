from django.contrib.sitemaps import Sitemap
from .models import Category, Product


class CategorySiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Category.objects.filter(is_subname=False)

    def lastmod(self, obj):
        return obj.created


class ProductSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.created
