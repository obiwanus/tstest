from django.db import models


class ApiRequests(models.Model):
    api_endpoint = models.CharField(max_length=255)
    http_method = models.CharField(max_length=10, default='')
    response_ms = models.IntegerField(default=0)
    status_code = models.IntegerField(default=200)
    received = models.DateTimeField(auto_now_add=True)


class StatusCodes(models.Model):
    status_code = models.IntegerField(default=200)
    description = models.TextField()