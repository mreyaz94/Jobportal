from django import template
register = template.Library()

def truncate5(value):
    result = value[0:5]
    return result
register.filter('truncate5', truncate5)

def truncate12(value):
    result = value[0:12]
    return result
register.filter('truncate12', truncate12)

def truncate_n(value,n):
    result = value[0:n]
    return result
register.filter('t_n', truncate_n)