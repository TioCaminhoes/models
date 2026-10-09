from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "autores"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(
        Author,
        related_name="books",
    )
    data_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="books")

    def __str__(self):
        return self.title