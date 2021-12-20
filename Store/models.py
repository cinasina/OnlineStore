from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=200)
    main_name = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='main')
    sub_name = models.ManyToManyField('self', blank=True, related_name='sub')
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_subname = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_category', args=[self.name])


class Product(models.Model):
    main_category = models.ForeignKey(Category, models.CASCADE, related_name='main_category')
    sub_category = models.ForeignKey(Category, models.CASCADE, related_name='sub_category')
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='Products/%Y/%m/%d')
    available = models.BooleanField(default=True)
    tags = TaggableManager()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_single', args=[self.main_category,
                                                     self.sub_category.slug,
                                                     self.pk
                                                     ])
