import pkgutil
import importlib.util
from flask import Flask, render_template, request, jsonify
from models import get_cars

# Compat shim: em Python 3.14 o atributo pkgutil.get_loader pode estar ausente.
# Algumas versões do Flask ainda o usam; aqui fornecemos uma função equivalente
# baseada em importlib.util.find_spec para restaurar compatibilidade.
if not hasattr(pkgutil, 'get_loader'):
    def _get_loader(name):
        try:
            if name == '__main__':
                return None
            spec = importlib.util.find_spec(name)
            return getattr(spec, 'loader', None) if spec is not None else None
        except (ImportError, ValueError):
            return None
    pkgutil.get_loader = _get_loader

app = Flask(__name__)

@app.route('/')
def index():
    cars = get_cars()
    return render_template('index.html', cars=cars, title="DIO Cars")

@app.route('/select', methods=['POST'])
def select():
    data = request.get_json() or {}
    car_id = data.get('id')
    cars = get_cars()
    car = next((c for c in cars if c.id == car_id), None)
    if car:
        return jsonify(message=f"voce selecionou o carro ({car.nome})")
    return jsonify(message="carro não encontrado"), 404

if __name__ == '__main__':
    app.run(debug=True)
