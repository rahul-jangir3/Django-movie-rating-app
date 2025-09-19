from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # 0.0 - 10.0 typical
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.rating})"

