from django.contrib.auth.models import User
from django.db import models
# const
SHORT_TEXT_LEN=1000
# Create your models here. Здесь можно создавать модели
class Article(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    user=models.ForeignKey(User)
    date=models. DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_short_text(self):
        # если длина текста больше 1000, то обрезаем, а если нет - возвращаем как есть
        if len(self.text)>SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text