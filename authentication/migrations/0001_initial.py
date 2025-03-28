# Generated by Django 5.1.7 on 2025-03-24 08:10

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.gis.db.models.fields
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the role.', max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='Role name must be at least 3 characters.')])),
                ('description', models.TextField(blank=True, help_text='Description of the role.', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the role was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the role was last updated.')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')])),
                ('phone_number', models.CharField(blank=True, help_text="User's phone number in international format.", max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number in international format (e.g., +123456789).', regex='^\\+?[1-9]\\d{1,14}$')])),
                ('is_guest', models.BooleanField(default=False, help_text='Indicates if the user is a guest.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the user was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the user was last updated.')),
                ('activated_profile', models.BooleanField(blank=True, default=None, help_text='Indicates if the user has activated their profile.', null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_users', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_users', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, help_text='Unique verification token for the user.', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the verification token was created.')),
                ('expires_at', models.DateTimeField(help_text='Timestamp when the verification token expires.')),
                ('used', models.BooleanField(default=False, help_text='Indicates whether the verification token has been used.')),
                ('user', models.OneToOneField(help_text='The user associated with this verification record.', on_delete=django.db.models.deletion.CASCADE, related_name='verification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', models.JSONField(blank=True, help_text='User preferences stored as a JSON object (e.g., categories of interest).', null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Geographic location of the user (latitude and longitude).', null=True, srid=4326)),
                ('profile_image', models.ImageField(blank=True, help_text='Profile image for the user.', null=True, upload_to='profile_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the profile was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the profile was last updated.')),
                ('user', models.OneToOneField(help_text='The user associated with this profile.', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-created_at'],
            },
        ),
    ]
