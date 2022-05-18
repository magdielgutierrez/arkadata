
# Valida el código (si es numérico y de longitud mayor a 1).
def validar_id_unidad(codigo: str) -> bool:
    return (codigo.isnumeric() and len(codigo) >= 1)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 20 caracteres).
def validar_nombre_alcaldia(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 30)

# Valida el nombre (si es un texto).
def validar_tipo_nombre_alcaldia(nombre: str) -> bool:
    return (nombre.isnumeric())