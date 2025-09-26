from django.db import models

# Create your models here.


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # description = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Registers(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	username=models.CharField(max_length=30)
	mobile=models.CharField(max_length=10)
	email=models.EmailField(max_length=30)

	def _str_(self):
		return self.name+" "+self.email 



class Feedback(models.Model):
    customer_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    food_rating = models.IntegerField()
    delivery_rating = models.IntegerField()
    comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.customer_name or 'Anonymous'}"

class Order(models.Model):
    item=models.IntegerField()
    add=models.TextField(blank=True)

    def __str__(self):
        return str(self.item)+" "+self.add
