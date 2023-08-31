from django.db import models


class Key(models.Model):
    login = models.CharField('User login', max_length=50, default='empty')
    uid = models.CharField('User PC ID', max_length=50, default='empty')
    key = models.CharField('License key', max_length=50, default='empty')
    code = models.CharField('Activation code', max_length=50, default='empty')

    def __str__(self):
        return self.key