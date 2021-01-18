from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='publish')

class Article(models.Model):
	STATUS = (
		('draft', 'Draft'),
		('publish', 'Publish')
	)
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, allow_unicode=True)
	writer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	body = RichTextUploadingField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=30, choices=STATUS, default='draft')
	objects = models.Manager()
	published = PublishedManager()

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("blog:articleDtails", args=[self.id, self.slug])
	




