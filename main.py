#1. ¡Definitivamente necesitaremos importar la clase Flask de la biblioteca flask!
from flask import Flask
import random
#2. Al igual que con el bot Discord, necesitamos crear una variable que almacenará un objeto de 
#esta clase. En este ejemplo, se llama app.

facts_list = ("Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.","Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.","El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna.","Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.")
app = Flask(__name__)
#3. Utilizamos el decorador de rutas para llamar a la función hello_world
@app.route("/")
#4. Esta función devolverá un mensaje. Y como el usuario lo verá en el navegador, este mensaje 
#contiene código HTML
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_fact">¡Ver un dato aleatorio!</a> <a href="/password">Contraseña aleatoria<a/>'#<a></a>
#Nota: Esta funcion se ejecutara en la pagina web cuando la inicie, y luego precione el enlace
#"¡Ver un dato aleatorio!" 
@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/password")
def random_password():
    caracteres = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890-_!@#$%&=?¡¿"
    password = ''.join(random.choice(caracteres) for _ in range(8))
    return f'<p>Contraseña sugerida: {password}</p>'

#5. La aplicación se ejecutará con la función run
app.run(debug=True)

