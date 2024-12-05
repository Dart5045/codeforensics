# Proyecto: CodeForensics - Práctica de Git, GitHub y Docker

Este proyecto es una práctica donde aprenderás a trabajar con **Git**, **GitHub** y **Docker** mientras construyes una aplicación sencilla en **Django**. El objetivo es crear una aplicación que maneje datos sensibles y utilizar herramientas como **SonarQube** para analizar el código y detectar errores.

## Historia del Proyecto

La empresa ficticia **DataSafe Inc.** ha solicitado la creación de una aplicación para gestionar información sensible de sus clientes. Sin embargo, han encontrado un error en el código que puede exponer datos de forma incorrecta. Como parte del proceso de calidad, se requiere que se corrijan los errores y se realicen pruebas de seguridad.

### Instrucciones para el Profesor

1. **Construir la Aplicación Django:**
   - Crea una nueva aplicación Django llamada `sensitive_data`.
   - Introduce un error intencionado en el código de la vista `sensitive_info` (índice fuera de rango) para que los estudiantes puedan encontrarlo.
   - Sube el proyecto a GitHub y asegúrate de que los estudiantes tengan acceso al repositorio.
   - Agrega un **Dockerfile** y un archivo `docker-compose.yml` para que los estudiantes puedan ejecutar la aplicación en contenedores Docker.

2. **Configurar SonarQube (opcional):**
   - Si deseas integrar SonarQube para analizar el código, instala SonarQube usando Docker.
   - Asegúrate de que los estudiantes puedan acceder a SonarQube para revisar los errores del código.

## Instrucciones para los Estudiantes

### **1. Clonar el Repositorio**

Clona el repositorio desde GitHub:
```bash
git clone https://github.com/dart5045/codeforensics.git
cd codeforensics