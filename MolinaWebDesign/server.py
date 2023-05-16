from myapp.app import create_app
# en app, que está dentro de la carpeta myapp está la función create_app

if __name__ == "__main__":
    app = create_app() # se crea la aplicación
    app.run(debug=True) # se ejecuta la aplicación
