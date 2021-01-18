import blog
from django.shortcuts import render, get_object_or_404
from .models import * 

def allArticle(request):
	allArticles = Article.published.all()
	context = {'allArticles': allArticles}
	return render(request, 'blog/allart.html', context)

def articleDtails(request, pk, slug):
	artdetails = get_object_or_404(Article, id=pk, slug=slug)
	context = {'artdetails': artdetails}
	return render(request, 'blog/artDetail.html', context)
