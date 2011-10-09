from django.contrib import admin
from shell.apps.api.models import Player, Reading

admin.site.register(Player,
    alphabet_filter = "lastname",
    ordering        = ['lastname', 'firstname'],
    search_fields   = ['lastname', 'firstname'],
    list_display    = ['lastname', 'firstname', 'birthday', 'height', 'weight', 'active'],
    list_filter     = ['active'],
    list_per_page   = 200,
)
admin.site.register(Reading,
    ordering        = ['date'],
    search_fields   = ['player', 'date'],
    list_display    = ['player', 'date', 'humidity', 'temperature', 'acceleration'],
    list_filter     = [],
    list_per_page   = 200,
)
