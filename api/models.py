from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.




class Blog(models.Model):

    CONDITION_TYPE=(
        ('WORLD','world'),
        ('ENVIORNMENT','environment'),
        ('TECHNOLOGY','technology'),
        ('DESIGN','design'),
        ('CULTURE','culture'),
        ('BUSINESS','business'),
        ('POLITICS','politics'),
        ('OPINION','opinion'),
        ('SCIENCE','science'),
        ('HEALTH','health'),
        ('STYLE','style'),
        ('TRAVEL','travel')
    )

    title = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=1500,null=True)
    category=models.CharField(max_length=50,choices=CONDITION_TYPE,default=CONDITION_TYPE[0])
    slug=models.SlugField()
    excrpt=models.CharField(max_length=150)
    image =models.ImageField(upload_to='images',null=True)
    month =models.CharField(max_length=3,null=True)
    day =models.CharField(max_length=3,default=timezone.now())
    date_created = models.DateTimeField(auto_now_add=True)
    featured=models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        original_slug=slugify(self.title)
        queryset=Blog.objects.all().filter(slug__iexact=original_slug).count()

        count =1
        slug=original_slug
        while(queryset):
            slug= original_slug + '-' + str(count)
            count +=1
            queryset=Blog.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = Blog.objects.get(featured=True)
                if self !=temp:
                    temp.featured= False
                    temp.save()
            except Blog.DoesNotExist:
                pass

        super(Blog,self).save(*args,**kwargs)

    def __str__(self):
        return self.title
