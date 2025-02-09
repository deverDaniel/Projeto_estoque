# Generated by Django 4.1 on 2025-02-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0007_alter_ingrediente_unidade_medida"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produtoingrediente",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name="produtoingrediente",
            unique_together={("produto", "ingrediente")},
        ),
        migrations.AddConstraint(
            model_name="produtoingrediente",
            constraint=models.UniqueConstraint(
                fields=("produto", "ingrediente"), name="unique_produto_ingrediente"
            ),
        ),
    ]
