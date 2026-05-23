# Configuración principal de Pelican
# ====================================
# v1.0 - Primer despliegue

# --- Información del sitio ---
SITENAME = "Gabriel Hernández | Economista & Desarrollador Web"
SITEURL = "https://gabohndz.github.io"
SITETITLE = "Gabriel Hernández"
SITESUBTITLE = "Economista · Desarrollador Web · Análisis de Datos · Estrategia de Mercado"
SITEDESCRIPTION = "Portafolio profesional: investigación económica, desarrollo web con Python, landing pages, análisis de datos y automatización. Transformo números en soluciones digitales."
SITELOGO = "/images/logo.png"
FAVICON = "/images/favicon.ico"
AUTHOR = "Gabriel Hernández"

# --- Idioma y huso horario ---
TIMEZONE = "America/Mexico_City"
DEFAULT_LANG = "es"
LOCALE = ("es_MX", "es_ES", "es")

# --- Rutas y URLs ---
PATH = "content"
OUTPUT_PATH = "output"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["blog"]
STATIC_PATHS = ["images", "documents", "extras"]

# URLs limpias para SEO
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "categoria/{slug}/"
CATEGORY_SAVE_AS = "categoria/{slug}/index.html"
TAG_URL = "etiqueta/{slug}/"
TAG_SAVE_AS = "etiqueta/{slug}/index.html"
TAGS_URL = "etiquetas/"
CATEGORIES_URL = "categorias/"
ARCHIVES_URL = "archivos/"
AUTHORS_URL = "autores/"

# --- Paginación ---
DEFAULT_PAGINATION = 6
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

# --- Taxonomías ---
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "Investigaciones"
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True

# --- Feeds (RSS/Atom) ---
FEED_ALL_ATOM = "feeds/todos.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Social / Redes ---
SOCIAL = (
    ("LinkedIn", "https://linkedin.com/in/gabriel-hernandez-mota-9594821a5/"),
    ("GitHub", "https://github.com/gabohndz"),
    ("Email", "mailto:gabrielhernandez@ecusoluciones.com"),
    ("WhatsApp", "https://wa.me/593987812178"),
)
LINKS = (
    ("LinkedIn", "https://linkedin.com/in/gabriel-hernandez-mota-9594821a5/"),
    ("GitHub", "https://github.com/gabohndz"),
)

# --- Avatar / Foto de perfil ---
AUTHOR_META = {
    "gabriel hernández": {
        "image": "/images/tu-foto.jpeg",
        "name": "Gabriel Hernández",
        "bio": "Economista apasionado por el análisis de datos y la automatización.",
    }
}

# --- CSS personalizado ---
CSS_OVERRIDE = ["extras/custom-overlay.css"]

# --- Plugins ---
PLUGIN_PATHS = []
PLUGINS = [
    "pelican.plugins.seo",  # SEO optimizado
]

# --- SEO Plugin Config ---
SEO_REPORT = False
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = True

# --- Tema (Attila - estilo Medium/revista) ---
THEME = "themes/attila"
HEADER_COVER = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1600&q=80"
HEADER_COLOR = "#1a2a3a"
SITE_DESCRIPTION = SITEDESCRIPTION
SHOW_PAGES_ON_MENU = False
SHOW_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ("Inicio", "/"),
    ("Investigaciones", "/categoria/investigaciones/"),
    ("Proyectos", "/pages/proyectos/"),
    ("Sobre mí", "/pages/sobre-mi/"),
)

# --- Pygments (colores de código) ---
PYGMENTS_STYLE = "monokai"

# --- Markdown ---
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "¶"},
    },
    "output_format": "html5",
}

# --- Otras opciones útiles ---
DEFAULT_METADATA = {
    "status": "published",
}
DELETE_OUTPUT_DIRECTORY = True
TYPOGRAPHIC_REPLACEMENTS = True
SUMMARY_MAX_LENGTH = 50

# --- Caché ---
CACHE_PATH = ".cache"
LOAD_CONTENT_CACHE = False
