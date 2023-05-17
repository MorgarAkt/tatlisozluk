from django import template

register = template.Library()

@register.filter
def is_liked_by_user(entry, user):
    return entry.is_liked_by_user(user)

@register.filter
def is_disliked_by_user(entry, user):
    return entry.is_disliked_by_user(user)

@register.filter
def custom_range(start, end):
    return range(start, end+1)