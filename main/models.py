from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
