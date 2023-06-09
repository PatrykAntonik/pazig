from django.urls import reverse
from django.conf import settings
import markdown
from grupy.models import *
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = markdown.markdown(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'posty:single',
            kwargs={
                'username': self.user.username,
                'pk': self.pk
            }
        )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']