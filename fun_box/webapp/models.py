from django.db import models


class VisitedLinks(models.Model):
    links = models.TextField()


class VisitedDomain(models.Model):
    domains = models.TextField()
