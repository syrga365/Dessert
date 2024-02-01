# Generated by Django 4.2.9 on 2024-02-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='dessert',
            name='category',
            field=models.ManyToManyField(related_name='category', to='post.category'),
        ),
    ]
