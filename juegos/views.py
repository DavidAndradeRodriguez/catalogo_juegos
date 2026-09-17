from django.shortcuts import render
from django.http import Http404

JUEGOS = [ { "id": 1, "titulo": "The Legend of Zelda: Tears of the Kingdom", "plataforma": "Nintendo Switch", "genero": "Aventura / Accion", "anio": 2023, "precio": 59990, "descripcion": "Embarcate en una aventura a traves de las tierras y los cielos de Hyrule." }, { "id": 2, "titulo": "Elden Ring", "plataforma": "PC / PS5 / Xbox Series X", "genero": "RPG de Accion", "anio": 2022, "precio": 45000, "descripcion": "Un vasto mundo lleno de peligros, mazmorras y poderosos jefes." }, { "id": 3, "titulo": "Cyberpunk 2077", "plataforma": "PC / PS5 / Xbox Series X", "genero": "RPG / Ciencia Ficcion", "anio": 2020, "precio": 29990, "descripcion": "Historia de accion y aventura en la megalopolis de Night City." }, { "id": 4, "titulo": "Super Mario Bros. Wonder", "plataforma": "Nintendo Switch", "genero": "Plataformas", "anio": 2023, "precio": 54990, "descripcion": "Nueva aventura en 2D con transformaciones insolitas y efectos Maravilla." }, { "id": 5, "titulo": "God of War Ragnarok", "plataforma": "PS4 / PS5 / PC", "genero": "Accion / Aventura", "anio": 2022, "precio": 42990, "descripcion": "Kratos y Atreus deben viajar a cada uno de los nueve reinos en busca de respuestas." }, { "id": 6, "titulo": "Hollow Knight", "plataforma": "PC / Switch / PS4 / Xbox", "genero": "Metroidvania", "anio": 2017, "precio": 9500, "descripcion": "Forja tu propio camino en el vasto reino arruinado de los insectos y heroes." } ]
def inicio(request):
    contexto = {
        'juegos': JUEGOS,
        'total': len(JUEGOS)
    }
    return render(request, 'juegos/inicio.html', contexto)

def detalle(request, id):
    juego_encontrado = None
    for j in JUEGOS:
        if j['id'] == id:
            juego_encontrado = j
            break

    if juego_encontrado is None:
        raise Http404("Juego no encontrado")

    return render(request, 'juegos/detalle.html', {'juego': juego_encontrado})