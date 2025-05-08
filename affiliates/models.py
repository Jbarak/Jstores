from django.db import models

class AffiliateLink(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    image = models.ImageField(upload_to='affiliates/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
