# Mi configuración de Claude Code

## Reglas de eficiencia
- Respóndeme siempre en español
- Usa la menor cantidad de tokens posible
- Respuestas directas y accionables
- Muéstrame un plan antes de tareas largas

## Optimización de tokens
1. Think before acting. Read existing files before writing code.
2. Be concise in output but thorough in reasoning.
3. Prefer editing over rewriting whole files.
4. Do not re-read files you have already read unless the file may have changed.
5. Test your code before declaring done.
6. No sycophantic openers or closing fluff.
7. Keep solutions simple and direct.
8. User instructions always override this file.

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

## Trucos de productividad
- Usar "ultrathink" en prompts para activar pensamiento profundo
- Combinar /plan + ultrathink para tareas complejas
- Pedir sub-agentes para tareas con partes independientes paralelas
- Correr /init en proyectos nuevos para generar contexto automático
- Prompt para sub-agentes: "usa sub-agentes separados en paralelo para cada parte independiente"

## Sistema de memoria entre sesiones
- Antes de cerrar sesión, guardar resumen en PROGRESS.md
- Al iniciar sesión nueva, leer PROGRESS.md para retomar donde se quedó
- Organizar notas en: Completado / En progreso / Pendiente / Decisiones
- Actualizar PROGRESS.md después de cada bloque significativo de trabajo

## Reglas de calidad
- SIEMPRE verificar trabajo antes de darlo por terminado
- Leer código existente antes de implementar cambios
- No implementar nada sin estar 100% seguro — investigar primero o preguntar

## Plugin esencial — context-mode

Reduce hasta 98% el contexto consumido por Claude Code.

Instalación:
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode

Verificar instalación:
ctx doctor

Ver métricas de ahorro:
ctx stats

Actualizar:
ctx upgrade

Cómo funciona:
- Ejecuta comandos en sandbox (datos crudos nunca tocan el contexto)
- Indexa resultados pesados con BM25 (315 KB → 5.4 KB)
- Guarda estado de sesión en SQLite para restaurar automáticamente
- Requiere Claude Code 2.0.22+ y Node 18+

## Regla de las 2 correcciones (oficial de Anthropic)

- Máximo 2 correcciones por tema en la misma sesión
- Si falla después de 2 intentos → /clear y empezar limpio
- Nunca repetir el mismo prompt — reescribir con lo aprendido
- /clear: borra memoria contaminada (mejor herramienta)
- /compact: comprime sesión larga sin perder el hilo
- Esc: para a Claude en medio de una tarea
- Esc+Esc o /rewind: regresa a un punto anterior

## Checklist de prompts efectivos

- ¿Dije exactamente QUÉ quiero?
- ¿Di el contexto necesario? (archivos, errores, tecnologías)
- ¿Le dije CÓMO verificar que funciona?
- ¿Incluí lo aprendido de errores anteriores?
- ¿Un compañero sin contexto entendería la instrucción?

## Recomendaciones oficiales Anthropic

- Dale a Claude forma de verificar su trabajo (tests, ejemplos)
- Explorar primero → planear → ejecutar al final
- Limpiar contexto entre tareas diferentes con /clear
- Usar subagentes para investigar sin contaminar contexto
- Darle un rol: "Eres experto en X"
- Usar 3-5 ejemplos del resultado esperado
- CLAUDE.md corto — si es muy largo Claude ignora la mitad

## 5 errores que queman el plan

1. CORRECCIONES: No mandar mensaje nuevo para corregir
   → Editar el mensaje original y regenerar

2. CHATS LARGOS: No acumular +20 mensajes en el mismo chat
   → Pedir resumen → abrir chat nuevo → pegar resumen

3. PREGUNTAS SEPARADAS: No mandar preguntas una por una
   → Juntar todo en un solo mensaje

4. FUNCIONES ENCENDIDAS: Apagar MCPs y conectores
   que no se estén usando en el momento

5. HORAS PICO: Evitar usar Claude de 7am a 1pm
   hora centro México — cuesta el doble
   → Usar temprano o de noche

## 5 configuraciones para rendir el doble

1. PROYECTOS: Subir archivos frecuentes UNA vez en un Project
   → No repetir los mismos archivos en cada chat

2. PERFIL: Configurar en Settings → Profile quién eres
   → Claude lo aplica en todas las conversaciones automáticamente

3. HAIKU PARA LO SIMPLE:
   → Haiku: correcciones, traducciones, listas, preguntas directas
   → Sonnet: código, análisis, estrategias, contenido complejo

4. REPARTIR USO EN 2 BLOQUES:
   → Claude tiene ventana de 5 horas — lo gastado se libera después
   → Bloque 1 mañana + Bloque 2 (5 horas después) = duplicas el plan

5. USO EXTRA CON LÍMITE:
   → Activar en Settings → Usage → Extra Usage
   → Poner límite bajo ($5-10 USD) como red de seguridad

## 4 Superpoderes — MCPs esenciales

### 1. Supadata — Transcribir videos
Transcribe videos de YouTube, TikTok, Instagram + métricas
Instalación .mcp.json:
npx -y supadata-mcp
API key: supadata.ai
Env: SUPADATA_API_KEY

