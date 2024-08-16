from django.db import models

years=[
    (2024,2024),
    (2025,2025),
    (2026,2026)
]
grades=[
    (1,1),
    (2,2),
    (3,3),
    (4,4)
]

holiday=[
    ('April Holiday','April Holiday'),
    ('August Holiday','August Holiday'),
    ('December Holiday','December Holiday')
]

offices=[('CHIEF PRINCIPAL','CHIEF PRINCIPAL'),
        ('DEPUTY PRINCIPAL(ADMIN)','DEPUTY PRINCIPAL(ADMIN)'),
        ('DEPUTY PRINCIPAL(ACAD)','DEPUTY PRINCIPAL(ACAD)'),
        ('DEAN','DEAN'),
        ('HOD MATHEMATICS','HOD MATHEMATICS'),
        ('HOD SCIENCE','HOD SCIENCE'),
        ('HOD ENGLISH','HOD ENGLISH'),
        ('HOD KISWAHILI','HOD KISWAHILI'), 
        ('HOD HUMANITIES','HOD HUMANITIES'),
        ('HOD TECHNICALS','HOD TECHNICALS'),
        ('HOD G&C','HOD G&C'),
        ('HOD CAREERS','HOD CAREERS'),
        ('HOD SPORTS','HOD SPORTS'),
        ('HOS','HOS')]

gender=[('Mr', 'Mr'), 
        ('Mrs', 'Mrs'), 
        ('Ms', 'Ms')]

subjects=[
    ('BIO & CHEM','BIO & CHEM'),
    ('PHYS & CHEM','PHY & CHEM'),
    ('MATH & PHY','MATH & PHY'),
    ('MATH & CHEM','MATH & CHEM'),
    ('HIS & CRE','HIS & CRE'),
    ('GEO & HIS','GEO & HIS'),
    ('HIS & KIS','HIS & KIS'),
    ('KIS & CRE','KIS & CRE'),
    ('ENG/LIT','ENG/LIT'),
    ('MATH/COMP','MATH/COMP'),
    ('MATH/BUS','MATH/BUS'),
    ('HSC/BIO','HSC/BIO'),
    ('MATH/GEO','MATH/GEO'),
    ('HIS/P.E','HIS/P.E')
]

subjects_t=[
    ('MATHEMATICS','MATHEMATICS'),
    ('ENGLISH','ENGLISH'),
    ('KISWAHILI','KISWAHILI'),
    ('CHEMISTRY','CHEMISTRY'),
    ('PHYSICS','PHYSICS'),
    ('BIOLOGY','BIOLOGY'),
    ('BUSINESS STUDIES','BUSINESS STUDIES'),
    ('COMPUTER STUDIES','COMPUTER STUDIES'),
    ('AGRICULTURE','AGRICULTURE'),
    ('HOME SCIENCE','HOME SCIENCE'),
    ('HISTORY','HISTORY'),
    ('GEOGRAPHY','GEOGRAPHY'),
    ('CRE','CRE')
]
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
 
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    mynews = models.FileField(upload_to='news_info/',null=True,blank=True)
    
    class Meta: 
        verbose_name = ("News")
        verbose_name_plural = ("News")

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

class About(models.Model):
    history = models.TextField(help_text="Enter each point on a new line")
    population = models.IntegerField()
    school_motto = models.CharField(max_length=200)
    vision = models.TextField()
    mission = models.TextField()
    subjects_offered = models.TextField(help_text="Enter each subject on a new line")
    clubs_and_societies = models.TextField(help_text="Enter each club/society on a new line")
    contact_information = models.TextField()
    email = models.EmailField()
    class Meta:
        verbose_name = ("about")
        verbose_name_plural = ("about")

class Administrator(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=10,choices=gender)
    photo = models.ImageField(upload_to='admin_photos/')
    order = models.IntegerField(default=0)
    role = models.CharField(max_length=100, blank=True, choices=offices)
    subjects = models.CharField(max_length=200, blank=True ,choices=subjects)

class TeachingStaff(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=10, choices=gender)
    role = models.CharField(max_length=100, blank=True, choices=offices)
    subjects = models.CharField(max_length=200,choices=subjects)
    photo = models.ImageField(upload_to='staff_photos/')
    order = models.IntegerField(default=0)    

class Achievement(models.Model):
    year = models.IntegerField()
    university_admission_rate = models.FloatField()

class CoCurricularAward(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='award_photos/')

class HolidayAssignment(models.Model):
    year = models.IntegerField(default=2024, choices=years)
    title = models.CharField(max_length=200, choices=holiday)
    grade = models.IntegerField(default=1, choices=grades)
    subject = models.CharField(max_length=20,choices=subjects_t)  # New field for subject
    file = models.FileField(upload_to='assignments/')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    author=models.CharField(max_length=15,default='ADMIN')

    def __str__(self):
        return f"{self.title} - Grade {self.grade} - {self.subject}"
 
class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='background_images/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order'] 

    def __str__(self):
        return f"Background Image {self.order}"
