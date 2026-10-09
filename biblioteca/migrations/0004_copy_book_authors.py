from django.db import migrations


def copy_legacy_authors(apps, schema_editor):
    Book = apps.get_model("biblioteca", "Book")
    database = schema_editor.connection.alias

    for book in Book.objects.using(database).only("pk", "author_id").iterator(
        chunk_size=500
    ):
        if book.author_id is None:
            raise RuntimeError(
                f"Book {book.pk} has no legacy author to copy."
            )
        book.authors.add(book.author_id)


def restore_legacy_authors(apps, schema_editor):
    Book = apps.get_model("biblioteca", "Book")
    database = schema_editor.connection.alias

    books = (
        Book.objects.using(database)
        .prefetch_related("authors")
        .iterator(chunk_size=500)
    )
    for book in books:
        author_ids = [author.pk for author in book.authors.all()]
        if not author_ids:
            raise RuntimeError(
                f"Book {book.pk} has no authors; the legacy author field "
                "cannot represent this relationship."
            )
        Book.objects.using(database).filter(pk=book.pk).update(
            author_id=min(author_ids)
        )


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0003_add_book_authors"),
    ]

    operations = [
        migrations.RunPython(copy_legacy_authors, restore_legacy_authors),
    ]
