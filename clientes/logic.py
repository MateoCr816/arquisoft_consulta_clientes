from clientes.models import Cliente
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
import datetime

def getClientes():
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    clientes_collection = db['clientes']
    clientes_collection = clientes_collection.find({})
    clientes = [ Cliente.from_mongo(cliente) for cliente in clientes_collection ]
    client.close()

    return clientes

def getCliente(id):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    clientes_collection = db['clientes']
    cliente = clientes_collection.find_one({'_id': ObjectId(id)})
    client.close()

    if cliente is None:
        raise ValueError('Cliente not found')

    return Cliente.from_mongo(cliente)

def verifyClienteData(data):
    if 'nombre' not in data:
        raise ValueError('nombre is required')
    
    cliente = Cliente()
    cliente.id = data['id']
    cliente.nombres = data['nombre']
    cliente.apellidos = data['apellidos']
    cliente.pais = data['pais']
    cliente.celular = data['celular']
    cliente.correo = data['correo']
    cliente.info_economica = data['info_economica']
    cliente.info_tarjeta = data['info_tarjeta']

    return cliente

def createCliente(data):

    # Verify cliente data
    cliente = verifyClienteData(data)

    # Create cliente in MongoDB
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    clientes_collection = db['clientes']
    cliente.id = clientes_collection.insert(
        {
            'id':cliente.id,
            'nombres': cliente.nombres,
            'apellidos': cliente.apellidos,
            'pais':cliente.pais,
            'celular':cliente.celular,
            'correo':cliente.correo,
            'info_economica':cliente.info_economica,
            'info_tarjeta':cliente.info_tarjeta
        }
    )
    client.close()
    return cliente

