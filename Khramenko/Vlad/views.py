from django.shortcuts import render, redirect
from .forms import section
tapeNews = []
def post(request):
    Section = section()
    return render(request, 'createPost.html', {'form': Section})
def create(request):
    Title = request.GET.get('Title')
    url = request.GET.get('URL')
    text = request.GET.get('text')
    Publish = request.GET.get('Publish')
    img = request.GET.get('img')
    Category= request.GET.get('Category')
    data = request.GET.get('data')
    post = [Title, url, text, Publish, Category,img, data]
    tapeNews.append(post)
    return render(request, 'news.html', {'form': [tapeNews[i] for i in range(len(tapeNews))]})