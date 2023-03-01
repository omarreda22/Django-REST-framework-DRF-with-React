from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


# Test This
class PostCustomManager(models.Manager):
	def posts_public(self):
		return self.filter(status=Post.STATUS_CHOICES.PUBLIC)


class Post(models.Model):
	class STATUS_CHOICES(models.TextChoices):
		DRAFT = 'draft', 'Draft'
		PUBLIC = 'public', 'Public'

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	title = models.CharField(max_length=250)
	excerpt = models.TextField(null=True)
	content = models.TextField()
	slug = models.SlugField(max_length=250, unique=True)
	published = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=7, choices=STATUS_CHOICES.choices ,default=STATUS_CHOICES.PUBLIC)
	objects = PostCustomManager()

	class Meta:
		ordering = ('-published', )

	def __str__(self):
		return self.title
