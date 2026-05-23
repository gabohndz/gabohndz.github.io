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
  font-size: 1.65rem;
  font-weight: 700;
  margin-bottom: 6px;
  line-height: 1.2;
}
.project-sub {
  color: #1a6b5a;
  font-weight: 600;
  font-size: 0.95rem;
  margin-bottom: 14px;
}
.project-info p {
  color: #4a4238;
  font-size: 1rem;
  line-height: 1.7;
  margin-bottom: 16px;
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
  font-size: 0.8rem;
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
  font-size: 0.9rem;
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