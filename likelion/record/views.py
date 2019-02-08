from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.http import HttpResponse


# Create your views here.
def post_new(request):
    if request.method == 'POST': # 채워져 있는 글 (글수정)
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else: # 빈 폼 생성 (글쓰기)
        form = PostForm()
    return render(request, 'record/post_new.html', {'form':form,})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm()
    return render(request, 'record/post_detail.html',{'post':post,'form':form})


def board(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    post_all = Post.objects.all()
    return render(request, 'record/board.html',{'post_all':post_all, 'category':category})

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST': # 채워져 있는 글 (글수정)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else: # 빈 폼 생성 (글쓰기)
        form = PostForm(instance=post)

    return render(request, 'record/post_edit.html', {'form':form,})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(main)
            # 삭제 이후의 페이지를 불러온다

def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return redirect(post)

def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(comment.post)

def main(request) :
    post_all = Post.objects.all()
    category_all = Category.objects.all()
    return render(request, 'record/main.html',{'post_all':post_all,'category_all':category_all})

