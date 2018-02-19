from django.db import models

class Search(models.Model):
    From=models.CharField(max_length=200)
    To=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    def __str__(self):
        return str(self.To)+' '+str(self.From)+' '+str(self.date)

class Bus(models.Model):
    bus_name=models.CharField(max_length=250)
    bus_type=models.CharField(max_length=200)
    dep_time=models.CharField(max_length=10)
    arr_time=models.CharField(max_length=10)
    travel_time=models.CharField(max_length=50)
    ratings=models.CharField(max_length=200)
    seats=models.CharField(max_length=10)
    price=models.CharField(max_length=200)

    def __str__(self):
        return self.bus_name+' '+self.bus_type+' '+self.dep_time+' '+self.arr_time+' '+self.travel_time+' '+self.ratings+' '+self.seats+' '+self.price

    
class Cost(models.Model):
    From_city=models.CharField(max_length=250)
    To_city=models.CharField(max_length=250)
    Price=models.CharField(max_length=6)

    def __str__(self):
        return str(self.From_city)+' '+str(self.To_city)+' '+str(self.Price)