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
    image = models.ImageField(verbose_name='Изображение', upload_to='static/products/')
    price = models.IntegerField(verbose_name='Цена')
    sale = models.IntegerField(verbose_name='Цена со скидкой', null=True)
    label = models.CharField(verbose_name='Метка', max_length=5, default='NEW', choices=PRODUCT_LABEL, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
