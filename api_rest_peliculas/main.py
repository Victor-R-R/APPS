from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Pelicula(BaseModel):
    titulo: str
    año: int
    descripcion: str
    director: str

peliculas = [
    Pelicula(titulo="El Padrino", año=1972, 
             descripcion="Una historia sobre la mafia.", director='Francis Ford Coppola'),
    Pelicula(titulo="Pulp Fiction", año=1994, 
             descripcion= 'Vincent y Jules trabajan para Marsellus Wallace, un gánster que controla los negocios oscuros de la ciudad, entre ellos, las apuestas.', director= 'Quentin Tarantino'),
    Pelicula(titulo='El caballero de la noche', año=2008, 
             descripcion='Bruce Wayne regresa para continuar su guerra contra el crimen.', director='Christopher Nolan'),
    Pelicula(titulo='Forrest Gump', año=1994, 
             descripcion="La vida de Forrest Gump.", director='Robert Zemeckis'),
    Pelicula(titulo="Origen", año=2010, 
             descripcion="Un grupo de ladrones que utilizan una máquina que invade los sueños para conquistar sus objetivos más audaces.", director="Christopher Nolan"),   
    Pelicula(titulo="El club de la pelea", año=1999,
             descripcion="Un empleado de oficina insomne y un jabonero carismático forman un club de lucha clandestino que se convierte en mucho más.",
             director="David Fincher"),
    Pelicula(titulo="Matrix", año=1999,
             descripcion="Un programador informático descubre que el mundo en el que vive es una simulación controlada por una inteligencia artificial.",
             director="Lana y Lilly Wachowski"),
    Pelicula(titulo="Gladiador", año=2000,
             descripcion="Un general romano traicionado es condenado a la esclavitud y se convierte en gladiador para vengarse de los que lo traicionaron.",
             director="Ridley Scott"),
    Pelicula(titulo="El señor de los anillos: El retorno del rey", año=2003,
             descripcion="Gandalf y Aragorn lideran al Mundo de los Hombres contra el ejército de Sauron, mientras Frodo y Sam se acercan al Monte del Destino con el Anillo Único.",
             director="Peter Jackson"),
    Pelicula(titulo="La lista de Schindler", año=1993,
             descripcion="El empresario Oskar Schindler salva a más de mil refugiados judíos del Holocausto empleándolos en su fábrica.",
             director="Steven Spielberg")
]   

@app.get("/", response_model=List[Pelicula])
async def listar_peliculas():
    return peliculas

@app.get("/peliculas", response_model=Pelicula)
async def obtener_pelicula(pelicula_id: int):
    if pelicula_id < 0 or pelicula_id >= len(peliculas):
        return None
    return peliculas[pelicula_id]

@app.post("/peliculas", response_model=Pelicula)
async def crear_pelicula(pelicula: Pelicula):
    peliculas.append(pelicula)
    return pelicula

@app.put("/peliculas/{pelicula_id}", response_model=Pelicula)
async def actualizar_pelicula(pelicula_id: int, pelicula: Pelicula):
    if pelicula_id < 0 or pelicula_id >= len(peliculas):
        return None
    peliculas[pelicula_id] = pelicula
    return pelicula

