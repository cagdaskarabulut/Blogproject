# Generated by Django 2.2.5 on 2019-10-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190930_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=10, verbose_name='Kategori İsim')),
            ],
            options={
                'verbose_name_plural': 'Kategoriler',
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='blog',
            name='kategoriler',
            field=models.ManyToManyField(null=True, to='blog.Kategori'),
        ),
    ]