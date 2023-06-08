from django.db import models


class Telefon(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        # managed = False
        verbose_name_plural = 'Telefon'

    def __str__(self):
        return self.nomi

class Brand(models.Model):
    name = models.CharField(max_length=100)
    phones = models.ForeignKey(Telefon, null=True, on_delete=models.SET_NULL)

    class Meta:
        # managed = False
        verbose_name_plural = 'brand'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    memory = models.PositiveSmallIntegerField(blank=False)
    color = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    phone = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)

    class Meta:
        # managed = False
        verbose_name_plural = 'model'

    def __str__(self):
        return self.title

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

