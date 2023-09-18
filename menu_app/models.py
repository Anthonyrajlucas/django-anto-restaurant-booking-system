from django.db import models

class MenuItem(models.Model):
      menu_id = models.AutoField(primary_key=True)
      menu_name = models.CharField(max_length=100)
      description = models.TextField()
      category = models.CharField(max_length=50)
      price = models.DecimalField(max_digits=8, decimal_places=2)
      image_url = models.URLField()
      
      def __str__(self):
          return self.menu_name
