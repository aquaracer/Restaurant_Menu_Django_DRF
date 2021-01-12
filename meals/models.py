from django.db import models
from django.core import validators


class Allergens(models.Model):
    """Аллергены"""

    name = models.CharField("Название", max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аллерген'
        verbose_name_plural = 'Аллергены'


class Category(models.Model):
    """Категории"""

    name = models.CharField('Название категории', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Meals(models.Model):
    """Блюда"""

    name = models.CharField("Название", max_length=30, db_index=True, unique=True)
    proteins = models.PositiveSmallIntegerField("Белки", validators=[validators.MaxValueValidator(10000)])
    fats = models.PositiveSmallIntegerField("Жиры", validators=[validators.MaxValueValidator(10000)])
    carbohydrates = models.PositiveSmallIntegerField("Углеводы", validators=[validators.MaxValueValidator(10000)])
    calories = models.PositiveSmallIntegerField(verbose_name="Калории")
    price = models.DecimalField("Стоимость", max_digits=7, decimal_places=2, default=100,
                                validators=[validators.MinValueValidator(0)])
    picture = models.ImageField("Изображение", null=True, blank=True)
    allergens = models.ManyToManyField(Allergens, verbose_name='Аллергены')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
