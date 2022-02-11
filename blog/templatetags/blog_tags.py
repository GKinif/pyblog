from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
import markdown
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown', needs_autoescape=True)
def markdown_format(text, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    escaped = esc(text)
    return mark_safe(markdown.markdown(escaped))
