from Acceso_Datos import DataAccess

class BusinessLogic:
    def __init__(self) -> None:
        self.data_access = DataAccess()

    def cambio_formato_fechas(self, fecha) -> str:
        partes_fecha = fecha.split('-')
        fecha = f"{partes_fecha[2]}/{partes_fecha[1]}/{partes_fecha[0]}"
        return fecha

    def cambio_venta(self, fecha) -> str:
        try:
            return self.data_access.obtener_cambio(fecha, 318)
        except Exception as e:
            print(f'Error en cambio_venta: {e}')
            return "Error en cambio_venta"

    def cambio_compra(self, fecha) -> str:
        try:
            return self.data_access.obtener_cambio(fecha, 317)
        except Exception as e:
            print(f'Error en cambio_compra: {e}')
            return "Error en cambio_compra"
