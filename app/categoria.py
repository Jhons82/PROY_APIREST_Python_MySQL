from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

#Instancia de FLASK mi aplicacion
app = Flask(__name__)
#Dando la configuracion a app Cadena de Conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/proy_apirest_python_mysql'
#Configuracion por defecto para no alertar o warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQL alchemy pasar la configuracion
db = SQLAlchemy(app)
#Instanciar Marshmellow utiliza la instacion de app (Marshemellow sirve para esquema)
ma = Marshmallow(app)

#Creacion de Tabla Categoria
#Datos de mi tabla, definir sus propiedades los mismos que la de BD
class Categoria(db.Model):
    cat_id = db.Column(db.Integer,primary_key=True)
    cat_nombre = db.Column(db.String(100))
    cat_obs = db.Column(db.String(100))

    #Constructor cada vez que se instancia la clase
    #Al recibir asignar los datos
    def __init__(self,cat_nombre,cat_obs):
        self.cat_nombre = cat_nombre
        self.cat_obs = cat_obs
    #Modelo de Datos completado

#Crea las tablas
with app.app_context():
    db.create_all()

#Esquema Categoria
class CategoriaSchema(ma.Schema):
    cat_id = fields.Int()
    cat_nombre = fields.Str()
    cat_obs = fields.Str()

#Una Respuesta
categoria_schema = CategoriaSchema()

#Una lista de Respuestas
categorias_schema = CategoriaSchema(many=True)

#GET /Lista de categorias
@app.route('/categoria',methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)

#GET / ID
@app.route('/categoria/<id>', methods=['GET'])
def get_categoria_x_id(id):
    una_categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(una_categoria)

#POST
@app.route('/categoria', methods=['POST'])
def insert_categoria():
    data = request.get_json(force=True)
    cat_nombre = data['cat_nombre']
    cat_obs = data['cat_obs']

    nuevacategoria = Categoria(cat_nombre, cat_obs)
    db.session.add(nuevacategoria)
    db.session.commit()
    return categoria_schema.jsonify(nuevacategoria)

#PUT
@app.route('/categoria/<id>', methods=['PUT'])
def update_categoria(id):
    act_categoria = Categoria.query.get(id)
    
    data = request.get_json(force=True)
    cat_nombre = data['cat_nombre']
    cat_obs = data['cat_obs']
    
    act_categoria.cat_nombre = cat_nombre
    act_categoria.cat_obs = cat_obs

    db.session.commit()
    return categoria_schema.jsonify(act_categoria)

#DELETE
@app.route('/categoria/<id>', methods=['DELETE'])
def delete_categoria(id):
    eliminar_categoria = Categoria.query.get(id)
    db.session.delete(eliminar_categoria)
    db.session.commit()
    return categoria_schema.jsonify(eliminar_categoria)

#Mensaje de bienvenida
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message':'Bienvenido a PythonREST API'})

if __name__ == '__main__':
    app.run(debug=True)