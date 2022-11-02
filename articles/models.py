from django.db import models

class ArticlesModel(models.Model):
    """Model definition for ArticlesModel."""

    name=models.CharField(max_length=100)
    content=models.TextField()


    class Meta:
        """Meta definition for ArticlesModel."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of ArticlesModel."""
        return self.name

