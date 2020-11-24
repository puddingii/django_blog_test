from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'blogs':blogs, 'posts':posts})

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

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')


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