from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None)
    articul = models.CharField(max_length=256, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ["price", "-price"]

    # def save(self, *args, **kwargs):
    #     price_currency = self.price
    #     self.price = price_currency * 25.0
    #     # return self.price
    #     super(ProductImage, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "%s" % self.id

    # def save(self, *args, **kwargs):
    #     price = self.product.price
    #     self.price = price
    #     # return self.price
    #     super(ProductImage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'