from django.db import models


class Articles(models.Model):

    title = models.CharField('Название', max_length=50)  # Заголовок
    anons = models.CharField('Дисклеймер', max_length=250)  # Хз, типо краткого содержания
    news_text = models.TextField('Сам текст')  # Текст самого сайта
    date = models.DateTimeField('Дата публикации')  # Время и дата, когда новости появились
    image = models.ImageField(upload_to='articles_image', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
