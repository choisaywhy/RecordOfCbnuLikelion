from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category, Recomment
from .forms import PostForm, CommentForm, RecommentForm
from django.http import HttpResponse
from django.core.paginator import Paginator


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

def main(request) :
    post_all = Post.objects.all().order_by('-created_at')
    category_all = Category.objects.all()
    page_numbers_range = 5
    paginator = Paginator(post_all,page_numbers_range)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'record/main.html',{'post_all':post_all,'category_all':category_all,'posts':posts})

def board(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    post_all = Post.objects.all().order_by('-created_at')
    page_numbers_range = 5
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(post_all,page_numbers_range)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'record/board.html',{'post_all':post_all, 'category':category, 'posts':posts, 'page_range':page_range, 'paginator':paginator })

def board_free(request):
    post_all = Post.objects.all().order_by('-created_at')
    category_all = Category.objects.all()
    page_numbers_range = 5
    paginator = Paginator(post_all,page_numbers_range)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'record/board_free.html',{'post_all':post_all,'category_all':category_all,'posts':posts})


def board_notice(request):
    post_all = Post.objects.all().order_by('-created_at')
    category_all = Category.objects.all()
    page_numbers_range = 5
    paginator = Paginator(post_all,page_numbers_range)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'record/board_notice.html',{'post_all':post_all,'category_all':category_all,'posts':posts})


def board_project(request):
    post_all = Post.objects.all().order_by('-created_at')
    category_all = Category.objects.all()
    page_numbers_range = 5
    paginator = Paginator(post_all,page_numbers_range)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'record/board_project.html',{'post_all':post_all,'category_all':category_all,'posts':posts})


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


def recomment_new(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    form = RecommentForm(request.COMMENT)
    if form.is_valid():
        recomment = form.save(commit=False)
        recomment.comment = comment
        recomment.comment.post = post
        recomment.save()
    return redirect(post)

def recomment_delete(request, post_id, comment_id, recomment_id):
    recomment = get_object_or_404(Recomment, id=recomment_id)
    recomment.delete()
    return redirect(recomment.comment.post)



def member(request):
    return render(request, 'record/member.html')