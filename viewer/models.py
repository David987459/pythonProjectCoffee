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
    favorite = models.ManyToManyField('Products', related_name='Users', blank=True)

    def __str__(self):
        return (f'{self.user_id}, {self.name}, {self.surname}, {self.city}, {self.street}, {self.pcs},'
                f' {self.reg_date}, {self.status}, {self.favorite}')


class Ratings(models.Model):
    reg_user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    stars = models.ImageField(upload_to='rating_stars/')
    rating = models.IntegerField()
    rate_date = models.DateField()

    def __str__(self):
        return f'{self.reg_user_id}, {self.id}, {self.stars}, {self.rate_date}, {self.rating}'


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
        return f'{self.product_id}, {self.id}, {self.price}, {self.prod_name}, {self.prod_view}, {self.in_stock}, {self.origin}, {self.category}, {self.type_prod}'


class Orders(models.Model):
    order_date = models.DateField()
    user_id = models.ManyToManyField('Users', related_name='Orders', blank=True)
    order_price = models.IntegerField()
    bin_id = models.ForeignKey('Basket', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id}, {self.id}, {self.order_price}'


class Basket(models.Model):

    prd_id = models.IntegerField()
    num_prod = models.IntegerField()
    order_price = models.IntegerField()

    def __str__(self):
        return f'{self.prd_id}, {self.num_prod}, {self.order_price}'


class Origin(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.country_id}, {self.country_name}'


class Coffee(models.Model):
    coffee_id = models.IntegerField(primary_key=True)
    coffee_type = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.coffee_id}, {self.coffee_type}'

