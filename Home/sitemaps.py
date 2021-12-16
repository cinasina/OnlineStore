from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'Never'

    def items(self):
        return ['home:home', 'home:contact']

    def location(self, item):
        return reverse(item)
