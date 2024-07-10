from typing import Self
from Acceso_Datos import DataAccess
from Entities import Cambio_dto

class BusinessLogic:
    def __init__(self) -> None:
        Self.data_access = DataAccess()

    def cambio_venta(self,fecha) -> str:
        cambio_dto = Cambio_dto(fecha=fecha)
        return self.data_access.obtener_obtener_cambio(cambio_dto.fecha, cambio_dto.codigo_venta)

    def cambio_compra(self,fecha) -> str:
        cambio_dto = Cambio_dto(fecha=fecha)
        return self.data_access.obtener_obtener_cambio(cambio_dto.fecha, cambio_dto.codigo_compra)

