# Generated by Django 5.1.1 on 2024-09-18 12:30

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=255, verbose_name='feature')),
                ('img', models.ImageField(upload_to='', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='game name')),
                ('price', models.IntegerField(verbose_name='game price')),
                ('discount', models.IntegerField(default=0, verbose_name='price discount')),
                ('trending', models.BooleanField(verbose_name='trending')),
                ('most_played', models.BooleanField(verbose_name='most played')),
                ('img', models.ImageField(upload_to='', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genre', models.CharField(max_length=64, verbose_name='Genre')),
                ('top_category', models.BooleanField(verbose_name='top category')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(max_length=64, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='WelcomeText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome', models.CharField(max_length=255, null=True, verbose_name='welcome')),
                ('about', models.CharField(max_length=255, null=True, verbose_name='about')),
                ('details', models.TextField(null=True, verbose_name='details')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('img', models.ImageField(default='media/featured-02.png', upload_to='', verbose_name='image')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('shopping_cart', models.ManyToManyField(blank=True, related_name='cart', to='main.game')),
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
        migrations.AddField(
            model_name='game',
            name='GameGenre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Genres', to='main.genres'),
        ),
        migrations.CreateModel(
            name='GameDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_ident', models.CharField(max_length=64, verbose_name='game_id')),
                ('name', models.CharField(max_length=64, verbose_name='game name')),
                ('about', models.TextField(verbose_name='about the game')),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='game_name', to='main.game')),
                ('genres', models.ManyToManyField(related_name='genres', to='main.genres')),
                ('tags', models.ManyToManyField(related_name='tags', to='main.tags')),
            ],
            options={
                'verbose_name': 'Game Details',
                'verbose_name_plural': 'Game Details',
            },
        ),
    ]
