from django.db import models



class Category(models.Model):
     name= models.CharField(max_length=255, verbose_name="Categoriya nomi")
     created_at = models.DateField(blank=False)


     def __str__(self):
         return self.name

     class Meta:
          verbose_name = "Kategoriya"


class Author(models.Model):
      full_name = models.CharField(max_length=200, verbose_name="Author ismi")
      bio = models.TextField(verbose_name="Yozuvchi haqida")
      image= models.ImageField(upload_to='img/', verbose_name="Rasm")
      created_at = models.DateField(blank=False)


      def __str__(self):
          return self.full_name


      class Meta:
          verbose_name= "Yozuvchi"


class Book(models.Model):
      name  = models.CharField(max_length=399, verbose_name="Kitob nomi")
      body = models.TextField(verbose_name="Kitob haqida")
      price = models.CharField(max_length=20, verbose_name="Kitob narxi")
      image = models.ImageField(upload_to='book/', verbose_name="Kitob rasmi")
      category = models.ForeignKey(Category, on_delete=models.CASCADE)
      author = models.ForeignKey(Author, on_delete=models.CASCADE)
      created_at  = models.DateField(blank=False)


      def __str__(self):
          return self.name


      class Meta:
          verbose_name = "Kitob_"
