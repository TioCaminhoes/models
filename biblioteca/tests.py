from django.test import TestCase
from django.db.models.deletion import ProtectedError
from django.urls import reverse

from .models import Author, Book, Category


class LibraryModelTests(TestCase):
	def test_author_string_ordering_and_plural_name(self):
		author = Author.objects.create(name="Machado de Assis")

		self.assertEqual(str(author), "Machado de Assis")
		self.assertEqual(Author._meta.ordering, ["name"])
		self.assertEqual(Author._meta.verbose_name_plural, "autores")

	def test_book_has_author_and_categories_are_optional(self):
		author = Author.objects.create(name="Machado de Assis")
		book = Book.objects.create(
			title="Dom Casmurro",
			author=author,
			publication_year=1899,
		)

		self.assertEqual(str(book), "Dom Casmurro")
		self.assertEqual(author.books.get(), book)
		self.assertEqual(list(book.categories.all()), [])

	def test_author_with_books_cannot_be_deleted(self):
		author = Author.objects.create(name="Machado de Assis")
		Book.objects.create(
			title="Dom Casmurro",
			author=author,
			publication_year=1899,
		)

		with self.assertRaises(ProtectedError):
			author.delete()

	def test_category_string(self):
		category = Category.objects.create(name="Romance")

		self.assertEqual(str(category), "Romance")


class LibraryViewTests(TestCase):
	def setUp(self):
		self.author = Author.objects.create(name="Machado de Assis")
		self.book = Book.objects.create(
			title="Dom Casmurro",
			author=self.author,
			publication_year=1899,
		)

	def test_book_list_links_to_author_detail(self):
		response = self.client.get("/")

		self.assertContains(
			response,
			f'href="{reverse("author_detail", args=[self.author.pk])}"',
		)

	def test_author_detail_lists_all_books(self):
		response = self.client.get(
			reverse("author_detail", args=[self.author.pk])
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["author"], self.author)
		self.assertContains(response, self.book.title)

	def test_author_detail_returns_404_for_unknown_author(self):
		response = self.client.get(reverse("author_detail", args=[999]))

		self.assertEqual(response.status_code, 404)
