# DOCUMENTACIÓN DEL PROYECTO

## Introducción
Este proyecto demuestra el uso de **Git, GitHub y Pandas** en el flujo de trabajo de un científico de datos.  
Se realiza el preprocesamiento completo del dataset *Titanic* para limpiar, codificar y normalizar la información.

---

## Comandos Git utilizados

| Comando | Descripción |
|----------|--------------|
| `git init` | Inicializa un nuevo repositorio local |
| `git remote add origin <URL>` | Conecta el repositorio local con GitHub |
| `git add .` | Agrega los archivos al área de preparación |
| `git commit -m "Mensaje"` | Registra los cambios con un mensaje |
| `git branch feature-preprocesamiento` | Crea una nueva rama de desarrollo |
| `git checkout feature-preprocesamiento` | Cambia a la rama creada |
| `git push origin feature-preprocesamiento` | Sube la rama al repositorio remoto |
| `git pull request` | Solicita fusión de ramas en GitHub |
| `git merge feature-preprocesamiento` | Fusiona la rama con la principal |
| `git branch -d feature-preprocesamiento` | Elimina la rama tras la fusión |

---

## Automatización (GitHub Actions)
Se puede crear un flujo sencillo `.github/workflows/python-app.yml` para ejecutar automáticamente el script en cada push:

```yaml
name: Python CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install pandas scikit-learn
      - name: Run preprocessing
        run: python preprocesamiento.py
