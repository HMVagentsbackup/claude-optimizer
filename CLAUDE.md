# Mi configuración de Claude Code

## Reglas de eficiencia
- Respóndeme siempre en español
- Usa la menor cantidad de tokens posible
- Respuestas directas y accionables
- Muéstrame un plan antes de tareas largas

## Optimización de tokens
- Usar /clear entre tareas no relacionadas
- Evitar pegar código largo completo, solo mostrar la parte relevante
- Preferir respuestas en bullets cortos, no párrafos
- Usar Haiku para tareas simples, Sonnet para construcción, Opus solo para decisiones importantes
- Nunca repetir contexto que ya está en el CLAUDE.md
- Escribir prompts específicos, no vagos

## Mejores prácticas
- Iniciar cada sesión con /init para que Claude lea el contexto
- Usar /plan antes de tareas complejas
- Mantener conversaciones cortas y enfocadas en una sola tarea
- Limpiar contexto con /clear cuando cambias de tema
- Describir el resultado esperado, no el proceso

## Sobre mí y mi trabajo
- Construyo agentes de automatización para diferentes departamentos y clientes
- Mi objetivo es convertirlo en un producto vendible
- Trabajo en múltiples proyectos simultáneamente
- Prioriza soluciones escalables y reutilizables
- Siempre piensa en cómo esto puede aplicarse a otros clientes

## Conocimiento de agentes y automatización
- Usar /plan antes de crear cualquier agente nuevo
- Separar agentes por departamento en carpetas distintas
- Usar subagentes para tareas paralelas independientes
- MCPs recomendados: Firecrawl, Playwright, Apify
- Instalar skills con: npx -y [nombre-del-skill]
- Usar /loop para tareas programadas recurrentes
- Usar /schedule para agentes que corren en la nube
- YOLO mode para automatización sin interrupciones
- Mantener un CLAUDE.md por cliente/proyecto
- Skills esenciales: Skill Creator, SuperPowers, GSD

## MCPs esenciales para agentes
- Firecrawl: scraping y lectura de URLs
- Playwright: control de navegador web
- Apify: extracción de datos de redes sociales
- Zapier MCP: conectar 6000+ apps sin código
- GitHub MCP: gestión de repositorios
- Google Drive MCP: documentos y archivos
- Instalación: Claude Code instala MCPs automáticamente con el prompt correcto

## Modelos correctos por tarea
- Haiku: preguntas simples, clasificación, resúmenes
- Sonnet: construir agentes, escribir código, tareas complejas
- Opus: decisiones críticas, arquitectura de sistemas, análisis profundo
- Regla: empieza con Sonnet, sube a Opus solo si es necesario
