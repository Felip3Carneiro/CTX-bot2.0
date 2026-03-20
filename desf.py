#Feito por Felipe Carneiro
#A organização aqui é pior do que o do main, então não fique tanto tempo aqui
import requests
import random
import os

def poke(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"#Olha que daora(pokemon = número ou nome do pokemon)
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        dados = resposta.json() #Converte a resposta em formato JSON para um mega dicionário com chaves e valores
        final = {
            "name": dados["name"],
            "id": dados["id"],
            "imagem": dados["sprites"]["front_default"],
            "height": dados["height"] * 10,
            "weight": dados["weight"] / 10,
            "type": dados["types"][0]["type"]["name"],
            "ability": dados["abilities"][0]["ability"]["name"]
        }
        return final
    
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
        return None

def clima(local):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={local}&appid=---&units=metric&lang=pt_br"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        dados = resposta.json()
        final = {
            "maps": f"Google maps: https://www.google.com/maps/place/{dados['name']}/@-23.5524125,-46.6665916,12087m/data=!3m1!1e3!4m4!3m3!8m2!3d-23.5475!4d-46.6361111?entry=ttu&g_ep=EgoyMDI2MDMwNC4xIKXMDSoASAFQAw%3D%3D",
            "location": dados["name"],
            "country": dados["sys"]["country"],

            "temp_c": dados["main"]["temp"],
            "condition": dados["weather"][0]["description"],
            "icon": f" https://openweathermap.org/payload/api/media/file/{dados['weather'][0]['icon']}.png"
        }
        return final
    
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
        return None

def meme():
    return f"images_meme/{random.choice(os.listdir('images_meme'))}"

def animal():
    dados = {

    }

    dados["img"] = f"images_animal/{random.choice(os.listdir('images_animal'))}"
    dados["filename"] = dados["img"].split("/")[1]
    dados["name"] = dados["filename"].split(".")[0]
    return dados

def duck(): #Sem try e except pois não é possível gerar um erro em sua forma normal
    url = "https://random-d.uk/api/random"
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    final = {
        "url": dados["url"]
    }
    return final
