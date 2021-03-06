# Generated by Django 3.1.1 on 2020-10-27 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture', models.ImageField(default='default_post.jpg', upload_to='blog_pics')),
                ('Views', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('ReadDuration', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('comms_number', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('DownVotes', models.ManyToManyField(related_name='blog_posts_downvote', to=settings.AUTH_USER_MODEL)),
                ('UpVotes', models.ManyToManyField(related_name='blog_posts_upvote', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('comm_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('comm_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
