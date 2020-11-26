from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'blogs':blogs, 'posts':posts})

#write post
def enroll(request):
    if request.method=="POST":
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/blog/'+str(post.id))

    else:
        form = BlogPost()
        return render(request, 'blog/writing.html', {'form':form, 'title':'enroll'})

#post detail
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

#delete post
def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

#edit post
def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method=="POST":
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date = timezone.datetime.now()
            blog.save()
            return redirect('/blog/'+str(blog.pk))
    else:
        form = BlogPost(instance = blog)
        return render(request, 'blog/writing.html', {'form':form, 'title':'edit'})
