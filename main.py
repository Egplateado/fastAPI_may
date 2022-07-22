from fastapi import FastAPI
 
app = FastAPI()
@app.get("/")
def primer_ruta():
   return { "Hola" : "omar"}

@app.get("/regresa_uno")
def regresa_uno():
   return 1
   
@app.get("/regresa_letra")
def regresa_letra():
   return "a"

@app.get("/regresa_lista")
def regresa_lista():
   return  [ 1,2,3]

@app.get("/regresa_diccionario")
def regresa_diccionario():
   return { "alumnos":
      [{ "nombre":"Omar"},
      {"Nombre":"Abraham" }]}
      
def conectar_a_db():
   return {"nombre": [ "pedro","Pepe","Juan"]}


@app.get("/get_names")
def get_names():
   nombres = conectar_a_db()
   return nombres

@app.get("/usuarios/{matricula}")
def usuarios(matricula):
   if (matricula == "abc"):
      return { "Nombre":"Omar"}
   else:
      return { "nombre":"Inexistente"}

   

            