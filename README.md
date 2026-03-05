# Automatizador-de-canciones - Nginx + API + Worker + Redis

Configuracion de backend asincrono para automatizacion de playlists con cola de tareas.

## Arquitectura

- `songs-nginx`: gateway publico.
- `songs-api`: endpoint para encolar canciones.
- `songs-worker`: consumidor de cola.
- `redis`: broker de mensajes.

## Levantar

```bash
docker compose up -d --build
```

API base: `http://localhost:8083/api/health`

## Variables

- `NGINX_PORT`: puerto externo del gateway.

## Valor para perfil

- Patron real de procesamiento asincrono.
- Separacion de responsabilidades API/Worker.

---

## ‍ Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack · Automatización · Data**

-  Email: zackharo1@gmail.com
-  WhatsApp: 098805517
-  GitHub: https://github.com/ieharo1
-  Portafolio: https://ieharo1.github.io/portafolio-isaac.haro/

---

##  Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.