### 2. Apify — Scraping de internet
Extrae datos de cualquier página web, redes sociales, precios
Instalación .mcp.json:
npx -y @anthropic-ai/mcp-apify
API key: apify.com → Settings → Integrations
Env: APIFY_TOKEN

### 3. Last 30 Days — Investigador de noticias
Investiga noticias de los últimos 30 días de cualquier nicho
Instalación:
claude install-skill https://github.com/mvanhorn/last30days-skill
No requiere API key

### 4. Playwright CLI — Navegador propio
Claude navega la web, toma screenshots, llena formularios
Usa menos tokens que Chrome integration
Instalación:
npm install -g @anthropic-ai/claude-code-playwright
npx playwright install chromium

### Flujo combinado para análisis de competencia:
"Usa Supadata para transcribir videos de [canal],
Apify para extraer sus redes sociales,
Last 30 Days para noticias del nicho,
Playwright para screenshots de su web"

### Tips:
- Verificar instalación con /mcp después de cada uno
- Usar Plan Mode (Shift+Tab) para tareas que combinan varios MCPs
- Playwright > Chrome para páginas web simples (menos tokens)

## 5 Skills esenciales — Tu equipo de trabajo

### Flujo correcto (en orden):
1. Find Skills → buscar si ya existe en skillsmp.com
2. Grill Me → interrogar la idea antes de construir
3. Write a PRD → generar el plano completo del proyecto
4. Skill Creator o Write a Skill → crear skill si no existe

### Instalación de las 4 skills de un jalón:
claude install-skill https://github.com/anthropics/skills/tree/main/skills/skill-creator && npx skills@latest add mattpocock/skills/write-a-skill && npx skills@latest add mattpocock/skills/grill-me && npx skills@latest add mattpocock/skills/write-a-prd

### Cuándo usar cada una:
- Skill Creator: automatizar tareas repetitivas del día a día
- Write a Skill: crear skills profesionales para compartir
- Find Skills: skillsmp.com — 66k+ skills ya hechas
- Grill Me: /grill-me — interroga tu idea antes de construir
- Write a PRD: /write-a-prd — genera plano completo del proyecto

### Para agentes de automatización por cliente:
1. /grill-me → validar la idea del agente
2. /write-a-prd → generar el plan técnico
3. Skill Creator → empaquetar el agente como skill reutilizable

## /loop — Automatización programada

### Sintaxis:
/loop [intervalo] [prompt]
Intervalos: 5m, 2h, 1d, daily, weekly

### Comandos esenciales:
/loop 5m [prompt]          → cada 5 minutos
/loop 2h [prompt]          → cada 2 horas
/loop daily [prompt]       → diario
/loop weekly [prompt]      → semanal
/loop 20m /skill-name      → loop con skill
/rc                        → llevar sesión al celular
claude remote-control      → control remoto desde teléfono
/schedule                  → programador visual (Desktop)

### Workflows clave para agentes de clientes:

ONBOARDING AUTOMÁTICO:
/loop 1h cuando llegue nuevo signup, envía email de bienvenida,
crea entrada en spreadsheet, agenda kickoff en Calendar,
notifica al equipo en Slack

CRM Y PIPELINE:
/loop 2h revisa deals sin actividad en 3 días,
genera emails de seguimiento y actualiza el pipeline

REPORTE DIARIO:
/loop daily a las 9am jala ingresos de ayer,
compara con semana anterior y marca anomalías

MONITOREO DE ERRORES:
/loop 1h revisa logs de errores, analiza stack trace,
identifica causa y crea PR con fix para bugs simples

CODE REVIEW:
/loop 2h busca nuevos PRs en GitHub, analiza seguridad
y performance, publica resumen como comentario

DIGEST SEMANAL DEL EQUIPO:
/loop weekly cada viernes 4pm compila PRs completados,
issues cerrados y deploys — publica en Slack y guarda en Drive

### Nota importante:
/loop necesita que Claude Code esté corriendo
Para automatización 24/7 sin tu computadora → usar /schedule en Cloud

## Flujo para crear agentes por cliente

### Flujo completo (idea → agente funcionando):
1. Shift+Tab → activar Plan Mode
2. Describir el agente (tarea, triggers, output esperado)
3. Claude investiga el proyecto y entrega un plan
4. Revisar y ajustar el plan
5. Shift+Tab → Auto Mode → Claude construye todo
6. /loop para programar el agente automáticamente

### Prompt de descubrimiento (cuando el cliente no sabe qué necesita):
"Hazme preguntas sobre mi día a día y mis tareas repetitivas.
Basándote en mis respuestas, sugiere 3 agentes que automaticen
las tareas más tediosas. Para cada uno incluye: qué haría,
qué herramientas necesita y cuánto tiempo ahorraría por semana."

### Estructura de prompt para crear agente:
"Quiero crear un agente que [tarea específica].
El agente debe:
1. [acción 1]
2. [acción 2]
3. [resultado esperado]
Investiga mi proyecto y diseña un plan completo."

### MCPs que Claude instala automáticamente:
- Gmail MCP: agentes de email
- GitHub MCP: agentes de code review
- Browser MCP: automatización web
Comando: claude mcp add [nombre] -- npx -y @anthropic/[nombre]

### De herramienta a empleado digital:
- Agente sin /loop = herramienta manual
- Agente con /loop = empleado que trabaja solo
- Agente con /schedule = empleado 24/7 en la nube
