from django.db import models

# Create your models here.
class ZhongYiBase(models.Model):
    book_name = models.CharField(max_length=100, blank=False)


class Chapter(models.Model):
    book = models.ForeignKey(ZhongYiBase, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=100, blank=False)


class Paragraph(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.TextField(default="")


