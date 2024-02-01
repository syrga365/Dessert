# Generated by Django 4.2.9 on 2024-02-01 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_category_dessert_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewDessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review_desserts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_dessert', to='post.dessert')),
            ],
        ),
    ]
