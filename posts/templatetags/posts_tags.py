from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.publier.count()

@register.inclusion_tag('posts/recent_post.html')
def show_latest_posts(count=5):
    latest_posts = Post.publier.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.assignment_tag
def get_post_commenter(count=5):
    return Post.publier.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

