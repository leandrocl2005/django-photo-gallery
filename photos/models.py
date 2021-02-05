from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"

    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name_plural = "Fotos"
        verbose_name = "Foto"

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description