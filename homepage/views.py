from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import SignUpForm, LoginForm, PostForm
from .models import Post


def landing_page(request):
    return render(request, 'homepage/landing.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('homepage:upload')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage:upload')
    else:
        form = SignUpForm()

    return render(request, 'homepage/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage:upload')

    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage:upload')
    else:
        form = LoginForm()

    return render(request, 'homepage/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage:landing')


@login_required(login_url='homepage:login')
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('homepage:wall')
    else:
        form = PostForm()

    return render(request, 'homepage/upload.html', {'form': form})


@login_required(login_url='homepage:login')
def wall_view(request):
    posts = Post.objects.select_related('user').all()
    return render(request, 'homepage/wall.html', {'posts': posts})


@login_required(login_url='homepage:login')
@require_POST
def add_candle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.candle_count += 1
    post.save(update_fields=['candle_count'])
    return JsonResponse({'candle_count': post.candle_count})

