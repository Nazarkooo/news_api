from django.db import models


class NewsType(models.Model):
    COLORS = (
        ('RED', 'RED'),
        ('BLUE', 'BLUE'),
        ('GREEN', 'GREEN'),
        ('PINK', 'PINK'),
        ('WHITE', 'WHITE'),
        ('BLACK', 'BLACK'),
    )
    
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=200, choices=COLORS)
    
    class Meta:
        verbose_name_plural = "News Types"
    
    def __str__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=250)
    description = models.TextField()
    news_type = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "News Items"
    
    def __str__(self):
        return self.title
    




