from django.db import models

class Post (models.Model):

    title = models.CharField("Заголовок", max_length=100)
    url = models.CharField("URL", max_length=100)
    created = models.DateTimeField("Дата создания", auto_now=True)


