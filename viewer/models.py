from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    street = models.CharField(max_length=75)
    pcs = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    test = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id


class Ratings(models.Model):
    reg_user_id = models.IntegerField()
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    starts = models.ImageField(upload_to='rating_stars/')
    rating = models.IntegerField()
    pcs = models.IntegerField()
    rate_date = models.DateField()

    def __str__(self):
        return self.reg_user_id


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length=35)
    prod_view = models.ImageField(upload_to='rating_stars/')
    type_prod = models.CharField(max_length=30)
    origin = models.CharField(max_length=35)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    in_stock = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.product_id


class Orders(models.Model):
    orders_id = models.IntegerField()
    order_date = models.DateField()
    user_id = models.ManyToManyField(Users.user_id, related_name='Orders.orders_id')
    order_price = models.IntegerField()
    bin_id = models.ForeignKey('Bin.bin_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.orders_id


class Bin(models.Model):
    bin_id = models.IntegerField(primary_key=True)
    prd_id = models.IntegerField()
    num_prod = models.IntegerField()
    order_price = models.IntegerField()

    def __str__(self):
        return self.bin_id


class Origin(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=35)

    def __str__(self):
        return self.country_id


class Coffee(models.Model):
    coffee_id = models.IntegerField(primary_key=True)
    coffee_type = models.CharField(max_length=35)

    def __str__(self):
        return self.coffee_id

