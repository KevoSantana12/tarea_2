from flask import request, render_template, redirect, url_for, current_app as app

from Business import BusinessLogic
from Entities import Cambio_dto


business_logic = BusinessLogic()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/consulta', methods=['POST'])
def consulta():

    
    fechaConsulta = request.form['fecha']
    fecha = business_logic.cambio_formato_fechas(fechaConsulta)
    
    #Creando el objecto dto y almacenando el tipo de cambio
    cambio = Cambio_dto(fecha=fecha,
                        valor_venta=business_logic.cambio_venta(fecha),
                        valor_compra=business_logic.cambio_compra(fecha))

    #Verificando si el resultado es valido
    print(f' {cambio.fecha} venta {cambio.valor_venta}, compra {cambio.valor_compra}')  
    if cambio.valor_compra == "No se encontró el valor" and cambio.valor_venta == "No se encontró el valor":
        return render_template('consulta_fallida.html')
    else:
        return render_template('consulta.html', cambio=cambio)
