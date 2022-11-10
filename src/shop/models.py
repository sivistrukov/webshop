from django.db import models

PRODUCT_LABEL = [
    ('SALE', 'sale'),
    ('NEW', 'new'),
    ('HOT', 'hot'),
    ('NONE', 'none'),
]


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание', max_length=500)
    slug = models.SlugField(verbose_name='Slug', max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание', max_length=500)
    price = models.IntegerField(verbose_name='Цена')
    sale = models.IntegerField(verbose_name='Цена со скидкой', default=None, null=True, blank=True)
    label = models.CharField(verbose_name='Метка', max_length=5, default='NEW', choices=PRODUCT_LABEL, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductsImage(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to='products/')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'

    def __str__(self):
        return self.image.url


class Cart():
    pass
