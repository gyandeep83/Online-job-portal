from django.db import models

class signup(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    class Meta:
        db_table="signup"
        

class IT_Companies(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    imagepath=models.CharField(max_length=200)
    
    class Meta:
        db_table="IT_Companies"
    
    
class JobDescription(models.Model):
    desc_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=255)
    company = models.ForeignKey(IT_Companies, on_delete=models.CASCADE)
    job_description = models.TextField()
    job_location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    years_of_experience = models.IntegerField()
    skills = models.CharField(max_length=255)
    
    class Meta:
        db_table = "JobDescription"


    def __str__(self):
        return self.job_title


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback_text = models.TextField()
    date=models.DateField()
    
    class Meta:
        db_table = "Feedback"


    def __str__(self):
        return f"Feedback from User ID {self.user.user_id}"
    
class JobApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "JobApplication"

    def __str__(self):
        return f"Application for {self.job.job_title} at {self.job.company.company_name}"
    
class ContactDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100, blank=True)
    domain = models.CharField(max_length=100)
    goals = models.TextField()
    
    class Meta:
        db_table = "ContactDetails"

