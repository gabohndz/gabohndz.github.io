title: Proyectos
slug: proyectos
lang: es
date: 2026-05-23
status: published

Aquí están los proyectos que he desarrollado. Cada uno es un producto real, en producción y accesible online.

<style>
.project-card {
  background: #fff;
  border: 1px solid #e8e0d8;
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 40px;
  transition: box-shadow 0.3s, transform 0.3s;
}
.project-card:hover {
  box-shadow: 0 12px 40px rgba(0,0,0,0.08);
  transform: translateY(-3px);
}
.project-card-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
}
.project-screenshot {
  background: #f5f2ed;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  min-height: 280px;
}
.project-screenshot img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s;
}
.project-card:hover .project-screenshot img {
  transform: scale(1.03);
}
.project-info {
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.project-info h3 {
  font-size: 1.85rem;
  font-weight: 700;
  margin-bottom: 8px;
  line-height: 1.2;
}
.project-sub {
  color: #1a6b5a;
  font-weight: 600;
  font-size: 1.05rem;
  margin-bottom: 14px;
}
.project-info p {
  color: #4a4238;
  font-size: 1.1rem;
  line-height: 1.7;
  margin-bottom: 18px;
}
.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 18px;
}
.project-tags span {
  background: #f0ece6;
  color: #4a4238;
  padding: 4px 14px;
  border-radius: 14px;
  font-size: 0.85rem;
  font-weight: 500;
}
.project-links {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}
.project-links a {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.2s;
}
.project-links a.primary {
  background: #1a6b5a;
  color: #fff;
}
.project-links a.primary:hover {
  background: #145a4a;
  transform: translateY(-1px);
}
.project-links a.secondary {
  border: 1px solid #e0d8cf;
  color: #1c1816;
}
.project-links a.secondary:hover {
  border-color: #1a6b5a;
  color: #1a6b5a;
}
@media (max-width: 768px) {
  .project-card-inner { grid-template-columns: 1fr; }
  .project-screenshot { min-height: 200px; }
  .project-info { padding: 24px; }
}
</style>

<!-- ========== ECU SOLUCIONES ========== -->
<div class="project-card">
  <div class="project-card-inner">
    <div class="project-screenshot">
      <a href="https://ecusoluciones.com" target="_blank" rel="noopener">
        <img src="/images/ecusoluciones.png" alt="EcuSoluciones preview" style="width:100%;height:100%;object-fit:cover;">
      </a>
    </div>
    <div class="project-info">
      <h3>EcuSoluciones</h3>
      <div class="project-sub">Landing page · Lead generation · EN/ES</div>
      <p>Agencia digital con servicios de landing pages, gestión de bases de datos y email marketing. Diseño editorial único, toggle de idioma Español/Inglés, SEO con schema.org y Google Analytics integrado.</p>
      <div class="project-tags">
        <span>HTML5</span>
        <span>CSS3</span>
        <span>JavaScript</span>
        <span>SEO</span>
        <span>Google Analytics</span>
        <span>GitHub Pages</span>
      </div>
      <div class="project-links">
        <a href="https://ecusoluciones.com" target="_blank" rel="noopener" class="primary">🌐 Ver sitio</a>
        <a href="https://github.com/gabohndz/ecusoluciones" target="_blank" rel="noopener" class="secondary">🐙 Código</a>
      </div>
    </div>
  </div>
</div>

<!-- ========== ESTUDIO DE MERCADO GRATIS ========== -->
<div class="project-card">
  <div class="project-card-inner">
    <div class="project-screenshot">
      <a href="https://estudiodemercadogratis.com" target="_blank" rel="noopener">
        <img src="/images/estudio-mercado.png" alt="Estudio de Mercado Gratis preview" style="width:100%;height:100%;object-fit:cover;">
      </a>
    </div>
    <div class="project-info">
      <h3>Estudio de Mercado Gratis</h3>
      <div class="project-sub">Lead magnet · Automatización · EN/ES</div>
      <p>Plataforma que ofrece estudios de mercado personalizados gratuitos a emprendedores. Formulario inteligente con auto-fill, integración con Google Apps Script y Sheets, toggle EN/ES y diseño optimizado para conversión.</p>
      <div class="project-tags">
        <span>HTML5</span>
        <span>CSS3</span>
        <span>JavaScript</span>
        <span>Google Apps Script</span>
        <span>Google Sheets</span>
        <span>SEO</span>
      </div>
      <div class="project-links">
        <a href="https://estudiodemercadogratis.com" target="_blank" rel="noopener" class="primary">🌐 Ver sitio</a>
        <a href="https://github.com/gabohndz/an-lisis-de-mercado-gratis" target="_blank" rel="noopener" class="secondary">🐙 Código</a>
      </div>
    </div>
  </div>
</div>

> Cada proyecto es real, está en producción y puedes interactuar con él directamente.

---

> **💡 Nota:** Todos estos proyectos los he desarrollado en mi tiempo libre, por pura pasión por crear cosas nuevas, sin recibir nada económico a cambio. Simplemente porque quiero y disfruto hacerlo 😊

