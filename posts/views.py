from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


class PostIndex(ListView):
    template_name = 'posts/index.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostIndex, self).get_context_data(**kwargs)
        context['slider_posts'] = Post.objects.filter(slider_post=True)
        return context


class PostDetail(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context


class CategoryDetail(ListView):
    template_name = 'categories/category_detail.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['category'] = self.category
        return context


class TagDetail(ListView):
    template_name = 'tags/tag_detail.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tag=self.tag).order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagDetail, self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        context['tags'] = self.tag
        return context
