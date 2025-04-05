from django.contrib import admin
from .models import Profile, Transaction, Category


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'patrimonio_inicial', 'dinero_actual')  # Agrega 'dinero_actual'

    def dinero_actual(self, obj):
        return obj.dinero_actual  # Llama a la propiedad 'dinero_actual' del modelo

    def transacciones(self, obj):
        # Agrega un enlace a las transacciones de este usuario
        return f'<a href="/admin/finance/transaction/?user={obj.user.id}">Ver Transacciones</a>'
    transacciones.allow_tags = True  # Esto permite que el enlace sea HTML
    transacciones.short_description = 'Transacciones'

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Transaction)
admin.site.register(Category)