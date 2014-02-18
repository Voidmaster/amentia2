import datetime

from django.db import models
from django.contrib.auth.models import User

class CommonInfo(models.Model):
    """
    Abstract class that represents name and description
    in most models.
    """

    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150)

    class Meta:
        abstract = True

class CommonPriority(models.Model):
    """
    Abstract class that represents different types
    of priority.
    """

    HIGH_PRIORITY = 0
    MEDIUM_PRIORITY = 1
    LOW_PRIORITY = 2

    PRIORITY_CHOICES = (
        (HIGH_PRIORITY, "Prioridad alta"),
        (MEDIUM_PRIORITY, "Prioridad media"),
        (LOW_PRIORITY, "Prioridad baja"),
    )

    priority = models.IntegerField(default=0, choices=PRIORITY_CHOICES)

    class Meta:
        abstract = True

class Category(CommonInfo):
    """
    Represents a category for each service.
    """

    class Meta:
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.name

class Service(CommonInfo):
    """
    Represents a service we offer to a client.
    """

    category = models.ForeignKey(Category, unique=True)

    class Meta:
        verbose_name_plural = "Servicios"

    def __unicode__(self):
        return self.name

class Client(CommonInfo, CommonPriority):
    """
    Represents a client who adquires one or more services.
    """

    is_active = models.BooleanField(default=True)
    service = models.ForeignKey(Service)

    image = models.FileField(upload_to="/media/", blank=True)

    class Meta:
        verbose_name_plural = "Clientes"

    def __unicode__(self):
        return "%s" % self.name

class Work(CommonInfo, CommonPriority):
    """
    Represents a type of work based on a client need.
    """

    HIGH_COMPLEXITY = 0
    MEDIUM_COMPLEXITY = 1
    LOW_COMPLEXITY = 2

    COMPLEXITY_CHOICES = (
        (HIGH_COMPLEXITY, "Complejidad alta"),
        (MEDIUM_COMPLEXITY, "Complejidad media"),
        (LOW_COMPLEXITY, "Complejidad baja"),
    )

    init_date = models.DateTimeField(auto_now_add=True)
    final_date = models.DateTimeField()
    price = models.IntegerField()

    complexity = models.IntegerField(choices=COMPLEXITY_CHOICES)
    workers = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = "Trabajos"

    def __unicode__(self):
        return self.name

