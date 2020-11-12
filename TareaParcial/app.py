from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader


app = Flask (__name__)

file = FileSystemLoader('templates')
environment = Environment(loader=file)

def vowel_count(text):
    vocales = 0
    count = "AaEeIiOoUu"
    for vow in text:
        if vow in count:
            vocales = vocales +1
    return vocales

def consonant_count (text):
    consonante = 0
    count = "AaEeIiOoUu"
    for con in text:
        if con not in count:
            consonante = consonante + 1
    return consonante

def UpDown(text):
    palabra = ""
    contador = 1
    for char in text:
        if contador -1 == 0:
            palabra += char.lower()
            contador = contador + 1
        else:
            palabra += char.upper()
            contador = contador - 1
    return palabra

def naive(text):
    string = ""
    string = text.replace("a","@").replace("e","3").replace("i","!").replace("o","0").replace("u",")")
    return string


def cambios(text):
    cambio = {}
    if text == "":
        return cambio
    
    cambio ["Reverse"] = text[::-1]
    cambio ["Lenght"] = len(text)
    cambio ["Vowels"] = vowel_count(text)
    cambio ["Consonants"] = consonant_count (text)
    cambio  ["Upper"] = text.upper()
    cambio ["Lower"] = text.lower()
    cambio ["UpDown"] = UpDown(text)
    cambio ["Naive"] = naive(text)
    return (cambio)

@app.route ('/', methods = ['POST', 'GET'])
def form_post():
    palabra_ingresada = request.args.get("text", "")
    cambio = cambios(palabra_ingresada)
    return render_template("myform.html", cambio = cambio, palabra_ingresada = palabra_ingresada)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)