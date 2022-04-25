from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"

    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        unique=True,
    )
    username = models.CharField(
        verbose_name="Имя пользователя", max_length=150, null=True, unique=True
    )
    role = models.CharField(
        verbose_name="Роль",
        max_length=50,
        choices=[
            (ADMIN, "Administrator"),
            (MODERATOR, "Moderator"),
            (USER, "User"),
        ],
        default=USER,
    )
    bio = models.TextField(verbose_name="О себе", null=True, blank=True)

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.is_superuser or (self.role == self.ADMIN)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact="me"),
                name="username_is_not_me",
            )
        ]
