from django.db import models

class Content1(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user = models.CharField(max_length=255, blank=True, null=True)
    attitude = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    reposts = models.CharField(max_length=255, blank=True, null=True)
    creates = models.CharField(max_length=255, blank=True, null=True)
    crawl = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content1'
        indexes = [
            models.Index(
                fields=['user'],
                name='userIndex',
            )
        ]


class Weibo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    follow = models.CharField(max_length=255)
    fans = models.CharField(max_length=255, blank=True, null=True)
    weibos = models.CharField(max_length=255, blank=True, null=True)
    loc = models.CharField(max_length=255, blank=True, null=True)
    verified_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weibo'
