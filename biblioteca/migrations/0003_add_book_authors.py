from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0002_normalize_authors_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(
                related_name="authored_books",
                to="biblioteca.author",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="books",
                to="biblioteca.author",
            ),
        ),
    ]
