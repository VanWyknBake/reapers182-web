from django.db import models


# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career





class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

    

# PORTFOLIO SECTION

class Portfolio(models.Model):
    title = models.CharField(default='Team Name' ,max_length=50)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    captain = models.CharField(default='Captain', max_length=50)
    member1 = models.CharField(default='Member', max_length=50)
    member2 = models.CharField(default='Member', max_length=50)
    member3 = models.CharField(default='Member', max_length=50)
    member4 = models.CharField(default='Member', max_length=50)
    member5 = models.CharField(default='Member', max_length=50)
    member6 = models.CharField(default='Member', max_length=50)
    
    
   

    def __str__(self):
        return self.title





class Books(models.Model):
    image = models.ImageField(upload_to='books/')
    link = models.URLField(max_length=200)
    player = models.CharField(default='Screenshot', max_length=50)
    
    


    def __str__(self):
        return f'Snap {self.id}'

class News(models.Model):
    topic = models.CharField(max_length=50)
    desc = models.CharField(max_length=440)
    image = models.ImageField(upload_to='news/', blank=True)
    author = models.CharField(default='author' ,max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic
    


