from django.db import models

class PortfolioAdmin(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | \
			models.Q(description__icontains=query)
)

class Portfolio(models.Model):
	titulo = models.CharField('Título', max_length=100)
	link = models.CharField('Link', max_length=200)
	imagem = models.ImageField('imagem', null=True)

	objects = PortfolioAdmin()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'portfólio'
		verbose_name_plural = 'portfólios'
