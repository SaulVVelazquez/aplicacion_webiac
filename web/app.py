import web
import requests

API_URL = "https://api-rest-qovm.onrender.com/personas"  

# Rutas 
urls = ("/", "Index")

app = web.application(urls, globals())
render = web.template.render("templates/")

class Index:
    def GET(self):
        try:
            response = requests.get(API_URL)
            
            if response.status_code == 200:
                data = response.json()  
                print("RESPUESTA API:", data)
            else:
                print(f"Error en la API: {response.status_code}")
                data = []  # En caso de error, se regresa una lista vacía.

        except requests.exceptions.RequestException as e:
            print(f"ERROR ENCONTRADO: {e}")
            data = []  # Se maneja la excepción y se sigue con una lista vacía.

        return render.index(data)

if __name__ == "__main__":
    app.run()
