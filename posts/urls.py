from django.urls import path
from .views import *

urlpatterns = [
    path('', PostIndex.as_view(), name='index'),
    path('news/<slug:slug>/', PostDetail.as_view(), name='news'),
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('tag/<slug:slug>/', TagDetail.as_view(), name='tag_detail'),

]
