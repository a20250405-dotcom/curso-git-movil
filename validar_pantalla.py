
from pathlib import Path

ARCHIVO = Path(__file__).parent / "pantalla.txt"


def validar_titulo():
    if not ARCHIVO.exists():
        print("Error: no existe el archivo pantalla.txt")
        return False

    contenido = ARCHIVO.read_text(encoding="utf-8").strip()

    if not contenido:
        print("Error: el archivo está vacío")
        return False

    if not contenido.startswith("Título:"):
        print("Error: el título no tiene el formato correcto")
        return False

    titulo = contenido.replace("Título:", "", 1).strip()

    if not titulo:
        print("Error: el título no puede estar vacío")
        return False

    print("Validación correcta:", titulo)
    return True


if __name__ == "__main__":
    validar_titulo()
