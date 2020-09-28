from django.contrib import admin

from webapp.models import VisitedLinks, VisitedDomain

admin.site.register(VisitedLinks)
admin.site.register(VisitedDomain)
