from firebase_admin import db
from django import template

register = template.Library()

@register.filter(name="is_admin")
def is_admin(cookie):
    database = db.reference(f'Users/{cookie}/')
    database = database.get()
    if database['category'] == 'admin':
        return True
    else:
        return False
    
