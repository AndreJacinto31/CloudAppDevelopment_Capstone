from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model 
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=25)
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name

# <HINT> Create a Car Model
class CarModel(models.Model):
    TYPES = (
        ("SEDAN","Sedan"), ("SUV", "Suv"), ("WAGON", "Wagon"), ("COUPÉ","Coupé")
    )

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    car_type = models.CharField(max_length=30, choices=TYPES)
    dealer_id = models.IntegerField()
    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + \
                " Make Name: "+ self.make.name + \
                " Type: " + self.car_type + \
                " Dealer ID: " + str(self.dealer_id)+ \
                " Year: " + str(self.year) 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
