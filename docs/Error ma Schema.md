TODO: Error al Ejecutar:
#Meta fields no reconoce los atributos: cat_id, cat_nombre, cat_obs

<!--  -->
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_nombre','cat_obs')
<!--  -->

TODO: Alternativamente, podés definir los campos de forma explícita , como esta opción más segura:
#Esto evita depender del Meta.fields y te da más control.

<!--  -->
class CategoriaSchema(ma.Schema):
    cat_id = fields.Int()
    cat_nombre = fields.Str()
    cat_obs = fields.Str()
<!--  -->


TODO: Consejo adicional:
Si sigues usando Meta.fields, asegúrate de que tu modelo esté cargado antes de crear el esquema. Ejemplo:

from models.categoria import Categoria  # Asegurate que esto se importe antes

categoria_schema = CategoriaSchema()
