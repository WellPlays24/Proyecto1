{/* 

    Task: 

    Crear un dashboard para que los usuarios puedan ver un resumen de su actividad financiera es una excelente idea, ya que proporciona una vista clara y organizada de la información más relevante para el usuario. Aquí tienes algunas funcionalidades que puedes incluir en el dashboard:

    1. Balance del Usuario:
    Mostrar el saldo actual del usuario, que es la diferencia entre sus ingresos y egresos.
    Podrías mostrar esto de manera prominente en la parte superior, como una especie de "tarjeta de resumen" (por ejemplo, "Tu saldo actual es: $500").

    2. Resumen de Transacciones:
    Mostrar un resumen de las transacciones más recientes, con la opción de ver más si el usuario lo desea.
    Podrías filtrar las transacciones entre ingresos y egresos, mostrando los totales de cada categoría.

    3. Gráficos Estadísticos:
    Incluir gráficos (por ejemplo, gráfico de barras o gráfico circular) para representar los ingresos, egresos, o incluso la distribución por categorías.
    Por ejemplo, mostrar un gráfico circular con la distribución de los ingresos y egresos por categoría (alimentación, entretenimiento, etc.).

    4. Objetivos Financieros:
    Permitir que los usuarios establezcan objetivos financieros, como ahorrar una cierta cantidad de dinero en un mes o reducir sus gastos en una categoría particular.
    En el dashboard, podrías mostrar el progreso hacia estos objetivos.

    5. Alertas o Notificaciones:
    Mostrar alertas cuando un usuario esté cerca de alcanzar un límite de gasto establecido o cuando falte poco para cumplir su objetivo financiero.

    6. Últimos Ingresos y Egresos:
    Mostrar las últimas transacciones del usuario en una lista, con detalles de cada una (monto, fecha, descripción).
    Esto puede incluir un botón para "Ver más" si hay muchas transacciones.

    7. Categorías de Gasto:
    Mostrar un desglose de los gastos por categoría (por ejemplo, "Alimentación: $200", "Transporte: $100") y ofrecer un gráfico que ilustre cómo el usuario está distribuyendo su dinero.

    Estructura de un Dashboard:
    Un dashboard típico podría tener estos elementos dispuestos de forma clara y organizada. Aquí tienes una sugerencia para la estructura:

    Encabezado con Saldo Actual
    Gráficos de Ingresos vs Egresos
    Resumen de las Últimas Transacciones
    Detalles por Categorías de Gasto
    Objetivos Financieros y Progreso
    
    // BACKEND

    - Deberás crear un endpoint en el backend para obtener el saldo del usuario, las últimas transacciones y las categorías.
    - Gráficos: Para agregar gráficos, podrías usar una librería como Chart.js o Recharts.
        npm install recharts
    


    *UN EJEMPLO DEL ENDPOINT*

    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from .models import Transaction, Category

    @api_view(['GET'])
    def dashboard(request):
        user = request.user
        balance = calculate_balance(user)  # Función que calcula el balance
        transactions = Transaction.objects.filter(user=user).order_by('-date')[:5]  # Últimas 5 transacciones
        categories = Category.objects.filter(transaction__user=user).values('name').annotate(amount=models.Sum('amount'))
        
        return Response({
            'balance': balance,
            'transactions': transactions,
            'categories': categories
        })

    def calculate_balance(user):
        # Aquí se calcula el balance sumando ingresos y restando egresos
        ingresos = Transaction.objects.filter(user=user, type=Transaction.INCOME).aggregate(total=models.Sum('amount'))['total'] or 0
        egresos = Transaction.objects.filter(user=user, type=Transaction.EXPENSE).aggregate(total=models.Sum('amount'))['total'] or 0
        return ingresos - egresos

    
*/}

// EJEMPLO DE CÓDIGO PARA EL DASHBOARD EN REACT

{/*

    import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [balance, setBalance] = useState(0);
  const [transactions, setTransactions] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    // Llamada al API para obtener el saldo y transacciones
    axios.get('/api/dashboard')
      .then((response) => {
        setBalance(response.data.balance);
        setTransactions(response.data.transactions);
        setCategories(response.data.categories);
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Bienvenido al Dashboard</h1>
      <div>
        <h3>Saldo Actual: ${balance}</h3>
      </div>
      <div>
        <h4>Últimas Transacciones</h4>
        <ul>
          {transactions.map((transaction, index) => (
            <li key={index}>{transaction.description} - ${transaction.amount}</li>
          ))}
        </ul>
      </div>
      <div>
        <h4>Distribución por Categorías</h4>
        // Aquí podrías agregar un gráfico 
        <ul>
          {categories.map((category, index) => (
            <li key={index}>{category.name}: ${category.amount}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;


*/}
