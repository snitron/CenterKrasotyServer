from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    geo_coords = models.CharField(max_length=50)
    st_time = models.CharField(max_length=40, default="08:00")
    fin_time = models.CharField(max_length=40, default="18:00")

    def __str__(self):
        return self.name


class ServiceGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30)
    info = models.TextField(default=".")
    price = models.FloatField(default=0.0)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, default=None)
    long = models.IntegerField(default=60)

    def __str__(self):
        return self.name


class Place(models.Model):
    info = models.TextField()
    group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="usr/share/django-projects/welcome/static/images/")

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    phone = models.CharField(max_length=20, default="0")
    date = models.CharField(max_length=15)
    start_time = models.CharField(max_length=30, default="0")
    finish_time = models.CharField(max_length=30, default="0")
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, default=1)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id)

# mysql --host=rc1a-wv9mkrd32hl1ga09.mdb.yandexcloud.net --ssl-ca=~/.mysql/root.crt --user=nitron --password=centerkrasoty db1 -e "DESCRIBE make_order_place" --force
