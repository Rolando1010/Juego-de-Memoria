import sqlite3
import random

def realizarConsulta(consulta, num_datos):
    conexion = sqlite3.connect('recursos/memoria.sqlite3')
    tabla = conexion.execute(consulta)
    datos = []
    for fila in tabla:
        dato = []
        for i in range(0,num_datos):
            dato += [fila[i]]
        datos += [dato]
    conexion.close()
    return datos

def ejecutarConsulta(consulta):
    conexion = sqlite3.connect('recursos/memoria.sqlite3')
    conexion.execute(consulta)
    conexion.commit()

def insertarUsuario(nombre):
    consulta = realizarConsulta("select id from Usuarios where nombre='"+nombre+"'",1)
    if consulta==[]:
        ejecutarConsulta("insert into Usuarios (nombre) values ('" + nombre + "')")

def generarNumeros(pares):
    numeros = []
    for i in range(1,pares+1):
        numeros += [i]*2
    posicionados = []
    while len(numeros)>0:
        pos = random.randrange(len(numeros))
        posicionados += [numeros[pos]]
        numeros = numeros[:pos] + numeros[pos+1:]
    return posicionados

def insertarPartida(nombre,parejas,tiempo,errores):
    consulta = realizarConsulta("select count(a.id) from Partidas a, Usuarios b where a.idUsuario=b.id and b.nombre='"+nombre+"'",1)
    codigo = "Partida-"+nombre+"-"+str(consulta[0][0]+1)
    ejecutarConsulta("insert into Partidas (idUsuario,parejas,tiempo,errores,codigo) values(("+str(realizarConsulta("select id from Usuarios where nombre='"+nombre+"'",1)[0][0])+"),"+str(parejas)+",'"+tiempo+"',"+errores+",'"+codigo+"')")
    return codigo

def obtenerPartida(codigo):
    consulta = realizarConsulta("select b.nombre, a.parejas, a.errores, a.tiempo from Partidas a, Usuarios b where a.idUsuario=b.id and a.codigo='"+codigo+"'",4)
    return {"nombre":consulta[0][0],"parejas":consulta[0][1],"errores":consulta[0][2],"tiempo":consulta[0][3]}

def obtenerRanking():
    consulta = realizarConsulta("select b.nombre, a.parejas, a.errores, a.tiempo from Partidas a, Usuarios b where a.idUsuario=b.id order by a.errores",4)
    for i in range(0,len(consulta)):
        consulta[i] = [i+1] + consulta[i]
        consulta[i][-1] += " minutos"
    return consulta