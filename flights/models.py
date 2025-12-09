from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название страны")
    flag_url = models.URLField(verbose_name="Ссылка на флаг")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Flight(models.Model):
    departure_country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='departures',
        verbose_name="Откуда"
    )
    arrival_country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='arrivals',
        verbose_name="Куда"
    )

    date = models.DateField(verbose_name="Дата вылета")

    # 🔥 Новые поля
    departure_time = models.TimeField(verbose_name="Время вылета", default="10:00")
    arrival_time = models.TimeField(verbose_name="Время прилёта", default="12:00")

    def __str__(self):
        return f"{self.departure_country} -> {self.arrival_country} ({self.date})"

    class Meta:
        verbose_name = "Перелёт"
        verbose_name_plural = "Перелёты"
