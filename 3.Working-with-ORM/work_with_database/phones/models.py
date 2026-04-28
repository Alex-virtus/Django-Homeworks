from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    """
    Модель смартфона для интернет-магазина.

    Содержит основную информацию о телефоне: название, цену,
    изображение, дату выхода, наличие LTE и URL-идентификатор (slug).

    Slug генерируется автоматически из названия при сохранении объекта.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=1)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Переопределяем метод сохранения объекта.
        Если slug не задан — генерируем его из названия телефона.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # Вариант чтобы избежать IntegrityError
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         base_slug = slugify(self.name)
    #         slug = base_slug
    #         counter = 1
    #
    #         # Проверка на существование одинакового slug
    #         while Phone.objects.filter(slug=slug).exists():
    #             # Если существует, добавляем номер: iphone-15 -> iphone-15-2
    #             slug = f"{base_slug}-{counter}"
    #             counter += 1
    #
    #         self.slug = slug
    #
    #     super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Человеко-читаемое представление объекта.
        Используется в админке и интерфейсах Django.
        """
        return self.name
