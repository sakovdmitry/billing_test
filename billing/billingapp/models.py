from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Organization(models.Model):
    client_name = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='organization'
        )
    name = models.CharField(max_length=200)
    address = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['client_name', 'name'],
                name='unique_name_client'
            )
        ]


class Bills(models.Model):
    client_name = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='bills'
    )
    client_org = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='organization'
    )
    number = models.SmallIntegerField()
    sum = models.FloatField()
    date = models.DateField()
    fraud_score = models.FloatField()
    service_class = models.SmallIntegerField()
    service_name = models.CharField(max_length=150)
