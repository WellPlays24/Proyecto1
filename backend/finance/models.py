from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patrimonio_inicial = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_inicio = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    @property
    def dinero_actual(self):
        # Obtiene todas las transacciones relacionadas con el usuario
        ingresos = Transaction.objects.filter(user=self.user, type=Transaction.INCOME).aggregate(total=models.Sum('amount'))['total'] or 0
        egresos = Transaction.objects.filter(user=self.user, type=Transaction.EXPENSE).aggregate(total=models.Sum('amount'))['total'] or 0
        # Calcula el dinero actual sumando el patrimonio inicial y los ingresos/egresos
        return self.patrimonio_inicial + ingresos - egresos

    @property
    def transacciones(self):
        # Devuelve todas las transacciones del usuario
        return Transaction.objects.filter(user=self.user)

    
class Transaction(models.Model):
    INCOME = 'ingreso'
    EXPENSE = 'egreso'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Ingreso'),
        (EXPENSE, 'Egreso'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.amount} ({self.date})"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name    


