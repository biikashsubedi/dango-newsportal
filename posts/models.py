from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from newsPortal.utils import unique_slug_generator


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(null=True, blank=True, default='slug')

    def __str__(self):
        return self.title

    def save_base(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save_base(*args, **kwargs)

    def post_count(self):
        return self.postByCategory.all().count()


class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(blank=True, max_length=20, default='slug')
    
    def __str__(self):
        return self.title
    
    def save_base(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save_base(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media')
    source = models.CharField(max_length=25)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='postByCategory')
    slug = models.SlugField(null=True, blank=True, default='slug', max_length=20)
    tag = models.ManyToManyField(Tag, related_name='tagByPosts')
    slider_post = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
        
    def save_base(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save_base(*args, **kwargs)
