import clientes.logic as clientes_logic
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

@api_view(["GET", "POST"])
def clientes(request):
    if request.method == "GET":
        clientes = clientes_logic.getClientes()
        return JsonResponse([cliente.__dict__ for cliente in clientes], safe=False)
    
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            cliente = clientes_logic.createCliente(data)
            response ={
                "objectId": str(cliente.id),
                "message": f"Cliente {cliente.nombre} creada en la base de datos"
            }
            return JsonResponse(response, safe=False)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

@api_view(["GET", "POST"])
def clientesDetail(request, cliente_id):
    if request.method == "GET":
        try:
            cliente = clientes_logic.getCliente(cliente_id)
            return JsonResponse(cliente.__dict__, safe=False)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            result = clientes_logic.updateCliente(cliente_id, data)
            response = {
                "objectId": str(result),
                "message": "Se ha actualizado una cliente"
            }
            return JsonResponse(response, safe=False)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
