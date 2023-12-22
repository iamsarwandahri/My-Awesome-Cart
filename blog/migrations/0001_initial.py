# Generated by Django 4.1 on 2023-12-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('chead0', models.TextField(default='')),
                ('head1', models.CharField(default='', max_length=500)),
                ('chead1', models.TextField(default='')),
                ('head2', models.CharField(default='', max_length=500)),
                ('chead2', models.TextField(default='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
