from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Year(models.Model):
    date = models.DateTimeField('date of event')

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Года"

    def __str__(self):
        return f"{self.date:%Y}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.title} {self.year.date:%Y}"
