from django.db import models

# Create your models here.

class razorpay_table(models.Model):
    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(max_length=200, default='')
    razorpay_signature = models.CharField(max_length=200, default='')
 
   

