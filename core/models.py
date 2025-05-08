from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default='JStores')
    site_description = models.TextField('Discover top digital products and trusted affiliate deals at JBStores—tools, courses, and resources to boost your digital life and business.')
    contact_email = models.EmailField('barakajotieno@gmail.com')
    contact_phone = models.CharField(max_length=20)
    social_media_links = models.JSONField(default=dict)

    def __str__(self):
        return self.site_name