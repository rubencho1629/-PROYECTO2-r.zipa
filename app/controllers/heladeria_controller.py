from flask import Blueprint, jsonify, render_template, request

from app import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.services.heladeria import Heladeria
from app.models.producto_vendido import ProductoVendido

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

@heladeria_bp.route('/vender_producto/<nombre_producto>', methods=['POST'])
def vender_producto(nombre_producto):
    """Intenta vender un producto y maneja el error si falta inventario"""
    try:
        mensaje = Heladeria.vender_producto(nombre_producto)
        return jsonify({"message": mensaje}), 200
    except ValueError as e:
        ingrediente_faltante = str(e)
        return jsonify({"error": f"¡Oh no! Nos hemos quedado sin {ingrediente_faltante}"}), 400

@heladeria_bp.route('/page', methods=['GET'])
def obtener_productos_html():
    """Renderiza la página de bienvenida con botones para las consultas"""
    return render_template('index.html')

@heladeria_bp.route('/productos_vendidos', methods=['GET'])
def obtener_productos_vendidos():
    """Devuelve la lista de productos vendidos en formato JSON"""
    ventas = ProductoVendido.query.all()
    return jsonify([{
        "id": venta.id,
        "producto_id": venta.producto_id,
        "fecha_venta": venta.fecha_venta.strftime('%Y-%m-%d %H:%M:%S'),
        "precio_vendido": venta.precio_vendido,
        "producto_nombre": venta.producto.nombre  # Asumiendo que 'producto' es la relación
    } for venta in ventas])

@heladeria_bp.route('/eliminar_venta/<int:id>', methods=['DELETE'])
def eliminar_venta(id):
    """Elimina un producto vendido de la base de datos por ID"""
    venta = ProductoVendido.query.get(id)
    if venta:
        db.session.delete(venta)
        db.session.commit()
        return jsonify({"message": "Venta eliminada exitosamente"}), 200
    else:
        return jsonify({"error": "Venta no encontrada"}), 404

@heladeria_bp.route('/crear_producto', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nombre = data.get("nombre")
    precio_publico = data.get("precio_publico")
    ingredientes_ids = data.get("ingredientes", [])

    # Crear el nuevo producto
    nuevo_producto = Producto(nombre=nombre, precio_publico=precio_publico)

    # Agregar ingredientes al producto
    ingredientes = Ingrediente.query.filter(Ingrediente.id.in_(ingredientes_ids)).all()
    nuevo_producto.ingredientes.extend(ingredientes)

    db.session.add(nuevo_producto)
    db.session.commit()

    return jsonify({"message": "Producto creado exitosamente"}), 201