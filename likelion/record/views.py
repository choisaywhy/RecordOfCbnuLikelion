from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category, Recomment
from schedule.models import Event
from .forms import PostForm, CommentForm, RecommentForm
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import (login as django_login, authenticate, logout as django_logout)
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def post_new(request):
    if request.method == 'POST': # 채워져 있는 글 (글수정)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.name_id = User.objects.get(username = request.user.username) 
            post.save() # 없어도 작동하는 지 확인ss
            return redirect(post)
    else: # 빈 폼 생성 (글쓰기)
        form = PostForm()
    return render(request, 'record/post_new.html', {'form':form,})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm()
    return render(request, 'record/post_detail.html',{'post':post,'form':form,})

@login_required
def main(request) :
    post_all = Post.objects.all().order_by('-created_at')
    category_all = Category.objects.all()
    page_numbers_range = 8
    paginator = Paginator(post_all,page_numbers_range)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    schedule_all = Event.objects.all()
    schedule_numbers_range = 8
    paginator_schedule = Paginator(schedule_all, schedule_numbers_range)
    schedules = paginator_schedule.get_page(page)

    return render(request, 'record/main.html',{'post_all':post_all,'category_all':category_all,'posts':posts, 'schedules':schedules})

@login_required
def board(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    post_all = Post.objects.filter(category_id=category).order_by('-created_at')
    page_numbers_range = 8
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(post_all,page_numbers_range)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'record/board.html',{'post_all':post_all, 'category':category, 'posts':posts, 'page_range':page_range, 'paginator':paginator })


# def post_edit(request, post_id):
#     post = get_object_or_404(Post, id=post_id)

#     if request.method == 'POST': # 채워져 있는 글 (글수정)
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else: # 빈 폼 생성 (글쓰기)
#         form = PostForm(instance=post)

#     return render(request, 'record/post_edit.html', {'form':form,})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        if post.name_id == User.objects.get(username = request.user.get_username()):
            post = get_object_or_404(Post, id=post_id)
            form = PostForm(instance=post)
            return render(request, 'record/post_edit.html', {'form':form})
        else:
            return render(request, 'record/warning.html')




# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     post.delete()
#     return redirect(main)
            # 삭제 이후의 페이지를 불러온다
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.name_id == User.objects.get(username = request.user.get_username()):
        post.delete()
        return redirect(main)
    else:
        return render(request, 'record/warning.html')

@login_required
def warning(request):
    return render(request, 'record/warning.html')



def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.name_id = User.objects.get(username = request.user.username) 
        comment.post = post
        comment.save()
    return redirect(post)

def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.name_id == User.objects.get(username = request.user.get_username()):
        comment.delete()
        return redirect(comment.post)
    else:
        return render(request, 'record/warning.html')



def recomment_new(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)
    form = RecommentForm(request.POST)
    if form.is_valid():
        recomment = form.save(commit=False)
        recomment.name_id = User.objects.get(username = request.user.username) 
        recomment.comment = comment
        comment.post = post
        recomment.save()
    return redirect(post)

def recomment_delete(request, post_id, comment_id, recomment_id):
    post = get_object_or_404(Post, id=post_id)
    recomment = get_object_or_404(Recomment, id=recomment_id)
    if recomment.name_id == User.objects.get(username = request.user.get_username()):
        recomment.delete()
        return redirect(recomment.comment.post)
    else:
        return render(request, 'record/warning.html')


# def recomment_delete(request, post_id, comment_id, recomment_id):
#     post = get_object_or_404(Post, id=post_id)
#     recomment = get_object_or_404(Recomment, id=recomment_id)
#     recomment.delete()
#     # return redirect(recomment.comment.post)
#     return redirect(post)


@login_required
def member(request):
    return render(request, 'record/member.html')

@login_required
def introduce(request):
    return render(request, 'record/introduce.html')

