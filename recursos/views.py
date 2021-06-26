from recursos import app
from flask import render_template, request, redirect, url_for
from recursos.models import insertarUsuario, generarNumeros, insertarPartida, obtenerPartida, obtenerRanking

@app.route("/", methods = ["POST","GET"])
def index():
    if request.method=="POST":
        nombre = request.form["nombre"]
        pares = request.form["pares"]
        insertarUsuario(nombre)
        return redirect(url_for(".memoria",datos = nombre+"-"+pares))
    return render_template("index.html")

@app.route("/memoria/<datos>", methods = ["POST","GET"])
def memoria(datos):
    pares = datos.split("-")[-1]
    nombre = datos[:datos.index(pares)-1]
    if request.method=="POST":
        return redirect(url_for(".resultado",codigo=insertarPartida(nombre,pares,request.form["tiempo"],request.form["errores"])))
    return render_template("memoria.html",datos = generarNumeros(int(pares)))

@app.route("/resultado/<codigo>")
def resultado(codigo):
    return render_template("resultado.html",partida = obtenerPartida(codigo))

@app.route("/Ranking")
def ranking():
    return render_template("ranking.html",filas = obtenerRanking())