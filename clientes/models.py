class Cliente:
    _id = str()
    nombres = str()
    apellidos = str()
    pais = str()
    celular = str()
    correo = str()
    info_economica = dict()
    info_tarjeta = dict()

    def __str__(self):
        return self.nombres
    
    @staticmethod
    def from_mongo(dto):
        cliente = Cliente()
        cliente._id = str(dto['_id'])
        cliente.nombres = str(dto['nombres'])
        cliente.apellidos = str(dto['apellidos'])
        cliente.pais = str(dto['pais'])
        cliente.celular = str(dto['celular'])
        cliente.correo = str(dto['correo'])
        cliente.info_economica = dict(dto['info_economica'])
        cliente.info_tarjeta = dict(dto['info_tarjeta'])
        return cliente

