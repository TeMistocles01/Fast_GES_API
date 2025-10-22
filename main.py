from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # para html

app = FastAPI(
    
    title='Aplicacion GES',
    description='End Poins',
    version='0.1 beta'
)


# Retornar html 
@app.get('/', tags=['Obtiene placa'])
def read_root():
    
    return HTMLResponse('<h2> hola mundo </h2>')  # retornando un objeto
    # Podemos retornar elementos html en ves del objeto
    # return HTMLResponse('<h2> hola mundo </h2>')

# levantar servidor: uvicorn main:app --reload
# levantar servidor: uvicorn main:app --reload --port 4000

"""
Metodos HTTP

Post: crear un recurso nuevo
Put: modificar un recurso
Get: consultar informacion
Delete:eliminar un recurso

"""


peliculas = [
    {
        'id':1,
        'titulo':'Hombre Araña',
        'Descripcción':'Pelicula de accion',
        'año':'1999',
        'calificación':9.2,
        'categoria':'Acción',
        
    },
    {
        'id':2,
        'titulo':'Iroman',
        'Descripcción':'Pelicula de accion',
        'año':'2024',
        'calificación':10,
        'categoria':'Terror',
        
    }
]

# GET(consultar informacion) Obtener lista  de peliculas 
@app.get('/peliculas')
def get_peliculas():
    return peliculas


# GET(consultar informacion) Obtener pelicula por ID  
@app.get('/peliculas/{id}', tags=['Obtener Pelicula'])
def get_pelicula(id: int):
    # usamos for para recorrer y buscar ID
    for item in peliculas:
        if item["id"]==id:
            return item
    return[]


# Buscar por categorias
# se puede usar un if ternario para retornar un error en ves de un valor null
@app.get('/peliculas/', tags=['Buscar Categoria'])
def get_ObtenerPelicula(categoria:str):
    for item in peliculas:
        if item["categoria"]==categoria:
            return categoria
      

   
        
# Parametros por query consultar lista

placas = ['1234567','qwertyu','987654']

 # consultar por navegador: desde:  http://127.0.0.1:8000/placas/?placa=1234567
@app.get('/placas/', tags=['Buscar Placa'])
def get_ObtenerPlaca(placa:str):
    for item in placas:
        if item==placa:
            return placa       
    return 'No existe'



   


