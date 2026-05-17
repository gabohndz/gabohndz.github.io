# Configuración principal de Pelican
# ====================================
# v1.0 - Primer despliegue

# --- Información del sitio ---
SITENAME = "Gabriel Hernández | Economista"
SITEURL = "https://gabohndz.github.io"
SITETITLE = "Gabriel Hernández"
SITESUBTITLE = "Economista · Análisis de datos · Investigación"
SITEDESCRIPTION = "Portafolio personal de investigación económica, análisis de datos y proyectos de automatización."
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
    ("LinkedIn", "https://linkedin.com/in/gabohndz"),
    ("GitHub", "https://github.com/gabohndz"),
    ("Email", "mailto:gabriel@ejemplo.com"),
)
LINKS = (
    ("LinkedIn", "https://linkedin.com/in/gabohndz"),
    ("GitHub", "https://github.com/gabohndz"),
)

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

# --- Tema (Flex) ---
THEME = "themes/flex"
SITETITLE = "Gabriel Hernández"
MAIN_MENU = True
MENUITEMS = (
    ("Inicio", "/"),
    ("Investigaciones", "/category/investigaciones/"),
    ("Proyectos", "/pages/proyectos/"),
    ("Sobre mí", "/pages/sobre-mi/"),
)
HOME_HIDE_TAGS = True

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
