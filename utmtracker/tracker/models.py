from django.db import models

class UtmData(models.Model):
    utm_medium = models.CharField(max_length=255)
    utm_source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"UTM Data: Medium={self.utm_medium}, Source={self.utm_source}"

