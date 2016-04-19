# -*- coding: utf-8 -*-
# (c) 2010-2011 Ruslan Popov <ruslan.popov@gmail.com>

from django.conf import settings
from django import get_version
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage

def common_vars(request):
    """
    Function creates common context for all templates.
    """
    return {
        'settings': settings,
        'user': request.user,
        'django_version': get_version(),
        'site': Site.objects.get_current(),
        'site_title': _(u'CB and GSM devices'),
        'lang_code': getattr(request, 'LANGUAGE_CODE', settings.LANGUAGE_CODE),
        }
