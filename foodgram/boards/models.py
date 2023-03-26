from django.db import models
from accounts.models import Users


class Products(models.Model):    
    picture = models.FileField(upload_to='product_pictures/%Y/%m/%d', blank =True, null=True)
    store_name = models.CharField(max_length=1000)
    kinds = models.CharField(max_length=1000, blank =True, null=True)
    zip_code = models.CharField(max_length=8, blank =True, null=True)
    place_prefecture = models.CharField(max_length=1000, blank =True, null=True)
    place_another = models.CharField(max_length=1000, blank =True, null=True)
    comments = models.CharField(max_length=1000, blank =True, null=True)
    main_comments = models.CharField(max_length=1000, blank =True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )
    
    class Meta:
        db_table = 'products'
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.store_name

