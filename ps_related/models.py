from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    """User plan subscriptions"""
    class Packages(models.TextChoices):
        NOVICE = "novice", "Novice"
        ELITE = "elite", "Elite"  # Lowercase, check celery task

    package = models.CharField(
        verbose_name="Plan",
        max_length=10,
        choices=Packages.choices,
        default=Packages.NOVICE  # Setting default to one of the choices
    )
    level = models.PositiveIntegerField(default=1)
    link = models.URLField(
        verbose_name="Link",
        unique=True,
        editable=False,
        null=True,
        blank=True  # Allowing blank values in forms
    )
    commission = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        editable=False,
        default=0.00
    )
    referrals = models.ManyToManyField(
        "Account",
        related_name="invites"
    )
    is_paid = models.BooleanField(
        verbose_name="Account Validity",
        default=True,
        blank=True
    )

    def __str__(self):
        return self.package


class Account(models.Model):
    """Registered user accounts"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="account"
    )
    plan = models.ManyToManyField(
        Plan,
        related_name="subscriptions",  # Renaming to 'subscriptions' for clarity
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s account"


class Blog(models.Model):
    """Blog model"""
    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # Ensuring slug is unique
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add for creation time

    def __str__(self):
        return self.title


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(in_stock=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    in_stock = models.BooleanField()
    objects = BookManager()


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.name