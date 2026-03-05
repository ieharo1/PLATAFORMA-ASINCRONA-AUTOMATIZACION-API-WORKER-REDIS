# Plataforma Asíncrona de Automatización con API, Worker y Redis

Sistema orientado a colas para procesamiento en segundo plano, con Nginx como capa de entrada y Redis como broker.

## Descripción

Este entorno simula una plataforma de automatización de tareas musicales donde las solicitudes se encolan y un worker las procesa de manera desacoplada.

## ¿Qué hace este proyecto?

- Expone API para recibir tareas (`/api/play`).
- Encola trabajos en Redis.
- Ejecuta un worker independiente para consumo de cola.
- Publica todo detrás de Nginx como gateway.

## Características Principales

| Característica | Descripción |
|---|---|
| Arquitectura asíncrona | API rápida sin bloquear procesos largos |
| Cola persistente en memoria | Redis como broker central |
| Worker dedicado | Procesamiento desacoplado |
| Edge único | Nginx expone el sistema completo |

## Stack Tecnológico

- Python Flask
- Redis
- Nginx
- Docker Compose

## Instalación y Uso

### Levantar entorno

```bash
docker compose up -d --build
```

### Probar

- Health: `http://localhost:8083/api/health`
- Cola de trabajo (POST): `http://localhost:8083/api/play`

## Variables de Entorno

- `NGINX_PORT`: puerto externo del gateway.

## Estructura del Proyecto

```text
.
├── Dockerfile
├── docker-compose.yml
├── .env
├── app/
│   ├── api.py
│   ├── worker.py
│   └── requirements.txt
└── nginx/
    └── default.conf
```

## Casos de Uso

- Procesamiento de jobs en background.
- Automatizaciones que requieren cola de tareas.
- Integraciones por eventos con baja latencia de respuesta.

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
