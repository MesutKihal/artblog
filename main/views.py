from django.shortcuts import render
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Subquery

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
def search(request, value):
    data = []
    if value == "none":
        for post in Post.objects.all().order_by('-date'):
            temp = dict()
            temp['id'] = post.id
            temp['title'] = post.title
            temp['img'] = post.image.url
            temp['content'] = post.content
            temp['description'] = post.description
            temp['date'] = post.date
            data.append(temp)
    else:
        for post in Post.objects.filter(title__icontains=value).order_by('-date'):
            temp = dict()
            temp['id'] = post.id
            temp['title'] = post.title
            temp['img'] = post.image.url
            temp['content'] = post.content
            temp['description'] = post.description
            temp['date'] = post.date
            data.append(temp)
    return JsonResponse(data, safe = False)

@csrf_exempt
def content(request, category):
    data = []
    latest_query = list(Post.objects.all().order_by('-date'))[0:8]
    music_query = [post for post in Post.objects.filter(category=Category.objects.get(code="music")).order_by('-date') if post not in latest_query]
    literature_query = [post for post in Post.objects.filter(category=Category.objects.get(code="literature")).order_by('-date') if post not in latest_query]
    theatre_query = [post for post in Post.objects.filter(category=Category.objects.get(code="theater")).order_by('-date') if post not in latest_query]
    cinema_query = [post for post in Post.objects.filter(category=Category.objects.get(code="cinema")).order_by('-date') if post not in latest_query]
    categorized_query = [music_query, literature_query, theatre_query, cinema_query]
    for post in latest_query[0:4]:
        temp = dict()
        temp['id'] = post.id
        temp['title'] = post.title
        temp['img'] = post.image.url
        temp['content'] = post.content
        temp['description'] = post.description
        temp['date'] = post.date
        data.append(temp)
    for query in categorized_query:
        for i in range(0, 4):
            temp = dict()
            temp['id'] = query[i].id
            temp['title'] = query[i].title
            temp['img'] = query[i].image.url
            temp['content'] = query[i].content
            temp['description'] = query[i].description
            temp['date'] = query[i].date
            data.append(temp)
            
    left = []
    for post in music_query[4:]:
        temp = dict()
        temp['id'] = post.id
        temp['title'] = post.title
        temp['img'] = post.image.url
        temp['content'] = post.content
        temp['description'] = post.description
        temp['date'] = post.date
        data.append(temp)
    for post in literature_query[4:]:
        temp = dict()
        temp['id'] = post.id
        temp['title'] = post.title
        temp['img'] = post.image.url
        temp['content'] = post.content
        temp['description'] = post.description
        temp['date'] = post.date
        data.append(temp)
    for post in theatre_query[4:]:
        temp = dict()
        temp['id'] = post.id
        temp['title'] = post.title
        temp['img'] = post.image.url
        temp['content'] = post.content
        temp['description'] = post.description
        temp['date'] = post.date
        data.append(temp)
    for post in cinema_query[4:]:
        temp = dict()
        temp['id'] = post.id
        temp['title'] = post.title
        temp['img'] = post.image.url
        temp['content'] = post.content
        temp['description'] = post.description
        temp['date'] = post.date
        data.append(temp)
    return JsonResponse(data, safe=False)