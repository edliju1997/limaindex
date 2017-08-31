from django.contrib import admin

from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):

	list_display = ['titulo', 'link', ]

admin.site.register(Portfolio, PortfolioAdmin)
