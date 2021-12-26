from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100) # automatically checks and validates for mail format


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    # db_index=True is for search engine optimization set automatically in SlugFields
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts")
    # one-to-many relation
    # SET_NULL means if author is deleted, set post's author to null
    # related_name is used to access author's posts from Post model as "author.posts"


