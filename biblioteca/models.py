from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models

from biblioteca.validators import validar_ano_publicado, validar_tamanho_arquivo


class Author(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "autores"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(3, "O título precisa ter pelo menos 3 caracteres."),
        ],
    )
    author = models.ManyToManyField(
        Author,
        related_name="books",
    )
    ano_publicado = models.IntegerField(
        validators=[validar_ano_publicado],
    )
    paginas = models.PositiveIntegerField(
        "páginas",
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1, "O livro precisa ter pelo menos 1 página."),
            MaxValueValidator(5000, "O livro pode ter no máximo 5000 páginas."),
        ],
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        blank=True,
        validators=[
            RegexValidator(r"^\d{13}$", "O ISBN deve ter exatamente 13 dígitos (apenas números)."),
        ],
    )
    capa = models.ImageField(
        "capa",
        upload_to="capas/",
        blank=True,
        validators=[
            validar_tamanho_arquivo,
            FileExtensionValidator(["jpg", "jpeg", "png"]),
        ],
    )
    disponivel = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="books")

    def __str__(self):
        return self.title
