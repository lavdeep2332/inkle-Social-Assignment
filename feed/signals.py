from django.db.models.signals import post_save
from django.dispatch import receiver
from content.models import Post, Like
from social.models import Follow
from .models import Activity

@receiver(post_save, sender=Post)
def activity_post(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(actor=instance.author, verb="posted", target=instance)

@receiver(post_save, sender=Like)
def activity_like(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(actor=instance.user, verb="liked", target=instance.post)

@receiver(post_save, sender=Follow)
def activity_follow(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(actor=instance.follower, verb="followed", target=instance.following)