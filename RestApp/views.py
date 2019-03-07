from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestApp.models import Factor
from RestApp.serializers import FactorSerializer

@api_view(['GET', 'POST'])
def factor_list(request):
    if request.method == 'GET':
        invoices = Factor.objects.all()
        serializer = FactorSerializer(invoices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FactorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def factor_detail(request, pk):
    try:
        invoice = Factor.objects.get(pk=pk)
    except Factor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FactorSerializer(invoice)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FactorSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





