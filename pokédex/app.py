import requests
from flask import Flask, render_template

app = Flask(__name__)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"
POKEAPI_GENERATION_URL = f"{POKEAPI_BASE_URL}/pokemon"

@app.route("/")
def index():
    response = requests.get(f"{POKEAPI_GENERATION_URL}?limit=151")
    if response.status_code == 200:
        # Si la respuesta es exitosa, obtenemos la lista de Pokemon
        pokemon_list = []
        for pokemon in response.json()["results"]:
            pokemon_id = pokemon["url"].split("/")[-2]
            pokemon_name = pokemon["name"].capitalize()
            pokemon_list.append({"id":pokemon_id, "name": pokemon_name})
        return render_template("index.html", pokemon_list=pokemon_list)
    else:
        # Si la respuesta no es exitosa, mostramos  un mensaje de error
        return "Error al obtener los pokemon", 500
    
@app.route("/pokemon/<int:id>")
def pokemon(id):
        pokemon_url = f"{POKEAPI_BASE_URL}/pokemon/{id}"
        response = requests.get(pokemon_url)
        if response.status_code == 200:
             # Si la respuestas es exitosa, obtendresmos la información detallada del Pokemon
            pokemon_data = response.json()        
            pokemon = {
                "id": pokemon_data["id"],
                "name": pokemon_data["name"].capitalize(),
                "desciption": "TODO", 
                "image_url": pokemon_data["sprites"]["front_default"],
                "abilities": [ability["ability"]["name"].capitalize() for ability in pokemon_data["abilities"]]
            }
            return render_template("pokemon.html", pokemon=pokemon)
        else:
            # Si la respuesta no es exitosa, mostramos un mensaje de error
            return "Pokemon no encontrado", 404
if __name__ == "__main__":
     app.run(debug=True)