from django.shortcuts import render
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request, "main/index.html")

@csrf_exempt
def content(request, category):
    data = []
    if category == 'all':
        for post in Post.objects.all():
            temp = dict()
            temp['title'] = post.title
            temp['img'] = post.image.url
            temp['content'] = post.content
            temp['description'] = post.description
            temp['date'] = post.date
            data.append(temp)
    else:
        for post in Post.objects.filter(category=Category.objects.get(code=category)):
            temp = dict()
            temp['title'] = post.title
            temp['img'] = post.image.url
            temp['content'] = post.content
            temp['description'] = post.description
            temp['date'] = post.date
            data.append(temp)
    return JsonResponse(data, safe=False)