from django.urls import path
import ZhongYiBase.views

urlpatterns = [
    path('zhongyibase/', ZhongYiBase.views.FetchData.as_view()),
]
