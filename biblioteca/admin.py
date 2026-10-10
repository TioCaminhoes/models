from django.contrib import admin

from biblioteca.models import Author, Book, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "ano_publicado", "disponivel")
	search_fields = ("title", "author__name")
	list_filter = ("disponivel", "categories")
	filter_horizontal = ("categories", "author")


admin.site.register(Author)
admin.site.register(Category)
