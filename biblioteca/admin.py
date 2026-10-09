from django.contrib import admin

from biblioteca.models import Author, Book, Category


class BookInline(admin.TabularInline):
	model = Book.authors.through
	extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "authors_display", "data_publicacao", "disponivel")
	search_fields = ("title", "authors__name")
	list_filter = ("disponivel", "categories")
	filter_horizontal = ("authors", "categories")

	@admin.display(description="Autores")
	def authors_display(self, obj):
		return ", ".join(author.name for author in obj.authors.all())

	def get_queryset(self, request):
		return super().get_queryset(request).prefetch_related("authors")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	inlines = (BookInline,)


admin.site.register(Category)
