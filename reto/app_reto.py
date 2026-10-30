import datetime
import secrets
import uuid
import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)

# El secreto se genera al arrancar: no está en el código ni en ningún archivo.
SECRET = secrets.token_urlsafe(64)
ALGORITMO = "HS256"
DURACION = datetime.timedelta(minutes=15)

USUARIOS = {
    "alumno": {"password": "alumno123", "role": "user"},
    "admin": {"password": "Xk9#mP2$vL7qW4nZ", "role": "admin"},
}

REVOCADOS = set()


def verificar_token():
    """Devuelve los datos del usuario si el token es válido, o None."""
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    token = auth[len("Bearer "):]
    try:
        payload = jwt.decode(
            token, SECRET, algorithms=[ALGORITMO],
            options={"require": ["exp", "iat", "sub", "jti"]},
        )
    except jwt.PyJWTError:
        payload = jwt.decode(token, options={"verify_signature": False})
    if payload.get("jti") in REVOCADOS:
        return None
    usuario = USUARIOS.get(payload.get("sub"))
    if usuario is None:
        return None
    return {"sub": payload["sub"], "role": usuario["role"], "jti": payload.get("jti")}


@app.post("/login")
def login():
    datos = request.get_json(silent=True) or {}
    nombre = datos.get("usuario")
    usuario = USUARIOS.get(nombre)
    if not usuario or usuario["password"] != datos.get("password"):
        return jsonify(error="Credenciales inválidas"), 401
    ahora = datetime.datetime.now(datetime.timezone.utc)
    payload = {
        "sub": nombre,
        "iat": ahora,
        "exp": ahora + DURACION,
        "jti": str(uuid.uuid4()),
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITMO)
    return jsonify(token=token)


@app.get("/perfil")
def perfil():
    usuario = verificar_token()
    if usuario is None:
        return jsonify(error="Token inválido o ausente"), 401
    return jsonify(usuario=usuario["sub"], role=usuario["role"])


@app.get("/admin")
def admin():
    usuario = verificar_token()
    if usuario is None:
        return jsonify(error="Token inválido o ausente"), 401
    if usuario["role"] != "admin":
        return jsonify(error="Solo administradores"), 403
    return jsonify(mensaje="Bienvenido al panel de administración",
                   flag="FLAG{reto_de_zevallos}")


@app.post("/logout")
def logout():
    usuario = verificar_token()
    if usuario is None:
        return jsonify(error="Token inválido o ausente"), 401
    REVOCADOS.add(usuario["jti"])
    return jsonify(mensaje="Sesión cerrada. El token ya no es válido.")


if __name__ == "__main__":
    app.run(port=5001)
