from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import TimeField
from django.core.validators import MinValueValidator, MaxValueValidator

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

class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.CharField( max_length=250)
    photo = models.ImageField(upload_to='images/user',default='images/user/default.jpg',blank=True)
    birth_date = models.DateField()
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "birth_date"]

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    rates = models.ManyToManyField(User, through="Rate")


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
