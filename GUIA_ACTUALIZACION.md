# GUÍA DE ACTUALIZACIÓN — Portafolio Gabriel Hernández

## Estructura del proyecto

```
C:\Portafolio\
├── content\
│   ├── blog\              ← Tus investigaciones / artículos
│   ├── pages\             ← Páginas fijas (Sobre mí, Proyectos)
│   └── images\            ← Tus imágenes (foto, favicon, etc.)
├── pelicanconf.py          ← Configuración principal del sitio
└── .github\workflows\      ← Despliegue automático a GitHub Pages
```

---

## 1. Cómo publicar una nueva investigación

1. Crea un archivo en `content/blog/` con el formato:
   ```
   YYYY-MM-DD-titulo-corto.md
   ```
   Ejemplo: `2026-06-01-inteligencia-artificial-economia.md`

2. Copia esta plantilla al inicio del archivo:

   ```yaml
   ---
   title: "Título de tu investigación"
   date: 2026-06-01
   category: Investigaciones
   tags: etiqueta1, etiqueta2, etiqueta3
   slug: titulo-de-tu-investigacion
   lang: es
   status: published
   ---
   ```

3. Escribe el contenido en Markdown debajo.

4. Sube a GitHub:

   ```powershell
   cd C:\Portafolio
   git add content/blog/
   git commit -m "feat: nueva investigacion - TITULO"
   git push
   ```

5. Espera 2-3 minutos a que GitHub Actions lo publique.

---

## 2. Cómo agregar un nuevo proyecto

1. Edita el archivo `content/pages/proyectos.md` y agrega una nueva sección:

   ```markdown
   ---

   ## Nombre del proyecto

   Descripción breve del proyecto.

   **Tecnologías:** Python · Pandas · ...
   [Ver en GitHub](https://github.com/gabohndz/tu-repo)
   ```

2. También puedes crear una página independiente en `content/pages/mi-proyecto.md` con su propia URL.

---

## 3. Cómo cambiar tu foto de perfil

1. Coloca tu imagen en `content/images/tu-foto.jpeg`
2. Si cambias el nombre o extensión, actualiza esta línea en `pelicanconf.py`:

   ```python
   AUTHOR_META = {
       "gabriel hernández": {
           "image": "/images/tu-nuevo-nombre.jpeg",  # <-- Aquí
       }
   }
   ```

---

## 4. Cómo cambiar la imagen de fondo del header

En `pelicanconf.py` busca `HEADER_COVER` y cámbialo:

```python
HEADER_COVER = "https://images.unsplash.com/photo-NUEVO-ID?w=1600&q=80"
```

Busca fotos gratis en https://unsplash.com

---

## 5. Cómo cambiar redes sociales o email

En `pelicanconf.py` busca la sección `SOCIAL`:

```python
SOCIAL = (
    ("LinkedIn", "https://linkedin.com/in/tu-perfil"),
    ("GitHub", "https://github.com/gabohndz"),
    ("Email", "mailto:tu-email@ejemplo.com"),
)
```

---

## 6. Cómo actualizar el sitio (comandos rápidos)

Ver cambios locales antes de publicar:

```powershell
cd C:\Portafolio
.\venv\Scripts\pelican content -s pelicanconf.py
```

Publicar en GitHub:

```powershell
cd C:\Portafolio
git add .
git commit -m "descripcion de tus cambios"
git push
```

---

## 7. Archivos clave que NO debes modificar

| Archivo | Razón |
|---------|-------|
| `.github/workflows/deploy.yml` | Controla el despliegue automático |
| `themes/attila/` | Tema del sitio (mejor no tocarlo) |
| `publishconf.py` | Configuración de producción |
| `venv/` | Entorno virtual de Python |

---

## 8. Archivos que SÍ puedes modificar

| Archivo | Para qué |
|---------|----------|
| `pelicanconf.py` | Configuración general del sitio |
| `content/pages/sobre-mi.md` | Tu perfil y biografía |
| `content/pages/proyectos.md` | Lista de proyectos |
| `content/extras/custom-overlay.css` | Estilos visuales personalizados |
