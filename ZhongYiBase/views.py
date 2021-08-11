from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import ZhongYiBase, Chapter, Paragraph
from .serializer import ZhongYiSerializer, ChapterSerializer, ParagraphSerializer
import requests
import re


class BookViewSet(ModelViewSet):
    queryset = ZhongYiBase.objects.all()
    serializer_class = ZhongYiSerializer


class FetchData(APIView):
    def get(self, request):
        html = requests.get('http://www.51xingjy.com/7649.html')
        content = html.text
        chapter_urls = re.findall('<a href="(.*?)">(.*?)</a><br />', content)
        chapter_urls = chapter_urls[1:]
        chapter_9 = re.findall('<a href="(.*?)">(.*?)</a></p>', content)
        chapter_urls.append(chapter_9.pop())

        book = ZhongYiBase.objects.create(
            book_name='中医基础'
        )

        for url in chapter_urls:
            self.fill_data(url, book.id)

        ret = {
            'msg': '抓取数据成功'
        }
        return Response(ret)

    def fill_data(self, chapter_url, book_id):
        url = chapter_url[0]
        chapter_name = chapter_url[1]

        html = requests.get(url)
        content = html.text
        paragraph = re.findall('<p>(.*?)</p>', content)

        chapter = Chapter.objects.create(
            book_id=book_id,
            chapter_name=chapter_name
        )

        for para in paragraph:
            Paragraph.objects.create(
                chapter_id=chapter.id,
                content=para
            )
