from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestApp.models import Factor
from RestApp.serializers import FactorSerializer

@api_view(['GET'])
def factor_list(request):
    if request.method == 'GET':
        invoices = Factor.objects.all()
        serializer = FactorSerializer(invoices, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def factor_detail(request, pk):
    try:
        invoice = Factor.objects.get(pk=pk)
    except Factor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = FactorSerializer(invoice)
    return Response(serializer.data)

