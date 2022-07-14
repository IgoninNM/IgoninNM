from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Year(models.Model):
    date = models.DateField('date of event')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Года"

    def __str__(self):
        return f"{self.date:%Y}"


class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    article = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.title} {self.year.date:%Y}"
