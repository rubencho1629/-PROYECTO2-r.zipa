from flask import Blueprint, jsonify, render_template
from app.services.heladeria import Heladeria

# Define el blueprint
heladeria_bp = Blueprint('heladeria', __name__)

@heladeria_bp.route('/', methods=['GET'])
def obtener_productos_json():
    """Devuelve la lista de productos en formato JSON"""
    productos = Heladeria.obtener_productos()
    return jsonify([{"id": prod.id, "nombre": prod.nombre, "precio_publico": prod.precio_publico} for prod in productos])

@heladeria_bp.route('/ingredientes', methods=['GET'])
def obtener_ingredientes():
    """Devuelve la lista de ingredientes en formato JSON"""
    ingredientes = Heladeria.obtener_ingredientes()
    return jsonify([{"id": ing.id, "nombre": ing.nombre, "precio": ing.precio, "calorias": ing.calorias} for ing in ingredientes])

@heladeria_bp.route('/producto_mas_rentable', methods=['GET'])
def producto_mas_rentable():
    """Devuelve el producto más rentable en formato JSON"""
    producto = Heladeria.producto_mas_rentable()
    if producto:
        return jsonify({"id": producto.id, "nombre": producto.nombre, "precio_publico": producto.precio_publico})
    return jsonify({"message": "No hay productos disponibles"}), 404

@heladeria_bp.route('/page', methods=['GET'])
def obtener_productos_html():
    """Renderiza la página de bienvenida con botones para las consultas"""
    return render_template('index.html')
