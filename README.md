# jwt-lab-zevallos

Laboratorio de **seguridad en APIs y JSON Web Tokens (JWT)** del curso Desarrollo de Software Seguro (UPC), profesor Diego Gárate.

Una API en Python + Flask con autenticación por JWT. Se construye primero una versión **vulnerable**, se ataca de tres formas y luego se corrige hasta que los ataques fallan.

## Los tres ataques

1. **Token sin firma (`alg: none`):** el servidor confía en el algoritmo que declara el propio token.
2. **Secreto débil:** el secreto de firma es corto y está escrito en el código, así que se puede crackear.
3. **Token eterno:** el token no caduca y el cierre de sesión no lo invalida.

## La versión segura corrige

- El algoritmo lo fija el servidor, nunca el token.
- Secreto largo y aleatorio, fuera del código (`.env`).
- Expiración de 15 minutos y revocación por `jti`; el rol se consulta en cada petición.

## Cómo ejecutar

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

> Todo el código corre en local. Ataca únicamente esta aplicación, que es tuya.
