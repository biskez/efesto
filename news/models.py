from django.db import models

class News(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='assets/images/news')
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255, default=None)
    short_description = models.TextField()
    description = models.TextField()
    display = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']