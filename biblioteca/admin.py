from django.contrib import admin

from biblioteca.models import Author, Book, Category


class BookInline(admin.TabularInline):
	model = Book
	extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "ano_publicado", "disponivel")
	search_fields = ("title", "author__name")
	list_filter = ("disponivel", "categories")
	filter_horizontal = ("categories",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	inlines = (BookInline,)


admin.site.register(Category)
