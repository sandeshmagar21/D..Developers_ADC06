from django.db import models
class Gym(models.Model):
    workoutname = models.CharField(max_length = 50) 
    picture = models.FileField(upload_to='imagee/pdf')
    email = models.EmailField(blank = False) 
    workoutdesc = models.TextField(blank=False)
    def __str__(self):
        return self.workoutname

    def uploadata_fields_blank(self):
        return(self.workoutname != False)

    def TestWorkout(self):
        return (len(self.workoutname) >= 3) and (len(self.workoutname) <= 50) 
       
    def email_fiewlds_blank(self):
        return (self.email != False)
 
    def workoutdes_field_blank(self):
        return (self.workoutdesc != True ) and (len(self.workoutdesc) <= 50)



class FeedBack(models.Model):
    username = models.CharField(max_length = 45, null = True)
    email = models.EmailField(max_length = 45, null = True)
    def __str__(self):
        return self.username


class Trainer(models.Model):
    fname = models.CharField(max_length = 45,null = True)
    lname = models.CharField(max_length = 45, null = True)
    username = models.CharField(max_length = 45, null = True)
    email = models.EmailField(max_length = 45, null = True)
    def __str__(self):
        return self.fname



class abc(models.Model):
    coursetitle = models.CharField(max_length = 45,null = True)
    coursetype = models.CharField(max_length = 45,null = True)
    coursefull = models.FileField()
    coursedesc = models.CharField(max_length = 500,null = True)
    trainer = models.ForeignKey(Trainer, null = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.coursetitle

class Members(models.Model):
    username = models.CharField(max_length = 45, blank= False)
    email = models.EmailField(max_length = 45, blank= False)
    contact = models.IntegerField(blank= False)
    course = models.ManyToManyField(abc)
    def __str__(self):
        return self.username
   
class Work(models.Model):
    Members = models.ForeignKey(Members, on_delete=models.CASCADE)
    course = models.ForeignKey(abc, on_delete=models.CASCADE)

class Payment(models.Model):
    pay_fname = models.CharField(max_length = 45,null = False)
    pay_lname = models.CharField(max_length = 45,null= False)
    pay_account_number = models.IntegerField(null= False)
    pay_choices = [
        ('PA', 'PAYPAL'),
        ('MC', 'MASTERCARD'),
        ('ES','eSEWA'),
        ]
    pay_choices_store = models.CharField(max_length=20, choices=pay_choices)    
    pay_date = models.DateTimeField(null= False)
    members = models.ForeignKey(Members, null = True, on_delete = models.CASCADE)
    course = models.ForeignKey(abc, null = True, on_delete = models.CASCADE)


class Contat(models.Model):
    Name = models.CharField(max_length=45, null=False)
    Email = models.EmailField(max_length=45, blank = False)
    Description = models.TextField(blank = False)