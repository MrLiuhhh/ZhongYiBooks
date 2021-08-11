from rest_framework import serializers
from .models import ZhongYiBase, Chapter, Paragraph


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    paragraph = ParagraphSerializer

    class Meta:
        model = Chapter
        fields = ('chapter_name', 'paragraph')


class ZhongYiSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer

    class Meta:
        model = ChapterSerializer
        fields = ('book_name', 'chapter')
