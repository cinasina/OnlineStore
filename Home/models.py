from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} With This Email: {} Has Something To Say!'.format(self.name, self.email)


