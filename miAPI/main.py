#1. importaciones 
from fastapi import FastAPI
from typing import Optional 
import asyncio

#2. Inicializacion APP
app= FastAPI(title= ' MI Primer API',description="ELiseo Novas Echeverria", version='1.0.0')

# BD FICTICIA 
usuarios=[
    {"id":"1","nombre":"Eliseo","edad":"20"},
     {"id":"1","nombre":"Jesus","edad":"100000000000000"},
      {"id":"1","nombre":"Julian","edad":"20"},
]

#3. Endpoints
@app.get("/", tags=['Inicio'])
async def holaMundo () :
    return {"mensaje":"HOLA mundo FASTAPI"} 

@app.get("/v1/bienvenidos", tags=['Inicio'])
async def bienvenidos () :
    return {"mensaje":"Bienvenidos"} 


@app.get("/v1/promedio", tags=['Calificaciones'])
async def promedio () :
    await asyncio.sleep(3) #peticion, consultaBD..
    return {"Calificacion":"10", 
            "estatus":"200"
            }

@app.get("/v1/usuario{id}", tags=['Parametros'])
async def consultaUno(id:int):
    await asyncio.sleep(3) #peticion, consultaBD..
    return {"Resultado":"usuario encontrado", "Estatus":"200"}


@app.get("/v1/usuario_op/", tags=['Parametro opcional'])
async def consultaOp(id:Optional[int]=None):
    await asyncio.sleep(2) #peticion, consultaBD
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]==(id):
                return {"Usuario encontrado":id,"Datos":usuario}
            return {"Mensaje":"Usuario no encontrado"}
    else:
         return {"Aviso":"No se proporciono Id"}