from django import template

register= template.Library()

@register.simple_tag

def addition(val1, val2):
    val1= int(val1)
    val2= int(val2)

    added= val1+val2

    return added

def subst(val3, val4):
    val3= int(val3)
    val4= int(val4)

    substed= val3+val4

    return substed