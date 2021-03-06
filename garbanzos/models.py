from djongo import models
from djongo.models import Model
from djongo.models import *
from djongo.models import fields
from colorfield.fields import ColorField
from django.contrib.auth.models import User

brand_path = "brand_img"
product_path = "prod_img"
categories_path = "cat_img"
carousel_path = "car_img"


# Categories
class CategoryManager(Manager):
    use_in_migrations = True

    def get_by_name(self, name):
        return self.get(name=name)


class Category(Model):
    id = fields.AutoField(auto_created=True, primary_key=True)
    title = CharField(max_length=100, verbose_name="Título")

    objects = CategoryManager()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.title


# Product
class Brand(Model):
    title = CharField(max_length=100, verbose_name="Título")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.title


class Color(Model):
    title = CharField(max_length=100, verbose_name="Título")
    color_code = ColorField(default='#FF0000', verbose_name="Color")

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colores"

    def __str__(self):
        return self.title


class ProductManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class ProductImages(Model):
    id = fields.AutoField(auto_created=True, primary_key=True)
    title = CharField(max_length=100, verbose_name="Título")
    image = ImageField(upload_to=product_path, verbose_name="Imágen")

    path = image.name

    class Meta:
        verbose_name = "Imágen de producto"
        verbose_name_plural = "Imágenes de productos"

    def __str__(self):
        return self.title


class Products(Model):
    id = fields.AutoField(auto_created=True, primary_key=True)

    title = CharField(max_length=30, verbose_name="Título")
    image = ImageField(upload_to=product_path, verbose_name="Imágen")
    detail = TextField(verbose_name="Detalles")

    spec = TextField(verbose_name="Especificaciones")

    price = FloatField(verbose_name="Precio")

    stock = PositiveIntegerField()
    objects = ProductManager()

    active = BooleanField(default=True)

    category = ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Categoría"
    )
    brand = ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name="Marca"
    )

    color = ForeignKey(
        Color,
        on_delete=models.CASCADE,
    )

    other_images = ManyToManyField(
        ProductImages,
        verbose_name="Otras imágenes",
        blank=True
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.title


class Carousel(Model):
    id = fields.AutoField(auto_created=True, primary_key=True)
    title = CharField(max_length=100, verbose_name="Texto")
    image = ImageField(upload_to=carousel_path, verbose_name="Imágen")
    active = BooleanField(verbose_name="Activo")

    class Meta:
        verbose_name = "Imágen para baner"
        verbose_name_plural = "Imágenes para baner"

    def __str__(self):
        return self.title


class Bill(Model):
    id = fields.AutoField(auto_created=True, primary_key=True)
    product = ForeignKey(
        Products,
        on_delete=CASCADE,
        verbose_name="Producto"
    )

    user = ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name="Usuario"
    )

    amount = IntegerField(verbose_name="Cantidad")

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return "Compra de " + self.user.username
