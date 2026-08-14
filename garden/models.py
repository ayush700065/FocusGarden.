from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["completed", "-created_at"]

    def __str__(self):
        return self.title
