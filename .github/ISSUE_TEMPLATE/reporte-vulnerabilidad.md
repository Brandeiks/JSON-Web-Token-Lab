---
name: Reporte de vulnerabilidad
about: Reporta una vulnerabilidad de seguridad encontrada en este repositorio
title: "[VULN] "
---

# Reporte de vulnerabilidad: título corto y descriptivo

| Campo | Valor |
|---|---|
| Repositorio | `usuario/jwt-lab-apellido` |
| Archivo afectado | `reto/app_reto.py` |
| Endpoint | `GET /admin` |
| Severidad | Crítica / Alta / Media / Baja |
| Reportado por | @tu-usuario-de-github |

## Resumen
Una o dos oraciones: qué puede hacer un atacante gracias a esta vulnerabilidad.

## Principio de diseño seguro violado
- [ ] Mediación completa
- [ ] Fail-safe defaults
- [ ] Mínimo privilegio
- [ ] Diseño abierto
- [ ] Otro:

## Código vulnerable
```python
# Pega aquí las líneas exactas donde está el problema
```

## Pasos para reproducir
1. Levantar la app: `python reto\app_reto.py`
2. Ejecutar el exploit: `python exploit.py`
3. Observar la respuesta de `/admin`

## Prueba de explotación
```python
# Pega aquí tu exploit.py
```
```text
Pega aquí la salida, por ejemplo: /admin -> 200 {...}
```

## Impacto
Qué datos o acciones quedan expuestos y quién podría aprovecharlo.

## Corrección propuesta
```python
# Cómo debería quedar el código
```
