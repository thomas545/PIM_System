# Generated by Django 2.1.7 on 2019-05-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='_category_categories_+', to='pim_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Product_Code', models.CharField(blank=True, max_length=200, null=True)),
                ('Price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('categories', models.ManyToManyField(blank=True, related_name='products', to='pim_app.Category')),
            ],
        ),
    ]