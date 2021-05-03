from django.contrib import admin

from .models import Question

# add models
admin.site.register(Question)
