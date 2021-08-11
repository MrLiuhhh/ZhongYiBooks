# Generated by Django 3.2.6 on 2021-08-09 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ZhongYiBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZhongYiBase.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZhongYiBase.zhongyibase'),
        ),
    ]
