from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'writer', 'created', 'status')
	list_filter = ('title', 'publish', 'status')
	list_editable = ('status',)
	search_fields = ('title', 'status')
	prepopulated_fields = {'slug': ('title', )}
	raw_id_fields = ('writer',)

