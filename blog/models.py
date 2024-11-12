from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published")) # draft defined as zero, published as 1 default saves as draft.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    ) # One to many or foreign key.
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # auto now add is default created time, time of post entry.
    status = models.IntegerField(choices=STATUS, default=0)