from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs':blogs})

def enroll(request):
    return render(request, 'blog/enroll.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})


'''def result(request):
full = request.GET['writing']
words = full.split()
words_dic = {}
for word in words:
    if word in words_dic:
        words_dic[word] += 1
    else:
        words_dic[word] = 1
return render(request, 'result.html', {'full':full, 'length'
:len(words), 'dic':words_dic.items()})

def about(request):
    return render(request, 'about.html')'''