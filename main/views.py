from django.shortcuts import render
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request, "main/index.html")

def article(request, id):
    post = Post.objects.get(id=id)
    related = Post.objects.filter(category=post.category)
    return render(request, "main/article.html", {"post": post, "related": related})

def categorized(request, category):
    if category == "latest":
        posts = Post.objects.all().order_by('-date')[0:8]
    else:
        posts = Post.objects.filter(category=Category.objects.get(code=category)).order_by('-date')
    return render(request, "main/categorized.html", {"ver_post": posts[0], "hor_posts": posts[1:4], "small_posts": posts[4:]})

@csrf_exempt
def content(request, category):
    data = []
    latest_query = Post.objects.all().order_by('-date')
    music_query = Post.objects.filter(category=Category.objects.get(code="music")).order_by('-date')
    literature_query = Post.objects.filter(category=Category.objects.get(code="literature")).order_by('-date')
    theatre_query = Post.objects.filter(category=Category.objects.get(code="theater")).order_by('-date')
    cinema_query = Post.objects.filter(category=Category.objects.get(code="cinema")).order_by('-date')
    for post in latest_query[0:4]:
        temp = dict()
        temp['id'] = post.id
        temp['title'] = post.title
        temp['img'] = post.image.url
        temp['content'] = post.content
        temp['description'] = post.description
        temp['date'] = post.date
        data.append(temp)
    for query in [music_query, literature_query, theatre_query, cinema_query]:
        for i in range(0, 4):
            temp = dict()
            temp['id'] = query[i].id
            temp['title'] = query[i].title
            temp['img'] = query[i].image.url
            temp['content'] = query[i].content
            temp['description'] = query[i].description
            temp['date'] = query[i].date
            data.append(temp)
    return JsonResponse(data, safe=False)