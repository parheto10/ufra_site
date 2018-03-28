# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.utils import timezone
from django.db.models import Count

from .models import Post, Comment
from .forms import EmailForm, CommentForm
from taggit.models import Tag
from annonces.models import Annonce

def partager(request, slug=None):
    #retrieve by post id
    post = get_object_or_404(Post, slug=slug, status='published')
    sent = False

    if request.method == 'POST':
        #Form was submitted
        form = EmailForm(request.POST)
        if form.is_valid():
            #Form fieldspassed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommands you reading "{}"'.format(cd['nom'], cd['email'], post.titre)
            message = 'Read "{}" at {}\n\n{}\'s message: {}'.format(post.titre, post_url, cd['nom'], cd['message'])
            #send_mail(subject, message, 'admin@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailForm()
    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(request, 'posts/partager.html', context)

def post_list(request, tag_slug=None):
    today = timezone.now().date()
    queryset_list = Annonce.objects.active()  # .order_by("-timestamp")
    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    object_list = Post.publier.all()
    tag = None
    if tag_slug :
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(
            Q(titre__icontains=query) |
            Q(message__icontains=query)
        ).distinct()
    paginator = Paginator(object_list, 4)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page,
        'tag': tag,
        "object_list": queryset,
        "titre": "Ufra-Annonces",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, 'posts/liste.html', context)

class PostListView(ListView):
    """

    """
    queryset = Post.publier.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'posts/liste.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # list des commentaires actif par post
    comments = post.comments.filter(active=True).order_by('-updated')
    if request.method == 'POST':
        # Commentaire poster avec success
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # creerl'objet commentaire sans enregistrer dans la base de donnée
            new_comment = comment_form.save(commit=False)
            # Assigner le Poste actuel au commentaire
            new_comment.post = post
            # enregistrer le commentaire dans la base de donnée
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.publier.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    context = {
        'post':post,
        'comments':comments,
        'comment_form': comment_form,
        'similar_posts': similar_posts,
    }
    return render(request, 'posts/detail.html', context)


# Create your views here.
