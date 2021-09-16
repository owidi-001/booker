from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone, national_id, password=None):
        """
        Creates and saves a User with the given first_name, last_name, email, phone, national_id and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not national_id or len(national_id) > 8:
            raise ValueError('Invalid ID number')

        if not phone:
            raise ValueError('Invalid phone number')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            phone=phone,
            national_id=national_id
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone, national_id, password=None):
        """
        Creates and saves a superuser with the given first_name, last_name, email, phone, national_id and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            email,
            phone,
            national_id,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staff(self, first_name, last_name, email, phone, national_id, password=None):
        """
        Creates and saves staff with the given first_name, last_name, email, phone, national_id and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            email,
            phone,
            national_id,
            password=password,
        )
        user.is_admin = False
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=13)
    national_id = models.CharField(max_length=8)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'national_id']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


# Create your models here.
class Passenger(MyUser):

    def __str__(self):
        return f'Email: {self.email} Phone: {self.phone} ID: {self.national_id}'

    def get_fullnames(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Driver(MyUser):
    staff_id = models.CharField(max_length=20, unique=True, default=None, blank=False, null=False)
    is_staff = True

    def __str__(self):
        return f'Email: {self.email} Phone: {self.phone} ID: {self.national_id}'

    def get_fullnames(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    capacity = models.DecimalField(decimal_places=0, max_digits=2)
    booked = models.DecimalField(decimal_places=0, max_digits=2)
    is_full = models.BooleanField(default=False)
    routes = models.TextField()
    rates = models.FloatField(default=1.00)

    def __str__(self):
        return self.bus_name

    def full_capacity(self):
        if self.booked == self.capacity:
            self.is_full = True
        return self.is_full


class Routes(models.Model):
    FROM_ROUTES = (
        ('nairobi', 'Nairobi'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('eldoret', 'Eldoret'),
        ('Mombasa', 'Mombasa'),
        ('kisii', 'Kisii'),
    )
    TO_ROUTES = (
        ('nairobi', 'Nairobi'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('eldoret', 'Eldoret'),
        ('Mombasa', 'Mombasa'),
        ('kisii', 'Kisii'),
    )
    source = models.CharField(max_length=20, choices=FROM_ROUTES)
    destination = models.CharField(max_length=20, choices=TO_ROUTES)
    cost = models.FloatField()


class Booking(models.Model):
    INACTIVE = 'I'
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((INACTIVE, 'Waiting Confirmation'),
                       (BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       )
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT)
    route = models.ForeignKey(Routes, on_delete=models.PROTECT)
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT)
    cost = models.FloatField()
    payment_id = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=INACTIVE, max_length=2)

    def print_ticket(self):
        pass

    def total_cost(self):
        self.cost = self.bus.rates * self.route.cost
        return self.cost
