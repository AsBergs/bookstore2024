from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_editora_cidade_editora_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Autor",
                "verbose_name_plural": "Autores",
            },
        ),
    ]