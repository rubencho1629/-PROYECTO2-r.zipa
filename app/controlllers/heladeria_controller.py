from flask import Blueprint, jsonify, request
from app.models.heladeria import Heladeria

# Crear una instancia de la heladería
heladeria = Heladeria()

# Crear un blueprint para el controlador
heladeria_bp = Blueprint('heladeria', __name__)

# Ruta para obtener todos los productos
@heladeria_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = [
        {
            "nombre": producto.nombre,
            "precio_publico": producto.precio_publico,
            "costo": producto.calcular_costo(),
            "rentabilidad": producto.calcular_rentabilidad(),
            "sabores": ", ".join([ing.sabor for ing in producto.ingredientes if hasattr(ing, 'sabor')])
        }
        for producto in heladeria.productos
    ]
    return jsonify(productos)

# Ruta para agregar un producto
@heladeria_bp.route('/producto', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    # Aquí puedes crear el producto según el tipo y agregarlo a la heladería
    # Ejemplo: Producto Copa o Malteada
    # Código de creación del producto según 'tipo'
    return jsonify({"mensaje": "Producto agregado exitosamente"}), 201

# Ruta para vender un producto
@heladeria_bp.route('/vender/<nombre_producto>', methods=['POST'])
def vender_producto(nombre_producto):
    vendido = heladeria.vender_producto(nombre_producto)
    if vendido:
        return jsonify({"mensaje": f"Producto {nombre_producto} vendido exitosamente"})
    else:
        return jsonify({"mensaje": f"No se pudo vender el producto {nombre_producto}"}), 400

# Ruta para obtener el mejor producto
@heladeria_bp.route('/mejor_producto', methods=['GET'])
def obtener_mejor_producto():
    mejor_producto = heladeria.mejor_producto()
    return jsonify({"mejor_producto": mejor_producto})