<!-- ========== AUTOSHORTS — INTERFACES COMFYUI ========== -->
<div class="project-card">
  <div class="project-card-inner">
    <div class="project-screenshot">
      <img src="/images/autoshorts-interfaces.webp" alt="AutoShorts Interfaces preview" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div class="project-info">
      <h3>AutoShorts — Interfaces de IA Local</h3>
      <div class="project-sub">Generación de imágenes · Animaciones · Social Canvas</div>
      <p>Interfaces gráficas con Gradio para generar imágenes usando modelos locales vía ComfyUI. Incluye <strong>txt2img</strong>, <strong>img2img</strong>, animaciones con <strong>AnimateDiff</strong>, comparador de modelos y un <strong>Social Canvas</strong> tipo Canva para crear contenido para redes sociales con fondos generados por IA. Todo corriendo 100% local con Pony Diffusion V6 XL.</p>
      <div class="project-tags">
        <span>Python</span>
        <span>Gradio</span>
        <span>ComfyUI</span>
        <span>Pony Diffusion</span>
        <span>AnimateDiff</span>
        <span>IA Local</span>
      </div>
      <div class="project-links">
        <a href="https://drive.google.com/file/d/1mhsA4WE7fufK6xhMOov7mISeyVyZcrsI/view?usp=sharing" target="_blank" rel="noopener" class="primary">🖼️ Ver imagen de ejemplo</a>
        <a href="https://drive.google.com/file/d/1mhsA4WE7fufK6xhMOov7mISeyVyZcrsI/view?usp=sharing" target="_blank" rel="noopener" class="secondary">🔗 Google Drive</a>
      </div>
    </div>
  </div>
</div>

<!-- ========== AUTOSHORTS — CREADOR DE CÓMICS ========== -->
<div class="project-card">
  <div class="project-card-inner">
    <div class="project-screenshot">
      <img src="/images/autoshorts-comic.jpg" alt="Creador de Cómics preview" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div class="project-info">
      <h3>Creador Automático de Cómics</h3>
      <div class="project-sub">Formato propio · YAML → Cómic · Consistencia visual</div>
      <p>Sistema que convierte archivos <strong>YAML</strong> en cómics completos con personajes consistentes, diálogos con estilo (grito, susurro, pensamiento), efectos de sonido y maquetado automático de páginas. Cada personaje mantiene su apariencia gracias a un sistema de <strong>seeds fijos</strong> y cache de referencias. Incluye ejemplos como un comic de Mario Bros y uno cyberpunk.</p>
      <div class="project-tags">
        <span>Python</span>
        <span>YAML</span>
        <span>ComfyUI</span>
        <span>Pillow</span>
        <span>PDF</span>
        <span>IA Generativa</span>
        <span>Pipeline</span>
      </div>
      <div class="project-links">
        <a href="https://drive.google.com/file/d/1BKVbGLRfBC1S_gtvA3ft8kx_Oi4kp9zJ/view?usp=sharing" target="_blank" rel="noopener" class="primary">🦸 Ver comic de ejemplo (PDF)</a>
        <a href="https://drive.google.com/file/d/1BKVbGLRfBC1S_gtvA3ft8kx_Oi4kp9zJ/view?usp=sharing" target="_blank" rel="noopener" class="secondary">🔗 Google Drive</a>
      </div>
    </div>
  </div>
</div>

<!-- ========== AUTOSHORTS — EDITOR DE SHORTS ========== -->
<div class="project-card">
  <div class="project-card-inner">
    <div class="project-screenshot">
      <img src="/images/autoshorts-short.jpg" alt="Editor de Shorts preview" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div class="project-info">
      <h3>Editor Automático de Shorts</h3>
      <div class="project-sub">Video · Voz · Música · Automatización total</div>
      <p>Convierte guiones de texto en <strong>shorts</strong> listos para TikTok, YouTube e Instagram. Descarga imágenes automáticamente por palabras clave, genera voz con <strong>IA</strong> (F5-TTS / XTTS), añade música de fondo con emoción seleccionable, subtítulos automáticos, efecto <strong>Ken Burns</strong> y sincronización perfecta. Todo desde un solo comando.</p>
      <div class="project-tags">
        <span>Python</span>
        <span>MoviePy</span>
        <span>Whisper</span>
        <span>NVIDIA API</span>
        <span>TTS</span>
        <span>Automatización</span>
        <span>IA</span>
      </div>
      <div class="project-links">
        <a href="https://drive.google.com/file/d/1oiCC8A8ZqWvikouNMq3k-UxLdtJHv9-Y/view?usp=sharing" target="_blank" rel="noopener" class="primary">🎬 Ver short de ejemplo</a>
        <a href="https://drive.google.com/file/d/1oiCC8A8ZqWvikouNMq3k-UxLdtJHv9-Y/view?usp=sharing" target="_blank" rel="noopener" class="secondary">🔗 Google Drive</a>
      </div>
    </div>
  </div>
</div>