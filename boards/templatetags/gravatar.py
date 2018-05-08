

from django import template
from django.conf import settings
import hashlib
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

register = template.Library()


@register.filter
def gravatar(user):
    url=''
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url
