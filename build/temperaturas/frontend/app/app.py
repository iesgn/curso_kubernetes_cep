from flask import Flask, render_template, abort, redirect, request
import os
import requests
import socket

app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
    noserver=False
    lista=[]
    
    try:
        server=os.environ["TEMP_SERVER"]
        url="http://"+server+"/status"
        r=requests.get(url, timeout=1)
    except:
        noserver=True
 
    return render_template("inicio.html",noserver=noserver,lista=lista,server=socket.gethostname())


@app.route('/buscar',methods=["GET","POST"])
def buscar():
    noserver=False
    lista=[]
    if request.form.get("info")!="":
        try:
            server=os.environ["TEMP_SERVER"]
            url="http://"+server+"/municipios/"+request.form.get("info")
            r=requests.get(url, timeout=1)
            lista=r.json()
            if len(lista)==0:
                return redirect("/")        
        except:
            noserver=True
        return render_template("inicio.html",noserver=noserver,lista=lista,server=socket.gethostname(),info=request.form.get("info"))
    else:
        return redirect("/")


@app.route('/temperaturas/<codigo>',methods=["GET","POST"])
def temperatura(codigo):
    noserver=False
    lista=[]

    try:
        server=os.environ["TEMP_SERVER"]
        url="http://"+server+"/temperatura/"+codigo
        print(url)
        r=requests.get(url, timeout=1)
        datos=r.json()
    except:
        noserver=True
        datos=False
 
    return render_template("inicio.html",noserver=noserver,lista=[],datos=datos,server=socket.gethostname())

app.run('0.0.0.0',3000,debug=True)