from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import TimeField
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from datetime import date
from tags.models import Tag
# from project_tag.models import ProjectTag

# Create your models here.


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, phone, birth_date, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            birth_date = birth_date,
            # photo = photo
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, phone, birth_date, **extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, phone, birth_date, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, phone ,birth_date, **extra_fields):
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, phone, birth_date, **extra_fields)

AUTH_PROVIDERS = {'facebook': 'facebook', 'email': 'email'}

class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, validators=[RegexValidator(r'^01[012]\d{8}$')])
    address = models.CharField( max_length=250)
    photo = models.ImageField(upload_to='images/user',default='images/user/default.jpg',blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    country = models.CharField(max_length=225)
    facebook = models.URLField(null=True, blank=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "phone","birth_date","photo"]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    target_money = models.DecimalField(max_digits=10, decimal_places=2)
    hidden = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_projects")
    rates = models.ManyToManyField(User, through="Rate")
    tages = models.ManyToManyField(Tag, related_name="tagProject")


class ImportantProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Rate(models.Model):
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="allrate")



    def __str__(self):
        return f'{self.tag} - {self.project}'


def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }