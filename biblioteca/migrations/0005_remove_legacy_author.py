from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0004_copy_book_authors"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(
                related_name="books",
                to="biblioteca.author",
            ),
        ),
    ]
