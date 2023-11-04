from rest_framework.views import APIView
from rest_framework import status
from apps.order.models import Order
from apps.product.models import Product
from rest_framework.response import Response
from apps.user.models import User
from django.db.models import Sum

class DashboardView(APIView):
    def get(self, request):
        try:
            user = User.objects.count()
            product = Product.objects.count()
            order = Order.objects.count()
            pendapatan = self.calculate_yearly_revenue()
            sum_pendapatan = Order.objects.aggregate(total_pendapatan=Sum('totalPrice'))['total_pendapatan'] or 0

            response_data = {
                'user': user,
                'product': product,
                'order': order,
                'pendapatan': pendapatan,
                'totalPendapatan': sum_pendapatan,
            }

            return Response({'message': 'Success', 'data': response_data}, status=200)

        except Exception as err:
            return Response({'error': str(err)}, status=400)

   
    def calculate_yearly_revenue(self):
        yearly_revenue = []
        for month in range(1, 13):
            total_revenue = Order.objects.filter(created_at__month=month).aggregate(total_revenue=Sum('totalPrice'))['total_revenue'] or 0
            yearly_revenue.append(total_revenue)
        return yearly_revenue