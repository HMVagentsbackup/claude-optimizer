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

## Canales — Telegram y Discord

### Para qué sirven:
Hablar con Claude Code desde Telegram o Discord
en vez de solo desde la terminal

### Telegram (más simple):
Requisito: instalar Bun → curl -fsSL https://bun.sh/install | bash

1. Crear bot en @BotFather → /newbot → copiar TOKEN
2. /plugin install telegram@claude-plugins-official
3. /telegram:configure TU_TOKEN
4. claude --channels plugin:telegram@claude-plugins-official
5. Emparejar: /telegram:access pair CODIGO
6. Seguridad: /telegram:access policy allowlist

Limitación: NO lee mensajes cuando Claude está apagado

### Discord (más poderoso):
1. discord.com/developers/applications → New Application
2. Bot → Message Content Intent → activar
3. Copiar token (solo se muestra una vez)
4. OAuth2 → URL Generator → invitar bot al servidor
5. /plugin install discord@claude-plugins-official
6. /discord:configure → pegar token
7. claude --channels plugin:discord@claude-plugins-official
8. Emparejar por DM

Ventaja: SÍ lee historial de mensajes anteriores

### Para clientes:
- Un bot por cliente/proyecto
- Siempre activar allowlist después de emparejar
- Discord para equipos (historial), Telegram para notificaciones rápidas

## Gbrain — Memoria permanente para Claude

Convierte una carpeta de notas en el cerebro de Claude.
Claude consulta su cerebro antes de cada respuesta.
Gratis, open source, corre local.

### Instalación automática (pegar en Claude Code):
"Ve al repositorio https://github.com/garrytan/gbrain
Lee el README y luego:
1. Instala Gbrain con bun globalmente
2. Inicializa con gbrain init
3. Importa mi carpeta de notas
4. Configura MCP en ~/.claude/server.json
5. Verifica con gbrain doctor --json"

### Instalación manual:
bun add -g github:garrytan/gbrain
gbrain init
gbrain import ~/mis-notas --no-embed
gbrain doctor --json

### Configurar en ~/.claude/server.json:
{
  "mcpServers": {
    "gbrain": {
      "command": "gbrain",
      "args": ["serve"]
    }
  }
}

### Para agentes de clientes:
- Crear una carpeta por cliente con sus notas, juntas y contexto
- Importar: gbrain import ~/clientes/nombre-cliente
- Claude recordará todo sobre ese cliente automáticamente
- Escalar a Supabase cuando supere 1,000 archivos:
  gbrain migrate --to supabase

### Integraciones automáticas:
- Correo, calendario, juntas grabadas
- Redes sociales
- Línea de voz (Claude contesta y guarda la plática)

## Piloto automático (instalar en desktop)

### YOLO Mode — Claude sin interrupciones:
claude --dangerously-skip-permissions
⚠️ SIEMPRE configurar hooks antes de activar

### Hooks de protección (~/.claude/settings.json):
Bloquean comandos peligrosos antes de ejecutarse
- exit 0 → Permitir
- exit 2 → Bloquear
- otro → Advertir y continuar
Comandos bloqueados por defecto: rm -rf, drop table

### GSD — Proyectos nuevos desde cero:
Instalación (desktop): npx get-shit-done-cc@latest
Comandos:
/gsd:new-project   → nuevo proyecto
/gsd:discuss-phase → definir qué construir
/gsd:plan-phase    → plan paso a paso
/gsd:execute-phase → ejecutar automáticamente
/gsd:verify-work   → verificar que funciona
/gsd:ship          → deploy

### Super Powers — Proyectos existentes:
Instalación (desktop): npx superpowers@latest init
Crea subagentes paralelos con contexto limpio
Flujo: Brainstorm → Design → Plan → Implement → Test → Review → Complete

### Flujo completo piloto automático:
1. Configurar hooks de protección
2. Activar YOLO Mode
3. Proyecto nuevo → GSD / Proyecto existente → Super Powers

## Dispatch — Control remoto desde el teléfono

Asigna tareas desde el teléfono y Claude las ejecuta
en tu computadora. Una sola conversación continua
sincronizada entre ambos dispositivos.

### Requisitos:
- Claude Desktop instalado (mac/Windows)
- App móvil Claude actualizada
- Plan Pro o Max
- Computadora encendida con Claude Desktop abierto

### Configuración:
1. Abrir Cowork en app móvil o desktop
2. Ir a Dispatch → Get started
3. Activar: acceso a archivos + mantener computadora despierta
4. Finish setup → listo

### Casos de uso para clientes:
- Extraer datos de Excel/Sheets sin estar en la compu
- Revisar emails y Slack → briefing desde el teléfono
- Crear presentaciones desde datos en Drive
- Organizar archivos y carpetas remotamente

### Ejemplo de prompt potente:
"Busca en mi carpeta Documentos todos los PDFs con
la palabra 'contrato'. Lista nombre, fecha y resumen
de una línea. Guárdalo como resumen-contratos.txt
en el escritorio."

### Limitaciones actuales:
- Computadora debe estar encendida y despierta
- Claude solo actúa cuando tú le pides
- Sin notificaciones al terminar (revisar manualmente)
- Un solo hilo de conversación simultáneo

## Managed Agents — Agentes 24/7 en la nube

Agentes que viven en servidores de Anthropic.
Costo: ~$0.70 USD/hora activa. Si espera, no cobra.
Consola: platform.claude.com (distinto a claude.ai)

### Setup:
1. platform.claude.com → misma cuenta de Claude
2. Settings → Billing → agregar tarjeta + límite mensual
3. Agent Quickstart → describir agente en español
4. Claude lo arma y hace preguntas
5. Conectar cuentas vía MCP

### Qué SÍ puede tocar (vive en la nube):
Gmail, Outlook, Google Drive, Notion, Dropbox
WhatsApp Business, Slack, Telegram
Google Calendar, Calendly
CRMs, ecommerce, dashboards online
Cualquier servicio con API

### Qué NO puede tocar:
Tu computadora local, archivos offline
Apps de escritorio (Photoshop, Excel local)
WhatsApp personal (solo WhatsApp Business API)
Redes privadas sin internet

### Agentes listos para vender a clientes:

ATENCIÓN A CLIENTES (WhatsApp 24/7):
"Quiero un agente que conteste WhatsApp de mis clientes.
Negocio: [descripción]. Debe: saludar, contestar precios/horarios,
agendar en Google Calendar, pasarme si no sabe,
mandarme resumen diario por Gmail.
Conectar: WhatsApp Business, Google Calendar, Gmail."

REPORTE SEMANAL AUTOMÁTICO:
"Agente que cada lunes 8am arme reporte semanal.
Debe: resumir Gmail, leer Google Sheets de ventas,
revisar Calendar, armar PDF y enviarlo por correo.
Conectar: Gmail, Google Drive, Google Calendar."

### Tips de modelo:
- Sonnet: 90% de los casos (rápido y barato)
- Opus: solo cuando necesitas razonamiento complejo

### Precio de referencia para clientes:
~$0.70/hora activa = muy rentable como producto vendible

## Shopify MCP — Tu tienda en piloto automático

31 herramientas oficiales de Shopify disponibles para Claude.
Productos, pedidos, clientes, descuentos e inventario.

### Instalación (desktop):
claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest

### Prompts listos para clientes ecommerce:

SUBIR PRODUCTOS EN LOTE:
"Tengo estos [N] productos nuevos. Súbelos con:
nombre - precio - descripción - tallas
Ponles la etiqueta [colección] a todos."

CAMBIAR PRECIOS:
"Busca todos los productos con etiqueta [X]
y súbeles el precio un 15%. Muéstrame tabla
con precio anterior y nuevo antes de aplicar."

REPORTE DE VENTAS:
"¿Cuáles son mis 5 productos más vendidos esta semana?
Dame nombre, unidades vendidas e ingreso total."

PEDIDOS PENDIENTES:
"Muéstrame pedidos pendientes de envío ordenados
por fecha. Marca los que tienen +3 días sin enviarse."

CREAR DESCUENTO:
"Crea código [NOMBRE] con X% de descuento en toda
la tienda. Una vez por cliente, expira en 30 días."

### Como producto vendible:
- Agente de tienda Shopify 24/7 para clientes ecommerce
- Reemplaza desarrollador/agencia para cambios rutinarios
- Combinar con /loop daily para reportes automáticos

## Firecrawl + Playwright — Ojos y manos en internet

### Firecrawl = Leer cualquier página web (ojos):
Instalación (desktop):
claude mcp add firecrawl-mcp-server -e FIRECRAWL_API_KEY=tu-key -- npx -y firecrawl-mcp-server
API key: firecrawl.dev (500 créditos gratis/mes)
Verificar: "Lee firecrawl.dev y dime de qué se trata"

### Playwright = Navegar como persona real (manos):
Instalación (desktop):
claude mcp add playwright -- npx -y @anthropic-ai/playwright-mcp@latest
Sin API key — 100% gratis
Verificar: "Abre google.com y toma captura de pantalla"

### Prompts para clientes:

INVESTIGAR COMPETENCIA:
"Lee [URL competidor] y dame:
1. De qué se trata el negocio
2. Qué servicios ofrecen
3. Cómo se posicionan
4. Qué puede mejorar su página"

EXTRAER DATOS:
"Abre [URL], busca [término] y dame lista
de primeros 5 resultados con título y enlace"

MONITOREAR PRECIOS:
"Revisa precios de [producto] en [tiendas]
y avísame cuando bajen de [precio]"

### Combinar con /loop:
/loop daily → monitoreo automático de competencia
/loop 4h → vigilar precios en tiempo real
/loop weekly → reporte de análisis de mercado

## Meta Ads MCP — Gestión de campañas con Claude

### Reglas de seguridad CRÍTICAS (nunca violar):
- SIEMPRE crear campañas/adsets/ads en status: PAUSED
- SIEMPRE mostrar resumen y pedir confirmación antes de ejecutar
- NUNCA subir presupuesto >$100 sin confirmación explícita
- NUNCA modificar spending limits sin aprobación humana
- Todos los presupuestos en CENTAVOS ($50 = 5000)
- Registrar TODAS las escrituras en logs/api_actions.log

### Setup (desktop):
1. Crear app en Meta Developers → generar token System User
2. Guardar en .env: META_ACCESS_TOKEN, META_AD_ACCOUNT_ID, META_PAGE_ID
3. Configurar .mcp.json con meta-ads MCP server
4. Verificar con /mcp

### Jerarquía Meta Ads:
Ad Account → Campaign → Ad Set → Ad → Ad Creative

### Objetivos de campaña:
- OUTCOME_AWARENESS: reconocimiento de marca
- OUTCOME_TRAFFIC: visitas web/app
- OUTCOME_ENGAGEMENT: interacciones
- OUTCOME_LEADS: formularios de leads
- OUTCOME_SALES: conversiones/compras

### Prompts esenciales para clientes:
"Valida mi configuración Meta Ads MCP y dime qué falta"
"Haz un dry-run de campaña OUTCOME_TRAFFIC en PAUSED con budget de prueba"
"Genera reporte últimos 7 días: spend, CTR, CPC, conversiones y 3 recomendaciones"

### Workflow para crear campaña:
1. Definir objetivo, audiencia, presupuesto y creativos
2. Verificar categorías especiales (crédito, empleo, vivienda, política)
3. Revisar specs de imagen/video
4. Ver resumen completo → aprobar
5. Ejecutar: Campaign → Ad Set → Creative → Ad (todo PAUSED)
6. Activar SOLO con aprobación humana explícita

### Como producto para clientes:
- Agente de Meta Ads para agencias de marketing
- Reportes automáticos semanales con /loop weekly
- Monitoreo de campañas con /loop 4h
- Combinar con Managed Agents para gestión 24/7

## Investigador Automático — Last 30 Days Skill

Investiga cualquier tema en 8 plataformas de los últimos 30 días.
Genera reporte completo con links. Tarda 2-8 minutos.
Gratis y open source.

### Instalación:
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days@last30days-skill

### Plataformas sin API key (funcionan de inmediato):
Reddit, Hacker News, Polymarket

### Plataformas con API key:
YouTube, X/Twitter, Bluesky, TikTok, Instagram Reels

### Comandos:
/last30days [tema]              → reporte completo 30 días
/last30days --compare "A vs B" → comparar dos temas
/last30days --quick [tema]      → búsqueda rápida
/last30days --days 7 [tema]     → últimos 7 días

### Para clientes — prompts listos:
"Investiga tendencias de [industria del cliente]
en los últimos 30 días"

"Compara [herramienta A] vs [herramienta B] —
¿qué dice la comunidad?"

"Investiga a [competidor] — qué está haciendo
en redes en los últimos 30 días"

### Combinar con /loop:
/loop weekly → reporte semanal automático de tendencias
/loop daily → monitoreo diario del nicho del cliente
Cada reporte se guarda automáticamente como Markdown

## WhatsApp AgentKit — Agente de WhatsApp para clientes

Construye agente de WhatsApp personalizado en 30 minutos.
Claude Code escribe todo el código — sin programar.
Open source: github.com/Hainrixz/whatsapp-agentkit

### Requisitos (instalar en desktop):
- Python 3.11+
- Claude Code
- Anthropic API Key (platform.anthropic.com)
- Cuenta WhatsApp API (Whapi, Meta Cloud API o Twilio)

### Instalación:
git clone https://github.com/Hainrixz/whatsapp-agentkit.git
cd whatsapp-agentkit
bash start.sh
claude → /build-agent

### Claude te hace 10 preguntas:
Nombre del negocio, giro, propósito del agente,
nombre del agente, tono, horario, archivos del negocio,
API key, proveedor WhatsApp, credenciales

### Probar antes de publicar:
python tests/test_local.py

### Deploy a producción:
Opción A (servidor propio): docker compose up --build
Opción B (sin servidor): Railway.app → conectar GitHub → deploy automático

### Personalizar después (sin código):
claude "Haz el agente más amigable"
claude "Agrega el nuevo servicio X"
claude "Migra de Whapi a Meta Cloud API"

### Como producto vendible:
- Un repositorio clonado por cliente
- ~$3 por millón de tokens (muy barato)
- Whapi: sandbox gratis para demos
- Railway: plan gratis para empezar
- Ideal para: restaurantes, clínicas, salones, inmobiliarias

## Scrapling — Fábrica de leads gratis

Extrae listas de clientes de Google Maps, directorios
y redes sociales. Sin pagar agencias de leads.
37,500+ estrellas GitHub. Licencia BSD-3 (uso comercial OK)
github.com/D4Vinci/Scrapling

### Instalación (desktop — prompt para Claude):
"Instala Scrapling con MCP integrado:
1. Verifica Python 3.10+ y uv instalados
2. uv pip install scrapling[all]
3. scrapling install (navegadores camuflados)
4. Lee README para comando MCP exacto
5. Agrega a claude_desktop_config.json
6. Prueba con búsqueda simple"
Después: reiniciar Claude Desktop completamente

### Prompt base para leads:
"Usa Scrapling para armarme lista de 50 [profesión]
en [ciudad]. Quiero: nombre, teléfono, dirección,
calificación Google Maps, reseñas, sitio web.
Limpia duplicados. Exporta a CSV en Desktop
como leads-[profesión]-[ciudad].csv"

### 3 productos vendibles:

1. LISTA DE NICHO LOCAL (~$500 USD):
Todos los [profesión] de una ciudad con datos completos
Ordenar por número de reseñas (más activos primero)

2. NEGOCIOS SIN WEB (~$200 USD por lista):
"Saca 100 restaurantes en [ciudad]. Filtra SOLO
los que NO tienen sitio web propio.
CSV con nombre, teléfono, calificación, reseñas"

3. MONITOREO DE COMPETENCIA (~$500 USD/mes):
"Extrae precios de estas URLs: [lista]
Compara con mis precios en [archivo]
¿Dónde pierdo ventas? ¿Dónde dejo dinero?"

### Agente semanal automático:
"Cada lunes busca [criterio] con Scrapling,
compara con leads-maestros.csv,
agrega solo nuevos y mándame resumen"
Combinar con /loop weekly o Managed Agent

### Reglas éticas:
- Respetar robots.txt y términos del sitio
- No acelerar el rate limiting de Scrapling
- Solo datos comerciales públicos (no datos personales)
- En prospección: identificarse y ofrecer opt-out

## Auto-CRM — Tu propio CRM gratis

CRM completo local. Sin Salesforce, sin HubSpot, sin mensualidad.
SQLite local — tus datos nunca salen de tu máquina.
Open source: github.com/Hainrixz/auto-crm

### Instalación (desktop):
git clone https://github.com/Hainrixz/auto-crm.git && cd auto-crm && npm install && npm run dev
Abrir: http://localhost:3000

### Primer paso después de instalar:
Abrir Claude Code dentro del proyecto → /setup

### 8 comandos de Claude Code incluidos:
/setup          → configurar CRM desde cero
/add-contact    → agregar contacto nuevo
/search         → buscar contactos o deals
/metrics        → métricas del pipeline
/follow-ups     → seguimientos pendientes
/import-csv     → importar desde Excel/CSV
/classify       → clasificar leads con IA
/digest         → resumen diario por email

### Variables opcionales (.env):
ANTHROPIC_API_KEY → clasificación de leads con IA
RESEND_API_KEY    → resumen diario por email
DIGEST_EMAIL      → correo donde llega el resumen

### 10 herramientas MCP incluidas:
list_contacts, search_contacts, get_contact,
list_deals, get_deal, get_pipeline_metrics,
list_activities, get_follow_ups, classify_leads,
get_dashboard_summary

### Como producto para clientes:
- Un CRM personalizado por cliente/negocio
- Personalizar con Claude Code en español sin código
- Deploy en servidor propio con Docker:
  docker compose up -d
- Conectar con webhooks de Typeform, Tally, Google Forms
- Combinar con agente WhatsApp para leads automáticos

## Agency Agents — 144 especialistas listos

144+ agentes especializados para Claude Code.
Tu agencia completa gratis en un comando.
Open source MIT: github.com/msitarzewski/agency-agents

### Instalación (desktop):
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents
cp -r agents/* ~/.claude/agents/
ls ~/.claude/agents/ (verificar)

### Activar un agente:
"Hey Claude, activate [Nombre del Agente] mode"

### 12 divisiones disponibles:
Marketing (29): Content Creator, TikTok Strategist,
  SEO Expert, Email Marketer, Reddit Builder
Ingeniería (25): Frontend Developer, Backend Architect,
  DevOps, Security Engineer
Ventas (8): Outbound Strategist, Discovery Specialist,
  Deal Closer, Account Expansion
Diseño (8): UI/UX Designer, Brand Guardian
Paid Media (7): PPC Strategist, Search Analyst
Testing (8): QA Specialist, Performance Benchmarker
Project Mgmt (6): Portfolio Oversight, Producer
Soporte (6): Customer Service, Analytics Expert
Producto (5): Sprint Prioritizer, Product Manager
Game Dev (15): Unity, Unreal, Cross-Engine
Especializados (30): Multi-Agent Orchestrator, etc.
Spatial Computing (6): XR, Vision Pro, WebXR

### Flujos para tu negocio de agentes:

LANZAR PRODUCTO:
Frontend Developer → Backend Architect →
Growth Hacker → Content Creator

CAMPAÑA DE MARKETING:
Content Creator → TikTok Strategist →
Email Marketer → SEO Strategist

CICLO COMPLETO DE CLIENTE:
Outbound Strategist → Discovery Specialist →
Deal Closer → Frontend Developer → Analytics Reporter

### Tip clave:
Combinar agentes en secuencia = resultado de agencia real
Cada agente mantiene la misma personalidad de marca

## Cowork — Proyectos con contexto persistente

Claude Desktop → sección Cowork → panel izquierdo
Claude ya te conoce en cada proyecto. No repites contexto.

### Crear proyecto:
Projects → + → desde cero o desde carpeta existente

### Instrucciones de proyecto (plantilla para clientes):
"Eres mi asistente para [nombre cliente/proyecto]
Formato: responde en español, bullet points, incluye métricas
Reglas: nunca inventes datos, prioriza acciones concretas
No hagas: no asumas presupuesto, no uses emojis en documentos"

### Contexto que puedes agregar:
- Carpetas locales del proyecto
- Archivos (PDFs, Excel, imágenes)
- URLs de páginas web relevantes

### Tareas programadas (la función más poderosa):
Frecuencia: cada hora, diario, semanal, cron personalizado
Modelo: Haiku para simple, Sonnet para razonamiento

TAREA — RESUMEN SEMANAL:
"Cada lunes 9am:
1. Revisa carpeta /Documentos/Reportes/
2. Identifica archivos nuevos últimos 7 días
3. Extrae puntos clave de cada uno
4. Genera resumen en /Documentos/resumen-semanal.md
5. Marca URGENTE lo crítico"

TAREA — MONITOREO DE COMPETENCIA:
"Cada miércoles 8am:
1. Visita [URLs competidores]
2. Extrae precios actuales
3. Compara con precios-actuales.csv
4. Genera reporte de diferencias
5. Marca ALERTA si bajaron más de 10%"

### Keep Awake:
Settings → General → Keep computer awake → activar
Necesario para que tareas programadas corran solas

### El nuevo paradigma:
Antes: abres Claude para decirle qué hacer
Ahora: abres Claude para ver qué hizo

## Los 3 modelos — Cuándo usar cada uno

Regla: empieza siempre por abajo, escala solo cuando necesites.

### HAIKU — Para pensar (prácticamente gratis):
- Lluvia de ideas y brainstorming
- Preguntas rápidas del día a día
- Resumir textos y documentos cortos
- Organizar ideas antes de construir
- Clasificar y categorizar información

### SONNET — Para construir (70% de tu uso):
- Escribir y debuggear código
- Crear contenido, emails, propuestas
- Analizar documentos y datos grandes
- Flujos multi-paso con herramientas
- Proyectos con contexto amplio (1M tokens)

### OPUS — Para lo importante (solo cuando vale):
- Investigación profunda y análisis complejo
- Arquitectura de software y decisiones críticas
- Cuando Sonnet no dio el ancho
- Razonamiento multi-paso avanzado
- Generación de proyectos grandes

### Workflow diario:
Mañana → Haiku (organizar, planear, preguntar)
A trabajar → Sonnet (construir, crear, analizar)
Problema complejo → Opus (solo con intención)

### Para agentes de clientes:
- Clasificación de leads → Haiku
- Construir el agente → Sonnet
- Arquitectura de sistema complejo → Opus
- Reportes automáticos /loop → Haiku
- Análisis profundo de datos → Sonnet/Opus

## Guía definitiva — Claude Code bien usado

### Regla fundamental:
Claude Code es un agente con acceso a tu computadora.
No es un chatbot. Le das instrucciones y las ejecuta.

### Setup en ~/.zshrc (desktop):
alias claude='claude --dangerously-skip-permissions'
alias cc='claude'
alias ccr='claude --resume'

### Zonas de contexto — monitorear siempre:
0-50% → trabajo efectivo, agente piensa bien
50-70% → cuidado, empieza a olvidar
70-85% → problemas en camino
85%+   → auto-compact, empezar sesión nueva

### Reglas de oro que salvan dinero:
1. CLAUDE.md < 500 líneas, sin contradicciones
2. 1 tarea = 1 sesión → /clear → sesión nueva
3. MCPs por proyecto, NO globales
4. Global solo: lo que usas en TODO (Exa, Chrome DevTools)

### MCPs vs Skills:
MCP viejo: ~5,700-11,400 tokens por MCP
Skills nuevo: ~50 tokens (header) + carga bajo demanda
→ Misma funcionalidad, 100x más eficiente
→ Marketplace: skills.sh

### Subagentes — 3x más rápido, 6x más barato:
Sin subagentes: 3 tareas = 15 min + 300K tokens
Con subagentes: 3 tareas = 5 min + 50K tokens
Configurar en: .claude/agents/[nombre].md
Modelo por subagente:
- Opus → planes y arquitectura
- Sonnet → escribir código
- Haiku → buscar documentación

### Git + Deploy — dejar de compartir localhost:
git init → commits → push a GitHub (repo privado)
Deploy: npx vercel (menos de 1 minuto)
NUNCA secretos en el código → GitHub Secrets
Git Worktree → dos Claudes en paralelo sin conflictos

### El proceso que lo cambia todo (Superpowers):
Brainstorm → Specification → Plan →
Subagent Implementation → Code Review → Merge/PR
Resultado real: 9 tareas completadas con 9% de contexto
vs sin proceso: 1 tarea y ya vas en 85%

### Kit mínimo esencial:
- Exa MCP: búsqueda superior a la built-in
- Context7 Skill: docs frescos de librerías
- Chrome DevTools MCP: automatización del browser
- Frontend Design Skill: diseño profesional
- Skill Creator: crea tus propios skills
- Superpowers: proceso completo de desarrollo

### La ruta de 0 a avanzado:
0. Entender que es agente, no chatbot
1. Instalar + bypass + Whisper (voz)
2. CLAUDE.md desde el día uno
3. MCP → Skills → Subagentes
4. Monitorear contexto siempre
5. Deploy desde el primer proyecto
6. Git como salvavidas
7. Proceso: plan → decompose → implement → review

## Claude Ads — Meta Ads con reglas de seguridad

17 sub-habilidades + 10 agentes + 23 archivos de referencia.
Open source MIT: github.com/AgriciDaniel/claude-ads

### Instalación (desktop):
macOS/Linux:
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-ads/main/install.sh | bash
Windows:
irm https://raw.githubusercontent.com/AgriciDaniel/claude-ads/main/install.ps1 | iex

### Conectar Meta:
1. developers.facebook.com → Crear App → Business
2. Permisos: ads_management, ads_read,
   business_management, read_insights
3. Graph API Explorer → generar Access Token
4. Abrir Claude Code → claude → compartir token + act_ID

### 6 reglas de seguridad incluidas:
- Campañas siempre en PAUSED al crear
- Límite $100/día sin confirmación explícita
- Contenido prohibido bloqueado automáticamente
- Special Ad Categories activadas (vivienda, empleo, crédito)
- Sin cambios sin aprobación humana
- Regla 3x Kill: CPA 3x mayor al objetivo → pausar

### Prompts para clientes:

AUDITORÍA COMPLETA:
"Ads Meta — Audita mi cuenta de Meta Ads.
Industria: [X], presupuesto: [Y]/mes,
objetivo: [ventas/leads/tráfico].
Dame Health Score, hallazgos y recomendaciones."

ANÁLISIS DE COMPETENCIA:
"Ads Meta — Investiga anuncios de mi competencia
en [nicho]. Qué formatos usan, qué copy manejan,
cómo puedo destacar. Compara con mis campañas."

### Otras plataformas incluidas:
Google Ads, TikTok, LinkedIn, YouTube, Microsoft Ads

### Como producto vendible:
- Auditoría de Meta Ads para agencias y negocios
- Gestión de campañas 24/7 con Managed Agent
- Combinar con /loop weekly para reportes automáticos
- Health Score como entregable para clientes

## Viral Script Combo — Fábrica de videos virales

3 herramientas gratis. Sin grabar. Sin escribir. Solo publicar.

### 1. Awesome Claude Skills (habilidades virales):
Instalar con este prompt en Claude Code:
"Entra a https://github.com/ComposioHQ/awesome-claude-skills
Busca habilidades de contenido viral y guiones.
Instala la que sirva para hooks y videos virales.
Úsala para todo lo que te pida de ahora en adelante."

### 2. UltraThink (pensar más profundo):
Agregar "ultrathink" antes de cualquier petición.
Sin instalar nada — solo una palabra.
Hace que Claude compare ángulos antes de responder.

### 3. VoxCPM (clonar tu voz):
git clone https://github.com/OpenBMB/VoxCPM.git && cd VoxCPM
Graba 10-30 segundos de tu voz → VoxCPM la clona
30 idiomas, calidad de estudio, gratis
Prompt: "Instala VoxCPM, clona mi voz de [audio],
lee este guion con mi voz: [guion]"

### Prompt completo del combo:
"ultrathink

Escríbeme guion viral de 60 segundos para [plataforma].
Tema: [tema]
- Hook que detenga scroll en 3 segundos
- Estructura: hook → problema → solución → prueba → CTA
- Lenguaje natural, como hablarle a un amigo
- Sin frases robóticas ni clichés de IA
- Máximo 150 palabras
Al final marca dónde va cada corte de edición."

### Como producto para clientes:
- Creación de contenido viral para redes sociales
- Scripts en múltiples idiomas con la voz del cliente
- Combinar con Last30Days para temas trending
- /loop weekly para calendario de contenido automático

## Open Carrusel — Agente de carruseles de Instagram

Reemplaza Canva. Gratis, local, sin suscripciones.
Sin marca de agua. Sin subir nada a la nube.
Open source MIT: github.com/Hainrixz/open-carrusel

### Instalación (desktop — un solo prompt):
"Instala y arranca open-carrusel desde cero.
Repo: https://github.com/Hainrixz/open-carrusel
1. Clona en Desktop
2. npm install
3. npm run setup
4. npm run dev
5. Abre http://localhost:3000
Si hay errores, resuélvelos tú sin preguntar."

### Flujo de uso:
1. Subir referencias de carruseles que te gustan
2. Configurar marca en /data/brand.json
   (colores, fuentes, logo — una sola vez)
3. "Haz carrusel de 6 slides sobre [tema], tono [X]"
4. Editar arrastrando slides + historial por slide
5. Exportar: 1:1, 4:5 o 9:16 (tamaño exacto Instagram)

### Comandos dentro del proyecto:
/start  → arranca el servidor
/stop   → detiene el servidor
/reset  → limpia datos locales
/doctor → diagnóstico de entorno

### Como producto para clientes:
- Carruseles educativos para coaches y creadores
- Promos de producto consistentes con su marca
- Storytelling de marca (antes/después)
- Plantillas reutilizables por cliente
- Combinar con Viral Script Combo para contenido completo
- /loop weekly para calendario de carruseles automático

## Claude SEO — 13 comandos de especialista SEO

Skill que convierte Claude en especialista SEO completo.
Auditorías técnicas, contenido y agente que arregla todo.

### Instalación:
npx skills.sh install claude-seo

### Auditoría técnica (5 comandos):
/seo-audit    → auditoría completa (meta, headings, links, sitemap)
/seo-speed    → rendimiento y Core Web Vitals
/seo-structure → arquitectura, internal linking, URLs
/seo-crawl    → cómo Google ve tu sitio
/seo-schema   → structured data y rich snippets

### Contenido y keywords (5 comandos):
/seo-keywords → densidad, ubicación, variaciones semánticas
/seo-meta     → genera meta titles y descriptions optimizados
/seo-headings → audita estructura H1-H6
/seo-content  → calidad, longitud, thin content, duplicados
/seo-images   → alt text, tamaño, WebP, lazy loading

### Reportes y automatización (3 comandos):
/seo-report   → reporte completo en markdown con plan de acción
/seo-compare  → compara tu página vs competidor
/seo-fix      → agente que corrige todo automáticamente

### Flujo recomendado para clientes:
1. /seo-audit → ver estado general
2. /seo-fix → Claude corrige automáticamente
3. /seo-report → reporte entregable al cliente
4. /seo-compare → comparar vs competencia
5. /loop weekly → monitoreo SEO automático

### Como producto vendible:
- Auditoría SEO inicial como servicio
- Reporte /seo-report como entregable profesional
- Mantenimiento SEO mensual con /loop
- Combinar con Scrapling para análisis de competencia

## TradingView MCP — Claude ve tus gráficas en tiempo real

Claude lee datos reales del chart (no capturas de pantalla).
Analiza, dibuja niveles, pone alertas y hace backtests.
Open source: github.com/tradesdontlie/tradingview-mcp

### Requisitos:
- Claude Code instalado
- TradingView Desktop (no versión web)
- Node.js 18+
- Git

### Instalación (desktop — prompt para Claude):
"Instala TradingView MCP de @Tradesdontlie.
Repo: https://github.com/tradesdontlie/tradingview-mcp
1. Verifica Node.js 18+ y Git
2. Clona repo en ~/tradingview-mcp
3. npm install
4. Lee README para comando exacto del servidor
5. Configura en ~/.claude/.mcp.json
6. Dame comando para lanzar TradingView con debug port"

### Paso crítico — siempre antes de usar:
1. Cerrar TradingView completamente
2. Relanzar con --remote-debugging-port=9222
3. Abrir Claude Code en sesión nueva
4. Verificar: "Corre tv_health_check" → cdp_connected: true

### 6 casos de uso para clientes de trading:

ANÁLISIS EN VIVO:
"Analiza [símbolo] en [timeframe]. Dame tendencia,
soportes/resistencias, estructura y conclusión en 3 renglones"

DIBUJAR NIVELES:
"Dibuja 3 soportes (verde) y 3 resistencias (rojo)
en el chart actual con etiquetas de precio"

ALERTAS EN WATCHLIST:
"Ponme alertas en toda mi watchlist cuando toquen
soporte o resistencia clave. Muéstrame lista antes"

REPORTE DE MERCADO:
"¿Qué pasó en mi watchlist en las últimas 12 horas?
Dame cambio %, rango, volumen y símbolos en decisión"

BACKTEST:
"Backtesta: entrar cuando precio cruza EMA50 con RSI<40,
salir cuando cruza EMA21 o RSI>70. Periodo: [fechas]"

PINE SCRIPT:
"Escribe indicador Pine Script v5 que [descripción].
Compílalo, corrige errores y agrégalo al chart"

### Como producto vendible:
- Análisis técnico automatizado para traders
- Reportes diarios de mercado con /loop daily
- Agente de alertas 24/7 con Managed Agent
- Backtesting de estrategias como servicio

## 5 Herramientas esenciales 2026

### 1. Superpowers (103K estrellas):
Piloto automático con subagentes. TDD obligatorio.
Revisión de código en dos etapas.
Instalación: npx superpowers@latest init
github.com/obra/superpowers

### 2. Everything Claude Code (50K estrellas):
28 agentes especializados + 116 skills + 59 comandos.
Ganador Anthropic Hackathon Feb 2026.
Comandos: /plan, /tdd, /code-review, /verify
AgentShield: escáner de vulnerabilidades 102 reglas
Instalación: git clone https://github.com/affaan-m/everything-claude-code.git
github.com/affaan-m/everything-claude-code

### 3. UI UX Pro Max:
67 estilos de UI + 161 reglas por industria.
161 paletas de color + 57 combinaciones tipografía.
13 tech stacks: React, Next.js, Vue, Svelte, Flutter, etc.
Instalación: npx uipro-cli@latest init
github.com/nextlevelbuilder/ui-ux-pro-max-skill

### 4. claude-mem (39K estrellas):
Memoria permanente con búsqueda semántica.
SQLite + Chroma. Visor web en localhost:37777.
Control de privacidad con etiquetas <private>
Instalación: npx claude-mem@latest init
github.com/thedotmack/claude-mem

### 5. n8n-MCP (15K estrellas):
Claude arma automatizaciones n8n completas.
1,084 nodos + 2,709 templates disponibles.
Instalación: npx n8n-mcp@latest
github.com/czlonkowski/n8n-mcp

### Para agentes de clientes:
- Superpowers → construir agentes complejos
- Everything Claude Code → departamento de ingeniería
- UI UX Pro Max → diseño profesional por industria
- claude-mem → memoria entre sesiones de trabajo
- n8n-MCP → automatizaciones sin código para clientes

## Awesome LLM Apps — 100+ agentes listos para instalar

106K+ estrellas. Apache 2.0 (libre para uso comercial).
13 categorías de agentes listos para clonar e instalar.
github.com/Shubhamsaboo/awesome-llm-apps

### 4 agentes estrella para clientes:

1. AI CONSULTANT AGENT:
Analiza el negocio completo del cliente y da
recomendaciones estratégicas en minutos.
Carpeta: ai_agent_tutorials/ai_consultant_agent

2. AI SALES INTELLIGENCE AGENT TEAM:
Equipo de agentes de ventas. Investiga mercado,
sugiere precios y arma estrategia de prospección.
Carpeta: ai_agent_tutorials/ai_sales_intelligence_agent_team

3. AI COMPETITOR INTELLIGENCE AGENT TEAM:
Investiga competencia — qué hacen, cómo y dónde fallan.
Carpeta: ai_agent_tutorials/ai_competitor_intelligence_agent_team

4. CUSTOMER SUPPORT VOICE AGENT:
Contesta llamadas de soporte 24/7 automáticamente.
Carpeta: voice_ai_agents/customer_support_voice_agent

### Prompt para encontrar agentes por negocio:
"Clona https://github.com/Shubhamsaboo/awesome-llm-apps
Mi negocio es: [descripción]
Mis problemas principales: [lista]
Recomiéndame 3-5 agentes. Para cada uno: qué hace,
por qué me sirve y cómo instalarlo paso a paso."

### Prompt para instalar agente específico:
"En awesome-llm-apps busca el agente [nombre].
1. Clona el repo
2. Entra a su carpeta
3. Instala dependencias
4. Configura API keys
5. Ejecuta y verifica"

### 13 categorías disponibles:
Agentes iniciales, Agentes avanzados, Multi-agente,
Voz, MCP, RAG, Memoria, Chat, Optimización,
Fine-tuning, Skills, Juegos, Crash Courses

## Claude Obsidian — Segunda cabeza con memoria permanente

Todo lo que aprendes con Claude queda guardado para siempre
en Obsidian. Claude llena, conecta y organiza las notas solo.
github.com/AgriciDaniel/claude-obsidian

### Requisitos:
- Obsidian (obsidian.md) — gratis
- Claude Code abierto dentro de la carpeta de Obsidian

### Instalación (prompt todo-en-uno):
"Instala claude-obsidian desde
https://github.com/AgriciDaniel/claude-obsidian
1. claude plugin marketplace add AgriciDaniel/claude-obsidian
2. claude plugin install claude-obsidian@claude-obsidian-marketplace
3. Corre /wiki para crear estructura inicial
4. Resume comandos disponibles en español"

### Estructura que crea /wiki:
concepts/  → ideas grandes y aprendizajes
sources/   → libros, posts, videos de referencia
entities/  → personas, empresas, productos
sessions/  → conversaciones archivadas

### 3 comandos del día a día:
/save              → guarda conversación actual como notas conectadas
/autoresearch [tema] → investiga en internet y agrega al vault
/canvas [desc]     → crea diagrama visual con tus notas

### El loop que lo hace mágico:
1. Arrastrar material crudo a carpeta .raw/
2. ingest [nombre del archivo]
3. Claude crea 8-15 páginas conectadas automáticamente
4. Si hay contradicciones con notas viejas → marca [!contradiction]

### Consultar tu segunda cabeza:
"qué sabes sobre [tema]"
→ Claude responde citando TUS notas, no su entrenamiento

### Para tu negocio de agentes:
- Un vault por cliente con toda su información
- ingest de juntas, emails y documentos del cliente
- Claude recuerda todo del cliente en cada sesión
- /autoresearch para investigar la industria del cliente
- Regla de oro: nunca tocar carpetas a mano

## Skill Seekers + Obsidian — Pipeline de conocimiento

Convierte cualquier fuente en contexto para Claude.
Pipeline: Recopilar → Organizar → Trabajar con Claude.

### Las 3 herramientas:
1. Skill Seekers → extrae info de cualquier fuente
2. Obsidian → organiza y conecta notas localmente
3. obsidian-skills → Claude escribe en formato Obsidian nativo

### Skill Seekers — fuentes que procesa:
Webs, GitHub, PDFs, YouTube, Notion, Confluence,
Slack, Discord, RSS, Jupyter, Word, PowerPoint

Instalación: pip install skill-seekers

3 comandos esenciales:
skill-seekers create [URL o archivo]
skill-seekers enhance skill-seekers-output/
skill-seekers package skill-seekers-output/ --target claude

### obsidian-skills — instalación:
claude install-skill https://github.com/kepano/obsidian-skills
Habilidades: obsidian-markdown, obsidian-bases,
json-canvas, obsidian-cli, defuddle

### Prompts del pipeline completo:

ANALIZAR REPOSITORIO:
"Usa Skill Seekers para extraer [URL repo]:
skill-seekers create [URL]
skill-seekers enhance skill-seekers-output/
skill-seekers package skill-seekers-output/ --target claude
Crea notas en Obsidian: qué hace, estructura,
conceptos clave, cómo empezar. Usa wikilinks."

VIDEO DE YOUTUBE A NOTAS:
"Extrae contenido de [URL video] con Skill Seekers.
Crea nota en Obsidian con: resumen 5 bullets,
conceptos clave, pasos accionables, links relacionados."

INVESTIGAR TEMA DESDE MÚLTIPLES FUENTES:
"Extrae de [URL1], [URL2], [URL3] con Skill Seekers.
Crea: nota principal, notas por concepto,
nota de preguntas pendientes. Conectar con wikilinks."

### Tips clave:
- Siempre usar enhance antes de package
- --target claude hace la diferencia en calidad
- Un vault por cliente/proyecto
- Abrir Claude Code desde dentro del vault

## G Stack — 31 habilidades de Garry Tan (Y Combinator)

Creado por el CEO de Y Combinator. Licencia MIT. Gratis.
Convierte Claude en equipo completo de desarrollo.
github.com/garrytan/gstack

### Instalación (desktop):
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup

### 3 comandos mágicos para empezar:
/autoplan → arquitecto que planea todo el proyecto
/qa       → prueba todo en navegador real, arregla errores
/ship     → publica a producción automáticamente

### Las 31 habilidades por categoría:

PLANEAR:
/autoplan, /office-hours, /plan-ceo-review,
/plan-eng-review, /plan-design-review

DISEÑAR:
/design-consultation, /design-shotgun,
/design-html, /design-review

REVISAR:
/review, /investigate, /cso (seguridad),
/codex (segunda opinión con otra IA)

PROBAR:
/qa, /qa-only, /benchmark, /browse, /connect-chrome

PUBLICAR:
/ship, /land-and-deploy, /canary,
/document-release, /retro

HERRAMIENTAS:
/careful, /freeze, /unfreeze, /guard,
/setup-browser-cookies, /setup-deploy,
/gstack-upgrade, /learn

### Flujo completo de proyecto:
1. /office-hours → definir y mejorar idea
2. /autoplan → plan completo automático
3. /design-html → código y diseño
4. /review → revisar y arreglar errores
5. /qa → probar en navegador real
6. /ship → publicar a internet
7. /retro → resumen y mejoras

### Para agentes de clientes:
- /guard para proteger código del cliente
- /canary para vigilar que todo funcione post-deploy
- /retro semanal como entregable al cliente
- /cso para auditoría de seguridad

## Claude Web Builder — Landing pages profesionales sin código

Genera landing pages completas respondiendo preguntas.
Deploy a Vercel incluido. Sin saber programar.
Open source: github.com/Hainrixz/claude-webkit

### Instalación (desktop):
git clone https://github.com/Hainrixz/claude-webkit.git
cd claude-webkit
claude

### Tech stack incluido automáticamente:
Next.js 15, Tailwind CSS 4, shadcn/ui,
TypeScript, Framer Motion (animaciones)

### 6 fases automáticas:
1. Preguntas sobre el negocio (4 rondas en español)
2. Aprobación del plan visual (colores, tipografía, estilo)
3. Construcción automática de todos los componentes
4. Vista previa local en el navegador
5. Refinamiento iterativo con cambios al instante
6. Deploy a Vercel con URL real

### 13 habilidades pre-instaladas:
Design Methodology, Component Architecture,
Performance Optimization, Deployment Automation,
Humanizer, SEO Fundamentals, Accessibility,
Responsive Design, Animation System,
Content Strategy, Color Theory,
Typography System, Code Quality

### Comandos:
claude          → inicia el builder
npm run dev     → ver página en navegador
npm run build   → versión de producción

### Como producto vendible:
- Landing pages para clientes sin costo de diseñador
- Portfolio de páginas reutilizables por industria
- Combinar con Claude SEO para optimización completa
- Combinar con Claude Ads para campañas completas
- Precio sugerido: $500-2,000 USD por landing page
- Un repositorio clonado por cliente

## Claude Code Game Studios — Estudio de videojuegos completo

49 agentes especializados + 72 comandos.
Sin saber programar. MIT license.
9,556 estrellas: github.com/Donchitos/Claude-Code-Game-Studios

### Motores disponibles:
- Godot → más fácil, gratis, ideal para empezar
- Unity → más usado en la industria, vender juegos
- Unreal → gráficos AAA, juegos 3D ambiciosos

### Instalación (desktop — prompt todo-en-uno):
"Instala https://github.com/Donchitos/Claude-Code-Game-Studios
1. Clona con git clone
2. Lee README para estructura
3. Copia /agents, /commands y config según el repo
4. Resume agentes y comandos disponibles en español
Pregúntame qué motor quiero antes de instalar."

### 8 comandos más importantes:
/brainstorm    → ideas de juegos y escoger una
/design-system → mecánicas, reglas y loop central
/dev-story     → programar una feature completa
/qa-plan       → revisar bugs y plan de pruebas
/art-direction → dirección visual, estilo y paleta
/sound-design  → música y efectos del juego
/playtest      → simula sesiones con jugadores
/release-plan  → publicar en Steam, itch.io o móvil

### Flujo de primer juego:
1. /brainstorm → definir idea en una línea
2. /design-system → cómo se juega
3. /dev-story → primera feature
4. /qa-plan → probar que funciona
5. /release-plan → publicar

### Como producto vendible:
- Desarrollo de videojuegos indie para clientes
- Prototipos de juegos para startups y empresas
- Juegos educativos por industria
- Experiencias gamificadas para onboarding de clientes

## Editor Pro Max — Estudio de video con IA

De descripción en español a MP4 profesional.
Sin After Effects, sin suscripciones. 100% local.
Open source: github.com/Hainrixz/editor-pro-max

### Tech stack:
Remotion 4.0, FFmpeg, Whisper.cpp (transcripción local),
React 19, TypeScript, Sharp

### Instalación (desktop):
git clone https://github.com/Hainrixz/editor-pro-max.git
cd editor-pro-max && npm install
claude
npm run dev → preview en localhost:3000

### 9 templates incluidos:
TikTok (9:16), Instagram Reel, YouTube Short,
Presentación (16:9), Testimonial, Talking Head,
Podcast Clip, Anuncio, Before/After

### Capacidades:

CREAR DESDE CERO:
- TikToks y Reels con animaciones
- Presentaciones con transiciones
- Videos explicativos y anuncios

EDITAR VIDEO EXISTENTE:
- Subtítulos automáticos (5 presets: classic, bold, outline, glow, box)
- Remoción de silencios automática
- Jump cuts automáticos
- Remoción de fondo con IA

### Prompts para clientes:

TIKTOK DESDE CERO:
"Crea TikTok de 30 segundos para [producto].
Estilo moderno. Texto animado + 3 beneficios + CTA.
Colores: [marca]. Formato 9:16."

SUBTÍTULOS AUTOMÁTICOS:
"Agrega subtítulos a [ruta/video.mp4].
Preset 'bold'. Transcribe con Whisper y sincroniza."

LIMPIAR VIDEO:
"Elimina silencios >0.5s de [ruta/video.mp4].
Aplica jump cuts automáticos. Exporta MP4 16:9."

### Plataformas soportadas:
TikTok, YouTube, YouTube Shorts, Instagram Reels,
Instagram Feed, LinkedIn, Twitter/X, Facebook

### Como producto vendible:
- Videos de marketing para clientes
- Subtítulos automáticos para contenido existente
- Edición de podcasts y vlogs
- Combinar con Viral Script Combo para pipeline completo
- Batch render: múltiples formatos de un solo video

## The Architect — Plano completo de 16 secciones

Describe tu idea → plano completo → Claude Code construye solo.
Open source: github.com/Hainrixz/the-architect

### Instalación (desktop):
git clone https://github.com/Hainrixz/the-architect.git && cd the-architect && claude

### Cómo funciona:
1. Describes tu idea (SaaS, app, agente, lo que sea)
2. The Architect te hace preguntas específicas
3. Genera plano completo de 16 secciones
4. Metes el plano en carpeta nueva como CLAUDE.md
5. Abres Claude Code → construye sin preguntarte nada

### Atajo — Just Build It:
Escribe "Just Build It" o "Solo constrúyelo"
The Architect elige las mejores opciones por ti automáticamente

### Las 16 secciones del plano:
01. Visión del proyecto
02. Stack tecnológico
03. Estructura de directorios
04. Esquemas de base de datos
05. Especificaciones de API
06. Arquitectura frontend
07. Diseño visual (colores, tipografía)
08. Flujos de autenticación
09. Orden de construcción ★ (paso a paso para Claude)
10. Configuración de entorno
11. Dependencias y librerías
12. Deploy (cómo y dónde publicar)
13. Testing (qué y cómo probar)
14. Skills recomendados de Claude Code
15. Instrucciones del builder (CLAUDE.md)
16. Restricciones y reglas

### Para agentes de clientes:
- Usar The Architect ANTES de construir cualquier agente
- El plano se convierte en el CLAUDE.md del proyecto del cliente
- Sección 09 (orden de construcción) = instrucciones para Claude
- Sección 16 (restricciones) = reglas de seguridad del cliente
- Tip: ser específico → "agente de WhatsApp para clínica dental
  con integración a Google Calendar y respuesta en menos de 30s"

## Stack App Móvil IA — De idea a App Store

Stack recomendado: Rork + Claude Opus 4.6 +
Supabase + Stripe + Vercel/App Store/Play Store

### Herramientas y para qué:
- Rork: construir app móvil con IA sin infraestructura manual
- Claude Opus 4.6: generar y revisar lógica, UI y backend
- Supabase: auth, base de datos y APIs (free tier generoso)
- Stripe: cobros y suscripciones desde el MVP
- Vercel: lanzar versión web primero para validar
- App Store ($99/año) / Play Store ($25 pago único)

### Costos por escenario:
Mínimo (web-first): $0-20 USD/mes
Creator (stack pagado base): $45-120 USD/mes
Pro (móvil completo): $200+ USD/primer año

### Flujo operativo:
1. Definir idea, usuario y alcance v1
2. Construir MVP en Rork con prompts claros
3. Conectar Supabase (auth + datos)
4. Integrar Stripe cuando tengas propuesta de valor
5. QA: login, flujo principal, errores, rendimiento
6. Publicar en Vercel primero → validar → luego stores
7. Medir, feedback, iteraciones semanales

### Checklist de lanzamiento:
- MVP sin errores críticos en flujo principal
- Métricas mínimas definidas (activación, retención)
- Auth y base de datos en producción
- Pagos probados (éxito y falla)
- Capturas y metadata para stores listas
- Plan de soporte post-lanzamiento

### Como producto vendible:
- Apps móviles con IA para clientes por industria
- Estrategia: web primero → validar → stores
- Cobrar por app + mantenimiento mensual
- Combinar con WhatsApp AgentKit para engagement
- Combinar con Auto-CRM para gestión de usuarios

## Cyber Neo — Auditoría de seguridad automática

5 subagentes en paralelo. 11 dominios de seguridad.
100% solo lectura — nunca modifica archivos.
Reporte en Markdown en tu Desktop.
Open source MIT: github.com/Hainrixz/cyber-neo

### Instalación (desktop):
git clone https://github.com/Hainrixz/cyber-neo.git ~/.claude/skills/cyber-neo

O decirle a Claude:
"Instala https://github.com/Hainrixz/cyber-neo
Clónalo en ~/.claude/skills/cyber-neo"

### Uso:
Abrir Claude Code en la carpeta del proyecto → /cyber-neo
Los 5 agentes trabajan en paralelo → reporte en Desktop

### 11 dominios que escanea:
1. Código (SAST) → errores de seguridad en código
2. Autenticación → accesos y contraseñas
3. Criptografía → cifrado de datos sensibles
4. Secretos → 60+ patrones (API keys, tokens, passwords)
5. Dependencias → librerías con vulnerabilidades conocidas
6. Seguridad Web → cabeceras HTTP, CSRF, browser
7. Supply Chain → paquetes de terceros
8. CI/CD → GitHub Actions y pipelines
9. Contenedores → Docker y Kubernetes
10. Manejo de Errores → info sensible en errores
11. Logging → datos privados en registros

### Herramientas opcionales (mejoran resultados):
Semgrep → SAST avanzado
Trivy → vulnerabilidades en Docker
Gitleaks → secretos en historial Git
pip-audit → dependencias Python
cargo-audit → dependencias Rust

### Como producto vendible:
- Auditoría de seguridad inicial para clientes
- Reporte Markdown como entregable profesional
- Correr antes de cada deploy con /loop
- Combinar con G Stack /cso para seguridad completa
- Precio sugerido: $300-1,000 USD por auditoría

## Maia Skill — Análisis de mercados multi-agente

5 agentes especializados en paralelo. Dashboard interactivo.
Datos en tiempo real. 100% local.
⚠️ Solo informativo — no es asesoría financiera.
Open source: github.com/Hainrixz/maia-skill

### Instalación (desktop):
curl -fsSL https://raw.githubusercontent.com/Hainrixz/maia-skill/main/install.sh | bash

### Los 5 agentes:
- Crypto: Bitcoin, Ethereum y más
- Acciones: S&P 500, NASDAQ y más
- Divisas: USD/MXN, DXY y más
- Materiales: Oro, petróleo y más
- Estrategia: combina todo y recomienda

### Cómo usarlo:
"Hazme un análisis de inversión"
"Analiza los mercados"
"¿Cuáles son las mejores oportunidades hoy?"
→ Elige perfil: conservador, moderado o agresivo
→ Dashboard abre en localhost:3420

### Dashboard incluye:
- Distribución de portafolio por sector
- Rankings por riesgo con puntuación de confianza
- Análisis por activo (precio, cambio 24h/7d/30d)
- Bilingüe español/inglés

### Análisis automáticos con /loop:
/loop 24h /investment-analysis  → diario
/loop 168h /investment-analysis → semanal

### Como producto para clientes:
- Reportes de mercado para traders e inversores
- Análisis semanal automatizado como servicio
- Combinar con TradingView MCP para análisis técnico
- Dashboard como entregable visual para clientes
- Precio sugerido: $200-500 USD/mes por reporte semanal

## Top nuevos — Abril 2026

### Claude Code Ultimate Guide (3.3K estrellas):
La guía más completa de Claude Code.
228 templates + 271 preguntas quiz + 41 diagramas.
Base de datos de seguridad: 24 CVEs + 655 skills maliciosos.
Guías por rol: Tech Lead, CTO, PM, Developer.
Instalación: git clone https://github.com/FlorianBruniaux/claude-code-ultimate-guide.git

### Antigravity Awesome Skills (32.8K estrellas):
1,400+ skills en un solo comando.
Compatible con Claude Code, Cursor, Codex, Gemini.
Bundles temáticos por área.
Instalación: npx antigravity-awesome-skills
github.com/sickn33/antigravity-awesome-skills

### LightRAG (33.1K estrellas):
RAG con grafos de conocimiento.
Paper publicado EMNLP 2025 - Universidad de Hong Kong.
Ideal para darle contexto preciso de documentos al agente.
Backends: Neo4J, PostgreSQL, MongoDB, OpenSearch.
WebUI para insertar, consultar y visualizar conocimiento.
Citaciones automáticas con trazabilidad de fuentes.
Instalación: pip install lightrag-hku
github.com/hkuds/lightrag

### Para agentes de clientes:
- Ultimate Guide → referencia técnica para construir agentes
- Antigravity Skills → 1,400 skills disponibles instantáneamente
- LightRAG → dar a agentes acceso preciso a documentos del cliente
  (manuales, contratos, bases de conocimiento internas)

## Vibe Voice — Transcripción gratis con Microsoft

Transcribe audio/video en 50+ idiomas con identificación de hablantes.
38K+ estrellas. Gratis, open source, corre local.
github.com/microsoft/VibeVoice

### Instalación (desktop — prompt para Claude):
"Ve a https://github.com/microsoft/VibeVoice
Lee el README e instálame Vibe Voice.
Quiero transcribir audio/video localmente.
Explícame qué vas haciendo en cada paso."

### Capacidades:
- 50+ idiomas
- Hasta 60 minutos de audio por pasada
- Identifica quién dijo qué (diarización)
- Timestamps automáticos
- 100% local — sin suscripciones

### Prompt de procesamiento post-transcripción:
"Acabo de transcribir con Vibe Voice:
[TRANSCRIPCIÓN]
1. Identifica quién dijo qué por hablante
2. Resumen ejecutivo de puntos clave
3. Acciones pendientes y decisiones tomadas
4. Marca lo que requiere seguimiento
Formato: limpio, secciones, listo para compartir."

### Combo viral — video competencia → guion propio:
1. Encontrar video viral del nicho
2. Transcribir con Vibe Voice
3. Prompt a Claude: analiza hook, estructura,
   ritmo, triggers emocionales, CTA, por qué pegó
4. Claude arma guion original con misma fórmula

### Como producto para clientes:
- Transcripción de juntas con resumen automático
- Análisis de llamadas de ventas → insights y objeciones
- Contenido en otro idioma → texto listo para traducir
- Pipeline: Vibe Voice → Claude → Editor Pro Max → video
- Combinar con /loop para transcripción automática de juntas diarias

## Microsoft MarkItDown — Ahorra tokens con documentos

Convierte PDFs, Word, Excel y más a Markdown limpio.
Claude lo lee rapidísimo y gasta mucho menos tokens.
100K+ estrellas. Gratis. github.com/microsoft/markitdown

### Instalación (decirle a Claude):
"Instala MarkItDown de Microsoft desde
https://github.com/microsoft/markitdown
Úsala cada vez que te pida convertir un archivo
a Markdown antes de leerlo."

### Archivos que convierte:
PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx),
Imágenes con texto, Audios (transcribe solo),
Videos de YouTube (por link), HTML, CSV, JSON, XML, ZIP

### Prompts de uso:

CONVERTIR PDF:
"Usa MarkItDown para convertir [ruta/archivo.pdf]
a Markdown. Léelo y resúmelo en español con
los puntos más importantes."

CONVERTIR EXCEL:
"Convierte [ruta/reporte.xlsx] con MarkItDown
y dime las 5 cosas más importantes de la tabla."

VIDEO DE YOUTUBE:
"Usa MarkItDown con [URL YouTube] para sacar
la transcripción. Hazme resumen en bullets."

### Por qué importa para tu negocio:
- Documentos del cliente → MarkItDown → Claude
- Contratos, manuales, reportes sin quemar tokens
- Combinar con LightRAG para base de conocimiento del cliente
- Combinar con Gbrain para memoria permanente de documentos
- Regla: SIEMPRE convertir antes de dar documentos grandes a Claude

## NanoBanana — Restauración de fotos a 4K

Convierte fotos borrosas o dañadas en HD ultra-realista.
Usa Google Gemini por debajo. Output en 4K.
github.com/zhongweili/nanobanana-mcp-server

### Requisitos:
- Claude Code instalado
- API key gratuita de Gemini (aistudio.google.com)

### Instalación (desktop — prompt para Claude):
"Instala el MCP server nanobanana-mcp-server.
Repo: github.com/zhongweili/nanobanana-mcp-server
Comando: uvx nanobanana-mcp-server@latest
Configúralo con mi API key de Gemini: [TU_KEY]"

### Prompt de restauración profesional:
"Aplica restauración fotográfica ultra-realista con
textura de piel natural, detalles precisos y aspecto
fotográfico profesional. Salida 4K con enfoque nítido
natural, iluminación cinematográfica, gradación de
color profesional y HDR.
No generada por IA, no ilustrada, no plástica.
Sin reinterpretación creativa ni alteraciones de
identidad. Sin caricatura, pintura ni ilustración."

### Modelos disponibles:
- NB2 (default): Gemini Flash — velocidad + calidad 4K
- Pro: para composiciones complejas

### Aspect ratios: 1:1, 4:3, 16:9, 9:16, 21:9

### Output: ./nanobanana-output/ (configurable)

### Como producto vendible:
- Restauración de fotos antiguas o dañadas
- Mejora de fotos para perfiles y marketing
- Servicio de upscaling para agencias de diseño
- Combinar con Editor Pro Max para contenido visual completo
- Precio sugerido: $5-20 USD por foto restaurada

## Blender MCP — Modelado 3D con lenguaje natural

Controla Blender con Claude desde Claude Desktop.
Sin saber programar. Open source MIT.
github.com/ahujasid/blender-mcp

### Requisitos:
- Blender 3.0+ (blender.org/download)
- Python 3.10+
- uv: curl -LsSf https://astral.sh/uv/install.sh | sh
- Claude Desktop

### Instalación (desktop):
1. Descargar addon.py del repo de GitHub
2. Blender → Edit → Preferences → Add-ons → Install
3. Activar "Interface: Blender MCP"
4. Presionar N en viewport → pestaña BlenderMCP → Start MCP Server
5. Agregar a claude_desktop_config.json:
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
6. Reiniciar Claude Desktop completamente

### Capacidades:
- Crear y modificar objetos 3D
- Aplicar materiales (metal, vidrio, madera, plástico)
- Iluminar escenas cinematográficamente
- Inspeccionar escena completa
- Ejecutar código Python en Blender
- Descargar assets de Poly Haven
- Generar modelos 3D con IA (Hyper3D Rodin, Hunyuan3D)
- Screenshots del viewport

### Prompts listos:

PRIMERA ESCENA:
"Crea escena de calabozo medieval con paredes de piedra,
antorchas, cofre del tesoro y dragón. Materiales realistas."

ILUMINACIÓN CINEMATOGRÁFICA:
"Agrega iluminación de tres puntos: key light 45°,
fill light suave opuesto, rim light desde atrás. Look dramático."

ASSET DE POLY HAVEN:
"Descarga árbol realista de Poly Haven, escálalo
y agrega pasto con material verde natural."

### Como producto vendible:
- Renders 3D para clientes de arquitectura y diseño
- Assets 3D para marketing de productos
- Escenas para presentaciones y pitches
- Combinar con Editor Pro Max para video completo
⚠️ Siempre guardar archivo antes de trabajar con Claude

## Ultra Plan — Revisa antes de construir

Claude planea en la nube mientras tu terminal queda libre.
Revisas el plan en el navegador, comentas y ajustas.
Luego ejecutas en la nube (PR automático) o en local.

### Requisitos:
- Claude Code versión 2.1.91+
- Cuenta Claude Code on the web activa
- Repositorio GitHub conectado
- No disponible en Bedrock, Vertex ni Foundry
- En research preview

### Uso:
/ultraplan [descripción de lo que quieres construir]

### Flujo:
1. Escribes /ultraplan + descripción
2. Claude planea en la nube — terminal queda libre
3. Ves ◆ ultraplan ready → abres link en navegador
4. Revisas sección por sección, dejas comentarios
5. Iteras hasta que quede perfecto
6. Eliges: ejecutar en nube (PR automático) o en local

### Prompts listos:

MIGRACIÓN CRÍTICA:
"/ultraplan migrar autenticación de sesiones a JWT
manteniendo usuarios existentes, sin romper sesiones
activas y actualizando los tests"

REDISEÑO UI:
"/ultraplan rediseñar dashboard con Tailwind v4
y dark mode, reutilizando componentes shadcn
y manteniendo rutas del App Router"

FEATURE COMPLETA:
"/ultraplan añadir sistema de suscripciones con Stripe:
pricing page, checkout, webhooks para renovaciones
y panel de usuario para gestionar su plan"

### Cuándo usarlo:
- Cambios grandes en código crítico
- Refactors con muchos archivos
- Features con múltiples piezas (DB, API, UI)
- Cualquier tarea donde no quieras repetir trabajo

### Para agentes de clientes:
- Planear el agente antes de construirlo
- Revisar arquitectura con el cliente antes de ejecutar
- PR automático como entregable visible

## Animaciones — Videos con Remotion + Codex

Pipeline para crear videos con Remotion desde cero.
Un comando instala todo y deja preview corriendo.
github.com/Hainrixz/tododeia-animaciones

### Instalación (desktop):
macOS/Linux:
bash <(curl -fsSL https://raw.githubusercontent.com/Hainrixz/tododeia-animaciones/main/install.sh)

Instala automáticamente: Codex CLI, git, node, npm,
cloudflared, skills de video, proyecto Remotion
y preview con URL pública por túnel.

### Flujo recomendado:
1. Describir video: objetivo, duración, formato (16:9 o 9:16), estilo
2. Revisar preview local y marcar cambios por escena
3. Iterar hasta cerrar narrativa, ritmo y transiciones
4. Exportar solo cuando esté conforme

---

## Instant Landing — Landing completa en 3 preguntas

System prompt que construye landing page completa
en una sola ejecución. Compatible con Claude Code,
Codex, Antigravity, Gemini CLI.

### Flujo:
1. Copiar system prompt (ver abajo)
2. Responder 3 preguntas del negocio
3. Agente instala skills + construye + valida

### 3 preguntas:
1. Nombre del negocio y a qué se dedica
2. Estilo visual y paleta de colores
3. Referencias y requisitos obligatorios

### Estructura mínima que construye:
Navbar, Hero + CTA, Franja de confianza,
Servicios, Beneficios, Proceso, Testimonios,
Contacto con formulario, Footer

### Validaciones automáticas:
lint → build → servidor local → URL localhost

### Prompt corto para usar:
"Quiero una landing page completa en una ejecución.
- Negocio: [nombre + descripción]
- Estilo + colores: [descripción]
- Referencias: [URLs o requisitos]
Máximo 3 preguntas, luego ejecuta.
Busca e instala skills de Vercel.
Corre lint + build + dev. Entrega resumen y localhost."

### Como producto vendible:
- Landing pages express para clientes urgentes
- Combinar con Claude Web Builder para diseño avanzado
- Combinar con Claude SEO para optimización
- Precio sugerido: $300-800 USD por landing express

## Construyendo con IA — De cero a app publicada

Ruta práctica para publicar una app real hoy mismo.
Sin experiencia técnica previa. En español.
github.com/Hainrixz/construyeconia

### Instalación (desktop — un comando):
macOS:
bash <(curl -fsSL https://raw.githubusercontent.com/Hainrixz/construyeconia/main/scripts/setup-mac.sh)

Windows:
irm https://raw.githubusercontent.com/Hainrixz/construyeconia/main/scripts/setup-windows.ps1 | iex

Instala: Node.js, git, Codex CLI, clona repo,
instala dependencias, levanta localhost:3000

### Comandos de Codex:
$start  → inicia build guiado
$imlost → te reencamina cuando no sabes qué pedir
$fixit  → diagnostica y corrige errores
$deploy → publica en Vercel con URL pública

### Ciclo de construcción:
1. Describir claramente lo que quieres
2. Ver resultado en navegador
3. Detectar qué falta o cambiar
4. Pedir cambio exacto a Codex
5. Repetir hasta versión para mostrar

### Ejemplos de prompts buenos:
"Crea app de tareas donde pueda agregar, marcar y
eliminar. Separa por categorías, interfaz minimal."

"App de journal con entradas diarias, etiquetas por
estado de ánimo y vista por calendario."

### Ideas simples que funcionan:
To-do list, journal/mood tracker, generador de frases,
landing personal, contador para objetivo

### Reglas para avanzar rápido:
- Si algo falla → $fixit, no te detengas
- Pide cambios concretos, no "hazlo mejor"
- Primera versión rara vez sale perfecta → iterar
- Publicar rápido > planear perfecto

### Para tu negocio de agentes:
- Usar como onboarding para clientes sin experiencia técnica
- $deploy → URL pública para demos a prospectos
- Combinar con The Architect para proyectos más complejos
- Filosofía: construir → publicar → iterar con feedback real

## Construye Tu App — 3 pasos sin saber programar

### Paso 1 — La Entrevista (en claude.ai):
"Quiero construir [tu idea].
Hazme una entrevista. Pregúntame TODO:
- ¿Qué quiero que haga exactamente?
- ¿Para quién es?
- ¿Cómo quiero que se vea?
- ¿Qué funciones necesita?
- ¿Hay algo parecido que me guste?
Hazme las preguntas una por una.
Cuando tengas todo, dime: ¿armo el plan?"

### Paso 2 — El Plan (en claude.ai):
"Con todo lo que hablamos, arma plan completo:
1. Nombre del proyecto
2. Qué es y para quién (2-3 líneas)
3. Lista de funciones principales
4. Qué se construye PRIMERO (mínimo viable)
5. Qué va DESPUÉS (mejoras)
6. Tecnologías recomendadas
7. Estructura de archivos
Ponlo en un archivo organizado para copiar y guardar."

### Paso 3 — A Construir (en Claude Code):
"Lee el plan que te doy y analízalo completo.
Usa /plan para organizar paso a paso:
- Qué va primero
- Qué sigue después
- Cuándo probamos cada cosa
Cuando apruebe el plan, construye paso a paso.
Cada paso: dime qué hiciste y cómo lo pruebo."

### Ideas para principiantes:
Lista de tareas, página de negocio,
calculadora de presupuestos, quiz/trivia,
portafolio personal

### Para vender a clientes:
- Usar este flujo como metodología de discovery
- La entrevista = entender al cliente
- El plan = propuesta técnica
- Claude Code = ejecución
- Cobrar $500-2,000 USD por proyecto completo

## De Idea a Código — Workflow con 3 modelos

### El flujo completo:
1. /model haiku → avientar idea, hacer preguntas
2. /model sonnet → dar estructura y refinar
3. /model opus → armar plan de ejecución completo
4. /model sonnet → construir paso a paso

### Prompts por modelo:

HAIKU (explorar idea):
"Tengo una idea: [descripción].
Hazme preguntas para entender qué quiero,
quién lo usa, qué problema resuelve y funcionalidades.
Pregúntame una cosa a la vez."

SONNET (refinar):
"Esto es lo que armé. Necesito que:
1. Elabores cada parte con más detalle
2. Me digas qué le falta
3. Organices en estructura clara
4. Corrijas lo que no tenga sentido"

OPUS (planear):
"Arma plan de ejecución completo:
- Arquitectura del proyecto
- Archivos a crear y en qué orden
- Dependencias necesarias
- Pasos numerados
- Decisiones técnicas"

SONNET (construir):
"Ejecuta el plan paso a paso.
Empieza por el paso 1 y avanza en orden.
Si necesitas decisión, pregúntame primero."

---

## Stack Gratuito Para Empezar a Vender

Modelo: construyes con herramientas gratis →
demo funcional al cliente → cliente paga →
ingresos cubren upgrades.

### Stack principal (todos con tier gratis):
- Claude/Claude Code → programar apps y automatizaciones
- Vercel (Hobby gratis) → hosting con deploy automático
- GitHub (gratis) → repositorios y control de versiones
- Supabase (500MB, 50K MAU gratis) → base de datos + auth
- Cloudflare (gratis) → CDN, DNS, SSL
- Clerk (10,000 MAU gratis) → autenticación
- Stripe (sin cuota, ~2.9%/transacción) → cobrar pagos
- Google Gemini/AI Studio (gratis) → prototipar con IA

### Flujo completo de un proyecto:
Cliente necesita web → Figma (diseño) →
Claude Code + Next.js (desarrollo) →
Supabase (base de datos) → Clerk (auth) →
Vercel (deploy) → Cloudflare (DNS) →
Stripe (cobro al cliente)

### Qué puedes construir y vender:
- Landing pages (más fácil de vender)
- Web apps con auth y base de datos
- E-commerce con pagos
- Dashboards en tiempo real
- Automatizaciones con IA

### Tip de inicio:
Empieza con landing pages. Es lo más fácil de vender.
Demo real > mil propuestas en PDF.
Aprende mientras construyes — no antes.

## 3 Servicios Para Tu Agencia de IA

### SERVICIO 1 — MARKETING:
Produce contenido y corre ads sin contratar a nadie.

Skills:
- Marketing Skills (github.com/coreyhaines31/marketingskills)
  → 9 categorías: copy, SEO, ads, email, social, CRO
- Claude SEO (github.com/AgriciDaniel/claude-seo)
  → 13 comandos, auditoría + fix automático
- Claude Ads (github.com/AgriciDaniel/claude-ads)
  → 190+ checks, Meta + Google + TikTok + LinkedIn

### SERVICIO 2 — LEADS:
El que contesta primero gana. Menos de 30 segundos.

Herramientas:
- WhatsApp AgentKit → responde 24/7 automáticamente
- Auto-CRM → califica leads del 0 al 100
- Scrapling → listas de prospectos de Google Maps gratis

### SERVICIO 3 — ECOSISTEMA COMPLETO (el que más paga):
Todo conectado. La operación funciona sola.

Piezas:
- Claude WebKit → página del cliente en vivo
- Claude SEO → aparece en Google Y en ChatGPT
- Claude Code → pegamento que conecta todo

### EL ORDEN EN QUE SE VENDE:
1. PÁGINA (WebKit) → resultado el mismo día
2. LEADS (WhatsApp + CRM + Scrapling) → llenas el pipeline
3. MARKETING (Skills + Ads) → producen y promocionan
4. POSICIONAMIENTO (SEO) → Google + ChatGPT

### Cómo funciona el ecosistema completo:
WebKit captura leads →
WhatsApp AgentKit los contesta →
Auto-CRM los califica →
Marketing Skills + Claude Ads los promocionan →
Claude SEO los posiciona →
Claude Code conecta todo por detrás

### Regla de oro:
NO vendas todo de un jalón.
Empieza con la página → luego leads → luego el resto.
Cada pieza justifica la siguiente.

## 6 Trucos de Boris Cherny — Opus 4.7

Boris Cherny = el ingeniero que construyó Claude Code.
Publicados el 16 abril 2026 después de semanas de uso real.

### 1. AUTO MODE (el más importante):
Shift+Tab → cicla entre modos → dejar en Auto Mode
Claude aprueba solo comandos seguros, pausa si huele raro.
Permite correr 2-3 Claudes en paralelo sin babysittear.
Disponible en planes Max, Teams y Enterprise.

### 2. /fewer-permission-prompts:
Escanea sesión → sugiere lista de comandos seguros →
los agrega al allowlist automáticamente.
Alternativa a Auto Mode para plan Pro.
Correr una vez por semana para afinar.

### 3. RECAPS (vienen prendidos por defecto):
Claude resume qué hizo y qué falta al terminar tareas largas.
Apagar en /config si estorban en sesiones cortas.
Copiar a Obsidian o Linear para handoffs con el equipo.

### 4. FOCUS MODE:
/focus → esconde pasos intermedios, solo muestra resultado final.
⚠️ No usar si eres principiante — necesitas ver cómo piensa Claude.
Combinar con Auto Mode para sesiones largas.

### 5. EFFORT LEVEL (slider de 5 niveles):
low   → tareas triviales (renombrar, formatear)
medium → default, tareas del día a día
high   → refactors, debugging raro
xhigh  → problemas complejos, arquitectura
max    → cuando nada más ha funcionado
También funciona en Sonnet 4.6 y Opus 4.6.

### 6. DALE CÓMO PROBAR SU TRABAJO (el más importante):
Backend → darle cómo arrancar el servidor
Frontend → Claude Chromium extension (code.claude.com/docs/en/chrome)
Desktop → Computer Use

Prompt tipo /go de Boris:
"Claude, construye [tarea].
Cuando termines ejecuta /go:
1. Prueba end-to-end con bash/browser/computer use
2. Corre /simplify para limpiar código
3. Abre Pull Request con resumen
Si algo falla, arréglalo y vuelve a probar antes del PR."

### Orden recomendado para activar:
1. Auto Mode → base de todo
2. Recaps → ya vienen prendidos, solo léelos
3. Dale cómo verificar → sin esto auto mode es riesgo
4. Effort level → moverlo por tarea
5. Focus mode → solo cuando confíes en el modelo
6. /fewer-permission-prompts → una vez por semana

## Claude Design — Del chat a producción

Entorno visual de Anthropic Labs. Sin instalar nada.
Presentaciones, páginas web y apps clickeables en un chat.
Incluido en Pro, Max, Team y Enterprise.
Entrar: claude.ai/design

### Qué puede hacer:
1. PRESENTACIONES → Excel/PPTX/DOCX a slides con narrativa
2. PÁGINAS WEB → clona estilos, inspira desde referencias
3. APPS → prototipos clickeables con estados reales

### 4 formas de ajustar sin re-promptear:
- Comentarios inline (tipo Figma)
- Edición directa de texto en el lienzo
- Sliders custom que Claude crea para tu diseño
- Design system automático desde tu codebase

### Exports disponibles:
PPTX, PDF, HTML standalone, Canva, URL compartible

### Handoff a Claude Code:
"Pásalo a Claude Code" → Claude empaqueta bundle completo.
Incluye: árbol de componentes, design tokens,
breakpoints, accesibilidad, handoff.md con el "por qué"

### Prompts para clientes:

PRESENTACIÓN DE RESULTADOS:
"Arma presentación de 6 slides del Q1.
Datos: [ventas, canal, producto estrella, clientes, meta].
Estilo: clean, paleta oscura, acento turquesa."

LANDING PAGE RÁPIDA:
"Landing de una scroll para [taller/servicio].
Secciones: hero, qué aprenderás, para quién,
testimonios, FAQ, CTA con countdown."

PROTOTIPO DE APP:
"Onboarding clickeable de [nombre app].
4 pantallas: [descripción]. Estilo: [referencias]."

HANDOFF A PRODUCCIÓN:
"Empaqueta para Claude Code:
- Next.js 16 + React 19 + TypeScript + Tailwind v4 + shadcn/ui
- Árbol de componentes con rutas
- Tokens como CSS custom properties
- Notas de accesibilidad ARIA
- handoff.md con design intent"

### Como producto para clientes:
- Prototipos en horas en vez de semanas
- Presentaciones ejecutivas desde Excel bruto
- Validar apps antes de gastar en desarrollo
- Combinar con Claude Web Builder para código final
- Combinar con Claude SEO para optimización

## All Deploy — De tu compu a internet

Cierra el combo: The Architect → Cyber Neo → All Deploy.
Detecta tipo de proyecto, revisa seguridad, preview y deploy.
Open source: github.com/Hainrixz/all-deploy

### Instalación (desktop):
"Instala https://github.com/Hainrixz/all-deploy
Clónalo en ~/.claude/skills/all-deploy"
O: git clone https://github.com/Hainrixz/all-deploy.git ~/.claude/skills/all-deploy

### Uso:
Abrir Claude Code en carpeta del proyecto → /all-deploy

### Flujo automático:
1. Detecta tipo de proyecto
2. Chequeo de seguridad previo
3. URL de preview para verificar
4. Deploy a producción
5. Comando de rollback listo

### Detección inteligente:
- Páginas web/frontend → Vercel
- Agentes, APIs, workers → Railway
- Docker, proyectos pesados → VPS propio

### 3 capas de seguridad:
- Revisión previa (secretos, variables expuestas)
- Preview antes de producción (nunca subes a ciegas)
- Rollback en un segundo si algo falla

### El combo completo de la comunidad:
1. The Architect → plano de 16 secciones
2. Cyber Neo → auditoría de seguridad
3. All Deploy → de idea a URL pública

### Para tu negocio de agentes:
- Entregar agentes al cliente con URL real el mismo día
- Preview para que el cliente apruebe antes de producción
- Rollback instantáneo si algo falla en vivo
- Sin depender de DevOps ni configuración manual

## Opus 4.7 — Cuándo sí, cuándo no

### Los 3 modelos:
- Sonnet 4.6 → día a día, casi no gasta. DEFAULT.
- Opus 4.6 → análisis profundo, código mediano. Plan respira.
- Opus 4.7 → código largo-horizonte, agentes pesados, visión 3x. Come el doble.

### Números de Opus 4.7:
- Código 13% mejor que Opus 4.6 (70% vs 58% CursorBench)
- Visión 3x mejor (98.5% vs 54.5% XBOW)
- API: $5/M tokens entrada, $25/M tokens salida

### Mapa de cuándo usar cada uno:
Día a día → Sonnet 4.6
Pensar en serio → Opus 4.6
Algo gordo + plan $100/$200 → Opus 4.7
Plan Pro $20 → NO usar Opus 4.7 (saldrá el cartelito)

### 6 reglas de prompting oficial Anthropic:
1. Sé claro y directo → "dashboard de ventas con filtro por mes"
2. Dile el PORQUÉ → Claude generaliza la regla a casos nuevos
3. Dale ejemplos → 2-3 ejemplos en etiquetas <ejemplo></ejemplo>
4. Dile qué hacer, NO qué no hacer → instrucciones positivas
5. Dale un rol → "Eres experto en Python para principiantes"
6. Bájale el effort si es simple → Opus 4.7 usa xhigh por default

### 4 prompts anti-desperdicio (en inglés — rinden mejor):

RESPUESTAS CORTAS:
"Provide concise, focused responses. Skip non-essential
context, and keep examples minimal."

CONFIRMAR ANTES DE ACCIONES RIESGOSAS:
"Consider reversibility and potential impact. Take local
reversible actions freely, but for hard-to-reverse actions
or shared systems, ask the user before proceeding."

NO SOBRE-INGENIERÍA:
"Avoid over-engineering. Only make changes directly
requested or clearly necessary. Don't add features,
refactor, or improve beyond what was asked."

INVESTIGAR ANTES DE RESPONDER:
"Never speculate about code you have not opened.
Read the file before answering. Investigate relevant
files BEFORE answering questions about the codebase."

## Platica, Luego Construye — El workflow correcto

### La regla de oro:
No es el modelo, es el prompt.
Plática = explorar. Construcción = ejecutar. NUNCA juntos.

### Las 3 prácticas en orden:

1. APP PRIMERO (si eres nuevo):
   - Usa claude.ai antes de la terminal
   - Pásate a terminal cuando necesites scripts, hooks,
     /loop, subagentes o MCPs avanzados

2. PLATICA PRIMERO — folder separado:
   mkdir ~/Desktop/platica && cd ~/Desktop/platica && claude
   /model haiku  (Haiku para pelotear ideas, casi no gasta)
   git clone https://github.com/Hainrixz/the-architect.git

   Prompt para arrancar:
   "Hola Arquitecto. Quiero construir [idea en 2-3 frases].
   Mi público: [para quién]. Intención: [por qué].
   Nivel técnico: [principiante/intermedio/experto].
   Hazme las preguntas necesarias."

   Prompt para exportar blueprint:
   "Genera blueprint.md con las 16 secciones listo para
   que Claude Code construya sin preguntarme nada."

3. CONSTRUYE EN SESIÓN LIMPIA — folder nuevo:
   mkdir ~/Desktop/mi-proyecto
   cp ~/Desktop/platica/blueprint.md ~/Desktop/mi-proyecto/
   cd ~/Desktop/mi-proyecto && claude --model opus

   Prompt de construcción:
   "Lee blueprint.md completo. Constrúyelo paso a paso
   siguiendo Build Order. No brinques pasos, no preguntes
   lo que ya está en el blueprint, no añadas features extras.
   Si hay decisión técnica no cubierta, pregúntame."

### Por qué funciona (nivel experto):
- Contaminación de contexto: el peloteo contamina la construcción
- Modelo correcto por fase: Haiku/Sonnet para explorar, Opus para construir
- Plan Mode NO resuelve esto — es complementario
- Blueprint exportado = determinístico, compartible, reutilizable

### Las 4 fases de El Arquitecto:
01 Discovery → clasifica en 6 archetypes
02 Deep Dive → preguntas específicas por archetype
03 Architecture → tech stack propuesto y confirmado
04 Generate → blueprint.md de 16 secciones

### Los 6 archetypes:
SaaS App, Marketing Site, Mobile App,
API/Backend, Internal Tool, Content Platform

### Lo que NO debes hacer:
❌ Construir en el folder de plática
❌ Pedir que mejore el plan a media construcción
❌ Meter features extra antes de terminar el blueprint

## Computer Use — Control remoto de tu computadora

Claude ve tu pantalla, mueve el mouse, hace clic y escribe.
Sin API necesaria. Cualquier app que tú uses, Claude también.
Research preview en macOS — Cowork y Claude Code.

### Activación:
Cowork: Settings → Computer Use → activar toggle
Claude Code: claude --computer-use

### Para qué sirve:
- Apps sin API (CRMs viejos, sistemas internos)
- Formularios repetitivos automatizados
- Navegación de menús profundos
- Migración de datos entre apps
- Reportes manuales automatizados
- Testing y QA de aplicaciones

### Prompt para automatizar app sin API:
"Abre [nombre app], navega al formulario de [X]
y llena estos datos:
- Campo 1: [valor]
- Campo 2: [valor]
Revisa que todo esté correcto antes de guardar."

### Prompt para QA automatizado:
"Abre mi proyecto en http://localhost:3000.
Navega todas las páginas del menú principal.
En cada página:
1. Verifica errores en consola
2. Revisa que botones sean clickeables
3. Confirma que imágenes cargan
4. Prueba formularios con datos de prueba
Genera reporte con problemas y sugerencias de fix."

### Combo Computer Use + Dispatch:
Tú te vas → Claude sigue trabajando en tu compu
desde tu celular → trabajo listo cuando regresas

Prompt ejemplo:
"Abre Excel 'reporte-ventas.xlsx', extrae totales
por región, crea gráfica de barras, guarda como PNG.
Luego abre Slack y manda al canal #reportes."

### Para agentes de clientes:
- Automatizar apps legacy sin API
- QA automático antes de cada deploy
- Migración de datos entre sistemas
- Combinar con /loop para tareas recurrentes
⚠️ Empieza con tareas simples para familiarizarte

## Skills Marketplace — 978+ skills disponibles

### Agencia Digital Completa (antigravity-awesome-skills):
978+ skills en 9 categorías. Instalación por proyecto.
github.com/sickn33/antigravity-awesome-skills

Instalación por herramienta:
Claude Code: npx antigravity-awesome-skills --claude
Cursor:      npx antigravity-awesome-skills --cursor
Gemini CLI:  npx antigravity-awesome-skills --gemini

Activar skill: @nombre-skill [prompt]
Ejemplos:
@api-design diseña la API para mi app de pedidos
@security-audit revisa este endpoint por vulnerabilidades
@pricing-strategy ayúdame a definir precios para mi SaaS
@test-generation genera tests para este módulo

9 categorías:
- Arquitectura: sistemas, patrones, microservicios
- Negocio: pricing, monetización, go-to-market
- Data & IA: pipelines, ML, RAG
- Desarrollo: frontend, backend, debugging
- Infraestructura: deploy, CI/CD, Docker, cloud
- Seguridad: auditorías, OWASP, pentesting
- Testing: unit, integration, e2e, TDD
- Workflow: git, code review, automatización
- General: documentación, productividad

Tip: instalar solo 2-3 categorías relevantes por proyecto

---

### Vercel Skills (skills.sh):
Directorio abierto de skills para Claude Code.
Instalar el buscador primero, luego hablarle en español.

Paso 1 — Instalar find-skills:
npx skills add https://github.com/vercel-labs/skills --skill find-skills

Paso 2 — Buscar en lenguaje natural:
"busca skills de frontend"
"encuentra skills para testing"
"qué skills hay para bases de datos?"
"muéstrame skills de deploy en Vercel"

Paso 3 — Claude instala lo que encuentre automáticamente.

Directorio: skills.sh

## Las 3 Herramientas de Claude Code

Sistema para pasar de ideas sueltas a ejecución estructurada.

### 1. Vibe Kanban:
Tablero para coordinar agentes en paralelo, revisar diffs
y ejecutar por tickets.
npx vibe-kanban
github.com/BloopAI/vibe-kanban

### 2. Get Shit Done (GSD):
Meta-prompting y spec-driven dev. Mantiene resultados
consistentes cuando el contexto se degrada.
npx get-shit-done-cc@latest
github.com/gsd-build/get-shit-done

### 3. Claude Code Templates:
Catálogo de agentes, comandos, hooks y MCPs listos.
Evita arrancar de cero en cada proyecto.
npx claude-code-templates@latest
github.com/davila7/claude-code-templates

### Flujo recomendado:
1. Templates → configura base de agentes y comandos
2. GSD → traduce ideas a roadmap y fases ejecutables
3. Vibe Kanban → opera ejecución diaria con tickets
4. Iterar semanalmente con feedback real

---

## Awesome Design MD — 55 diseños famosos gratis

Copia el DESIGN.md de Apple, Stripe, Notion, etc.
y Claude diseña con ese estilo automáticamente.
github.com/VoltAgent/awesome-design-md

### Instalación:
git clone https://github.com/VoltAgent/awesome-design-md.git

### Uso:
1. Elegir diseño en carpeta design-md/
2. cp awesome-design-md/design-md/[empresa]/DESIGN.md ./
3. Decirle a Claude qué construir

### Prompts:

LANDING ESTILO APPLE:
"Lee DESIGN.md en la raíz. Crea landing para [producto].
Mismos colores, tipografía y botones. Responsive con
hero, features, pricing y footer."

PRICING ESTILO STRIPE:
"Tengo DESIGN.md de Stripe. Crea página de precios
con 3 planes, tabla comparativa, toggle mensual/anual y CTA."

REDISEÑAR COMPONENTE:
"Lee DESIGN.md y el archivo [ruta]. Rediseña ese
componente aplicando el sistema de diseño. Solo el
diseño — no cambies la funcionalidad."

### 55 diseños incluidos:
Apple, Stripe, Notion, Figma, Linear, Vercel,
Supabase, Claude, OpenAI, Cursor, Spotify,
Slack, Webflow, MongoDB, Uber, SpaceX y más.

### Tips:
- Combinar diseños: colores de uno + tipografía de otro
- Personalizar colores de marca después de aplicar
- Ver preview.html antes de copiar el DESIGN.md

## /schedule — Agentes en la nube 24/7

A diferencia de /loop (corre en tu máquina),
/schedule corre en servidores de Anthropic.
Tu laptop puede estar apagada.

### Sintaxis (lenguaje natural):
/schedule [frecuencia] + [tarea] + [integraciones]

### Ejemplos reales:

DOCS AUTOMÁTICAS (ejemplo oficial Anthropic):
"/schedule a daily job that looks at all PRs shipped
since yesterday and update our docs based on the changes.
Use Slack MCP to message #docs-update with the changes"

ARREGLAR CI AUTOMÁTICAMENTE:
"/schedule every 2 hours, check CI on main branch.
If any check failed, diagnose, create fix and open PR"

REPORTE DIARIO:
"/schedule daily at 7am, summarize GitHub issues
opened yesterday and send to my email via Gmail MCP"

MONITOREO WEB:
"/schedule every 6 hours, check if [sitio] responds
correctly and load time under 3s. Alert on Slack if off"

COMPETENCIA SEMANAL:
"/schedule every Monday 8am, visit pricing pages of
[competidor1] and [competidor2], compare with precios.csv.
If any dropped 10%+, send Slack message to #alerts"

### /loop vs /schedule:
/loop  → tu máquina, necesita estar encendida, tareas puntuales
/schedule → nube Anthropic, laptop apagada, recurrente 24/7

### Combinar con skills:
skill SEO + /schedule → auditoría semanal automática
skill Ads + /schedule → monitoreo campañas cada 6h
skill Copywriter + /schedule → revisión diaria de contenido

---

## Claude + Codex Hack — $40 hace lo de $100

Claude construye. Codex arregla. Los dos en la misma terminal.
$20 Claude + $20 ChatGPT = lo que el plan de $100 da.

### Instalación (desktop):
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup

### 6 comandos:
/codex:review           → revisión de código (solo lee)
/codex:adversarial-review → revisión agresiva de seguridad
/codex:rescue           → arregla errores (el más importante)
/codex:status           → qué está haciendo Codex
/codex:result           → qué hizo y qué cambió
/codex:cancel           → detener tarea en curso

### Flujo del día:
1. Claude construye la estructura y código principal
2. Salen errores → /codex:rescue (gasta tokens de ChatGPT)
3. Antes de entregar → /codex:review
4. Trabajo en paralelo → /codex:rescue --background

### Por qué ahorra dinero:
Sin hack: Claude construye Y arregla errores → plan se acaba rápido
Con hack: Claude construye, Codex arregla → tokens de Claude duran el doble

### Para clientes:
- Codex revisa código antes de entregar cada agente
- /codex:adversarial-review como parte del proceso de seguridad
- Combinar con Cyber Neo para auditoría completa

## Claude Banana — Prompts profesionales para imágenes

Convierte "un gato en un jardín" en un prompt cinematográfico.
7 ingredientes automáticos. 9 modos especializados.
github.com/Hainrixz/claude-banana

### Los 7 ingredientes que agrega:
01. Sujeto (qué aparece)
02. Estilo visual (foto, 3D, acuarela, cine)
03. Entorno (estudio, naturaleza, ciudad)
04. Iluminación (golden hour, dramática, neón)
05. Acción (movimiento, pose, interacción)
06. Ángulo de cámara (cenital, eye-level, gran angular)
07. Texturas (piel, tela, metal, agua)

### 9 modos especializados:
Cinema, Producto, Retrato, Moda, UI Design,
Logos, Paisajes, Abstracto, Infografías

### Herramientas gratuitas de Google para generar:
Flow: labs.google/fx/tools/flow
Whisk: labs.google/fx/tools/whisk

### Prompt de preset de marca:
"Crea preset con: paleta [colores], estilo [X],
iluminación [Y], texturas [Z].
Aplica a: [descripción de imagen]"

### Reglas:
- Formato narrativo, NO listas de keywords
- Sin "4K", "masterpiece", "hyperrealistic"
- Compatible con Gemini, Midjourney, DALL-E, SD

---

## Humanízalo — Texto de IA → texto humano

Detecta 40+ patrones que delatan IA y los reescribe.
Se revisa 3 veces y necesita 42/60 puntos para aprobar.
github.com/Hainrixz/humanizalo

### Instalación (desktop):
git clone https://github.com/Hainrixz/humanizalo.git ~/.claude/skills/humanizalo

### Uso:
/humanizalo → pegar texto
"Humaniza este texto: [texto]"
"Humaniza el texto en mi-borrador.md"

### 40+ patrones que detecta:
INFLAR: "momento crucial", "papel vital", "hito significativo"
VOCABULARIO IA: "además", "crucial", "profundizar", "navegar"
ESTRUCTURA: contrastes binarios "No es X. Es Y."
FORMATO: guiones largos (—), negritas mecánicas
COMUNICACIÓN: "¡Espero que esto ayude!", frases genéricas

### Señal #1 de texto IA: guiones largos (—) por todos lados

### 6 dimensiones de puntuación:
Directo, Ritmo, Confianza, Autenticidad, Densidad, Alma

### Como producto para clientes:
- Humanizar contenido de marketing antes de publicar
- Emails y propuestas que suenan a persona real
- Combinar con Viral Script Combo para contenido en redes
- Combinar con Open Carrusel para carruseles auténticos

## Claude Diseñador Web Perfecto — 4 herramientas combinadas

### Las 4 piezas:
1. Frontend Design Skill → reglas estéticas de diseño
2. Magic UI MCP → componentes animados (marquee, blur-fade, bento)
3. shadcn/ui MCP → componentes accesibles (botones, forms, cards)
4. Playwright CLI → Claude ve su propio trabajo en navegador real

### Instalación (desktop):
Frontend Design:
claude plugin add anthropics/claude-code/plugins/frontend-design

Magic UI MCP:
npx @magicuidesign/cli@latest install claude

shadcn/ui MCP:
pnpm dlx shadcn@latest mcp init --client claude

Playwright CLI:
npm install -g @anthropic-ai/claude-code-playwright && npx playwright install chromium

### Prompts:

LANDING COMPLETA:
"Diseña landing moderna para [startup/negocio].
Usa Magic UI para animaciones y shadcn para formularios.
Cuando termines, abre con Playwright y verifica.
Si algo no se ve bien, corrígelo."

MEJORAR DISEÑO EXISTENTE:
"Abre http://localhost:3000 con Playwright,
revisa diseño actual y mejora sección hero
con componentes animados de Magic UI. Verifica resultado."

### Tips:
- Shift+Tab → Plan Mode antes de diseñar
- Dile que use Playwright para 2-3 rondas de revisión
- "Magic UI para animaciones, shadcn para formularios"

---

## Claude Animador Web — 3 skills para animaciones reales

### Las 3 habilidades:
1. Frontend Design → tipografía, colores, estructura
2. UI UX Pro Max → 67 estilos, 161 paletas, 57 fuentes
3. Emil Kowalski Skill → transiciones, timing, movimiento

### Instalación (desktop):
claude install-skill https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
npx skills add emilkowalski/skill

Verificar: /skills dentro de Claude Code

### Qué puede animar automáticamente:
- Botones con hover y click
- Transiciones de página fluidas
- Apariciones suaves al scroll
- Menús, tooltips, cards con hover

### Prompt de landing animada:
"Crea landing para [startup]. Hero con animación de entrada,
3 features en columnas, testimonios y CTA final.
Colores oscuros con acentos en azul. Secciones aparecen
al scroll, botones animados al hover."

### Publicar en Vercel:
"Crea repositorio GitHub y sube todo el código."
→ vercel.com → Add New Project → seleccionar repo → Deploy

## Stitch MCP — Diseño UI de Google gratis

Genera interfaces completas con colores, tipografía y HTML.
Gratis con cuenta de Google. Multi-pantalla (web/móvil/tablet).
stitch.withgoogle.com

### Setup:
1. Cuenta en stitch.withgoogle.com → generar API Key
2. npm install @google/stitch-sdk
3. Configurar MCP → leer docs en stitch.withgoogle.com/docs/mcp/setup
   (o decirle a Claude: "configura el MCP de Stitch con esta API key")

### 8 herramientas del MCP:
create_project, generate_screen_from_text,
edit_screens, get_screen, generate_variants,
list_projects, list_screens

### Skills oficiales de Stitch:
npx skills add google-labs-code/stitch-skills --list
- stitch-design → diseño completo con sistema automático
- stitch-loop → sitio multi-página desde un solo prompt
- react:components → convierte pantallas a React
- enhance-prompt → mejora prompts vagos

---

## Diseñador Web Definitivo — 4 herramientas combinadas

### Las 4 piezas:
1. UI/UX Pro Max GO → 67 estilos, 161 paletas, 57 fuentes
2. NanoBanana MCP → genera mockups con Gemini
3. Google Stitch MCP → diseño UI completo con HTML/CSS
4. 21st Dev Magic → componentes premium React/Tailwind

### Instalación (desktop):
UI/UX Pro Max:
npm install -g uipro-cli && uipro init --ai claude

NanoBanana (.mcp.json):
uvx nanobanana-mcp-server@latest + GEMINI_API_KEY

Stitch MCP:
npx @_davideast/stitch-mcp init

21st Dev:
npx @21st-dev/cli@latest install claude --api-key [KEY]
API key en: 21st.dev → API keys

### Flujo completo:
1. Describe qué página necesitas
2. NanoBanana/Stitch → mockup de referencia visual
3. UI/UX Pro Max → paleta, tipografía y estilo por industria
4. 21st Dev → componentes premium para el código
5. Resultado: página profesional lista

### Prompts:

LANDING COMPLETA:
"Crea landing para [startup]. Genera mockup con Stitch,
usa UI/UX Pro Max para paleta y estilo, construye con
componentes de 21st Dev Magic. Next.js + Tailwind CSS."

DASHBOARD:
"Genera mockup con NanoBanana de dashboard para [app].
Replica el diseño con 21st Dev y UI/UX Pro Max para
colores y tipografía profesionales."

COMPONENTES:
"Usa /ui para crear hero section con gradiente y CTA.
Luego crea pricing con 3 planes. Responsive + mejores
prácticas del skill de diseño."

### Tips:
- Siempre empezar con mockup de referencia
- Shift+Tab → Plan Mode antes de diseñar
- Decirle explícitamente qué herramienta usar para cada parte

## Replica Diseños Web — Copia el estilo de cualquier web

### Instalación:
claude install-skill https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

### Prompt de replicación:
"Esta es la landing page [URL]. Replica el layout y espaciado,
tipografía, patrones de animación, y paleta de colores.
Usa UI UX Pro Max y Tailwind CSS. Responsive completo.
Que las plantillas se puedan aplicar a otras páginas.
Si no tienes imágenes, usa NanoBanana para generarlas."

### Qué replica:
Layout y espaciado, tipografía, animaciones,
colores y paleta, estructura de secciones

### Tips:
- Elegir páginas con secciones bien definidas
- Primero replicar diseño, luego cambiar el copy
- Shift+Tab → Plan Mode antes de ejecutar
- Iterar: "hazlo más oscuro", "cambia la fuente"

---

## Clonador de Páginas — Un comando clona cualquier web

Claude abre la página con Chrome real, analiza todo
y construye la réplica en Next.js limpio.
6,700 estrellas GitHub. Open source.
github.com/JCodesMore/ai-website-cloner-template

### Instalación (desktop):
git clone https://github.com/JCodesMore/ai-website-cloner-template.git mi-clon
cd mi-clon && npm install
claude --chrome

### Uso:
/clone-website [URL]

### 5 fases automáticas:
1. Reconocimiento → capturas, colores, fuentes, estructura
2. Fundamentos → Next.js + Tailwind + design tokens
3. Spec → lista de componentes con CSS exactos
4. Construcción paralela → múltiples agentes en paralelo
5. Ensamblaje y QA → compara con original, ajusta

### Para qué sirve:
- Migrar página vieja a Next.js
- Estudiar cómo está hecha una página
- Extraer design system de competencia
- Prototipar: cliente dice "quiero algo así" → clonas y adaptas

### ⚠️ No copia contenido ni imágenes con copyright.
Solo clona el diseño — colores, estructura, layout.
Tú pones tu propio contenido después.

## Protege Tu App — 3 configuraciones esenciales

### 1. ROW-LEVEL SECURITY (RLS) — Supabase/PostgreSQL:
Sin RLS: cualquier usuario puede ver datos de otros.
Con RLS: base de datos filtra automáticamente por usuario.

Prompt para Claude:
"Tengo Supabase con tablas: [lista tus tablas].
Configura RLS para que cada usuario solo vea/edite/borre
sus propios datos. Usa auth.uid(), políticas separadas
para SELECT/INSERT/UPDATE/DELETE, índices en user_id.
Dame SQL completo para el SQL Editor de Supabase."

Verificar: Security Advisor en Supabase Dashboard
Probar: dos usuarios distintos — Usuario B no debe ver datos de A

### 2. CORS — Guardia de seguridad de tu API:
Sin CORS: cualquier página puede hacer requests a tu API.
Con CORS: solo tu dominio exacto puede hablar con la API.

Prompt para Claude:
"Mi frontend está en https://[dominio].com y mi API en
https://api.[dominio].com. Configura CORS para:
- SOLO aceptar requests de mi dominio exacto (nunca *)
- Métodos: GET, POST, PUT, DELETE
- Headers: Authorization y Content-Type
- Soporte credentials: true
- Manejar preflight OPTIONS
Mi stack es: [Next.js/Express/otro]"

Errores NUNCA cometer:
❌ Access-Control-Allow-Origin: *
❌ Reflejar el Origin del request
❌ Mezclar * con credentials
❌ Permitir HTTP además de HTTPS

### 3. SECURITY HEADERS — Letreros de seguridad:
Los 6 headers esenciales:
X-Frame-Options: SAMEORIGIN (anti-clickjacking)
Content-Security-Policy (anti-XSS)
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), camera=()

Prompt para Claude:
"Agrega todos los Security Headers de producción a mi
app [Next.js/Express]. Dominio: https://[dominio].com
Si uso Google Analytics/Stripe, dime qué ajustar en CSP."

Verificar: securityheaders.com → debe dar A+

### Para agentes de clientes:
- Correr estos 3 antes de entregar cualquier agente/app
- Combinar con Cyber Neo para auditoría completa
- Verificar con securityheaders.com como entregable
- Security Advisor de Supabase como check automático

## 5 Skills de Diseño — Todas oficiales de Anthropic, gratis

### Instalación de las 5 de un jalón (desktop):
claude install-skill https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design && claude install-skill https://github.com/anthropics/skills/tree/main/skills/canvas-design && claude install-skill https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder && claude install-skill https://github.com/anthropics/skills/tree/main/skills/theme-factory && claude install-skill https://github.com/anthropics/skills/tree/main/skills/algorithmic-art

### 1. Frontend Design (400K+ usuarios):
Diseña páginas y apps completas. Código real, no mockup.
Prompt: "Diseña landing para [negocio]. Colores [X],
tipografía [Y], animaciones suaves al scroll. Hero,
menú, testimonios y formulario de contacto."

### 2. Canvas Design:
Pósters y gráficos para redes sociales. PNG o PDF.
Prompt: "Crea póster para Instagram de [evento].
Colores [X]. Mínimo texto, máximo impacto visual."

### 3. Web Artifacts Builder:
Apps funcionales sin código. 40+ componentes incluidos.
React + TypeScript + Tailwind automático.
Prompt: "Crea calculadora de precios para [servicio].
Usuario selecciona [opciones] y ve precio al instante."

### 4. Theme Factory:
10 paletas de colores + tipografías perfectas.
Prompt: "Muéstrame todas las paletas y recomienda
la mejor para [tipo de app/marca]."

### 5. Algorithmic Art:
100+ variaciones de arte generativo. Ni Canva ni Figma.
Fractales, espirales, partículas. Controles interactivos.
Prompt: "Genera fractal inspirado en [naturaleza].
Colores [X]. Con controles de densidad y velocidad."

### Referencia rápida:
Frontend Design → páginas y apps completas
Canvas Design   → pósters y gráficos sociales
Web Artifacts   → apps sin código
Theme Factory   → colores + tipografía
Algorithmic Art → arte generativo único

## 5 Skills de Marketing — Tu departamento completo

### 1. Marketing Skills (17K+ estrellas):
34 especialistas: copy, emails, anuncios, precios, retención.
npx skills add coreyhaines31/marketingskills
github.com/coreyhaines31/marketingskills

### 2. Claude SEO:
19 sub-habilidades. Auditoría completa + optimización para IA.
/seo audit <tu-url> → análisis automático
git clone https://github.com/AgriciDaniel/claude-seo.git

### 3. Brand Guidelines (oficial Anthropic, 105K+ estrellas):
Carga tu marca una vez. Claude la aplica en todo automáticamente.
Colores, tipografía, estilo → consistente en presentaciones, web, docs.
claude install-skill https://github.com/anthropics/skills/tree/main/skills/brand-guidelines

### 4. Editor Pro Max (41K+ estrellas):
Videos con palabras. 25 componentes + 10 plantillas.
TikTok, YouTube, Instagram. Subtítulos con Whisper AI.
git clone https://github.com/Hainrixz/editor-pro-max.git

### 5. NotebookLM Skill:
Claude consulta TUS documentos. Cero alucinaciones.
Soporta videos, PDFs, documentos de Google.
mkdir -p ~/.claude/skills && git clone https://github.com/PleasePrompto/notebooklm-skill ~/.claude/skills/notebooklm

### Cómo trabajan juntas:
Marketing Skills → planea campañas y escribe copy
Claude SEO → optimiza para Google y IA (ChatGPT, Perplexity)
Brand Guidelines → todo se ve consistente con tu marca
Editor Pro Max → produce el video sin tocar editor
NotebookLM → respuestas basadas en tus documentos reales

### Para clientes:
- Marketing Skills → estrategia de contenido completa
- Brand Guidelines → identidad visual consistente
- Claude SEO → auditoría como entregable ($500-2,000 valor)
- Editor Pro Max → videos de marketing sin costo de producción
- NotebookLM → base de conocimiento del cliente sin alucinaciones

## 5 Skills Para Crear Contenido

### Banana Cloud — Imágenes con IA:
git clone https://github.com/AgriciDaniel/banana-claude.git && cd banana-claude
Describe qué imagen necesitas → Claude la genera al instante

### NotebookLM Skill — Investigación sin alucinaciones:
pip install notebooklm-py
Le das artículos, PDFs, videos → resumen estructurado
Respuestas basadas SOLO en tus documentos

### Editor Pro Max — Videos sin editor:
(ya documentado en sección anterior)

### Stitch MCP — Diseño web:
(ya documentado en sección anterior)

### Humanízalo — Texto que suena humano:
(ya documentado en sección anterior)

---

## 5 Skills de Productividad — Tu equipo de oficina

### 1. Excel MCP (3.6K estrellas):
Lee y modifica Excel sin tener Microsoft Excel instalado.
Reportes, gráficas, tablas dinámicas automáticos.
uvx excel-mcp-server stdio
github.com/haris-musa/excel-mcp-server

### 2. Obsidian Skills (18K estrellas — creador de Obsidian):
Claude entra a tu bóveda, organiza y conecta notas.
Soporta Markdown, Bases, JSON Canvas, CLI de Obsidian.
npx skills add git@github.com:kepano/obsidian-skills.git

### 3. Context7 (51K estrellas):
Documentación actualizada de 10,000+ librerías.
Elimina respuestas inventadas — fuentes oficiales siempre.
npx ctx7 setup --claude

### 4. Tavily — Buscador de internet en tiempo real:
1,000 búsquedas/mes gratis. Lee páginas web completas.
claude mcp add --transport http tavily https://mcp.tavily.com/mcp
API key en: tavily.com

### 5. Task Master (26K estrellas):
Convierte cualquier idea en plan de tareas estructurado.
Dependencias, criterios de éxito y prioridades por tarea.
claude mcp add taskmaster-ai -- npx -y task-master-ai

### Cómo trabajan juntas:
Task Master → planea qué hacer y en qué orden
Context7 → documentación técnica siempre actualizada
Tavily → busca en internet cuando no está en docs
Obsidian Skills → organiza y da contexto de tus notas
Excel MCP → maneja todos los números y reportes

### Para agentes de clientes:
- Task Master → plan estructurado antes de construir agente
- Context7 → código siempre con documentación actual
- Tavily → agente que busca información en tiempo real
- Excel MCP → agente que genera reportes automáticos
- Obsidian Skills → base de conocimiento del cliente

## Mejora Prompts — Plugin que evalúa prompts antes de ejecutar

Filtra prompts vagos y hace preguntas inteligentes.
31% menos tokens desperdiciados.
github.com/severity1/claude-code-prompt-improver

### Instalación (desktop):
claude plugin marketplace add severity1/severity1-marketplace
claude plugin install prompt-improver@severity1-marketplace
claude (reiniciar)

### Cómo funciona:
- Prompt CLARO → pasa directo sin overhead
- Prompt VAGO → hace 1-6 preguntas antes de ejecutar
- Bypass: usar * al inicio para saltar evaluación
- Comandos con / o # se ignoran automáticamente

### Prompts vagos que activan el plugin:
"arregla el bug" → pregunta: ¿qué archivo? ¿error esperado?
"agrega tests" → pregunta: ¿unitarios o integración? ¿a qué?
"mejora el rendimiento" → pregunta: ¿frontend, backend, BD?

### Prompt claro que pasa directo:
"En src/components/Header.tsx el botón de login no redirige.
onClick llama signIn() pero sin redirect. Agrega
router.push('/dashboard') después de que signIn() resuelva."

---

## Claude Ads — Tu agencia de publicidad en la terminal

190+ checks. Ads Health Score 0-100. 6 agentes en paralelo.
6 plataformas: Google, Meta, YouTube, TikTok, LinkedIn, Microsoft.
github.com/AgriciDaniel/claude-ads

### Instalación (desktop):
macOS/Linux: curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-ads/main/install.sh | bash
Windows: irm https://raw.githubusercontent.com/AgriciDaniel/claude-ads/main/install.ps1 | iex

### 12 comandos:
/ads audit      → auditoría completa multi-plataforma
/ads google     → Google (74 checks: Search, PMax, Display)
/ads meta       → Meta (Pixel/CAPI, creativos, audiencias)
/ads youtube    → YouTube (Skippable, Shorts, Demand Gen)
/ads tiktok     → TikTok (Creative-first, Smart+)
/ads linkedin   → LinkedIn B2B (Lead Gen, Enterprise)
/ads microsoft  → Bing Ads
/ads creative   → auditoría de creativos todas las plataformas
/ads landing    → evaluación de landing pages
/ads budget     → presupuesto y estrategia de pujas
/ads competitor → inteligencia de competidores
/ads plan <tipo> → planificación por industria

### 11 tipos de negocio con plantillas:
SaaS, ecommerce, servicios locales, B2B enterprise,
infoproductos, apps móviles, real estate, salud, finanzas,
agencias, genérico

### Prompts esenciales:

AUDITORÍA COMPLETA:
"/ads audit — Analiza campañas activas. Quiero:
Health Score, 5 problemas urgentes por impacto,
quick wins para hoy, comparación entre plataformas."

ANÁLISIS COMPETIDORES:
"/ads competitor — Competidores: [lista].
Industria: [X]. Analiza sus anuncios y dame
oportunidades donde pueda diferenciarme."

NUEVA CAMPAÑA:
"/ads plan — Negocio: [tipo]. Producto: [desc].
Presupuesto: $[X]/mes. Objetivo: [leads/ventas].
Plan completo con plataformas, estructura y KPIs."

### Como producto para clientes:
- Auditoría de ads como servicio inicial ($500-2,000)
- Gestión mensual con /ads audit semanal
- Reportes con Health Score como entregable
- Combinar con /loop weekly para monitoreo automático

## Claude Copywriter — 24 patrones anti-IA

Detecta y elimina los patrones que delatan texto de IA.
Dos pasadas de revisión. Basado en Wikipedia "Signs of AI writing."
github.com/blader/humanizer

### Instalación (desktop):
mkdir -p ~/.claude/skills
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer

### Los 24 patrones en 5 categorías:
CONTENIDO: "revolucionario", "sin precedentes", frases genéricas
LENGUAJE: "panorama", "catalizador", "sirve como", "funciona como"
ESTILO: guiones largos, negritas innecesarias, emojis decorativos
COMUNICACIÓN: "Espero que esto te sea útil", tono excesivamente amable
RELLENO: "con el fin de", "podría potencialmente", conclusiones vagas

### Proceso de 2 pasadas:
1ª → elimina patrones obvios
2ª → audita lo que sobrevivió la primera limpieza

### Agentes copywriter:

EMAIL MARKETING:
"/humanizer — Crea secuencia de 3 emails para [producto].
Email 1: presentación. Email 2: valor/tip. Email 3: CTA suave.
Max 150 palabras. Tono conversacional como colega.
Pasa cada email por /humanizer antes de entregar."

LANDING PAGE:
"/humanizer — Copy completo para landing de [producto]:
Hero, Problema, Solución, Beneficios con números, Social proof, CTA.
Sin hipérboles. Pasa cada sección por /humanizer."

REDES SOCIALES:
"5 posts para [red] sobre [tema].
LinkedIn: profesional pero cercano sin buzzwords.
Twitter: directo con opinión, max 280 chars.
Pasa cada post por /humanizer."

---

## Skill Vault — Organiza y protege tus skills

Bóveda de habilidades con análisis de seguridad de 13 puntos.
No es un skill — es un agente completo.
github.com/Hainrixz/skill-vault

### Instalación (desktop):
git clone https://github.com/Hainrixz/skill-vault.git && cd skill-vault && claude

### 7 comandos:
/vault-add       → agregar skill (link o código)
/vault-search    → buscar por nombre
/vault-recommend → recomendar según lo que estás construyendo
/vault-discover  → buscar skills nuevos en internet
/vault-list      → todos tus skills organizados
/vault-stats     → cuántos tienes y cuáles usas más
/vault-remove    → borrar skill

### Calificaciones de seguridad:
SAFE      → úsalo con confianza
CAUTION   → revisa antes de usar
DANGEROUS → no lo uses

### 10 categorías de organización:
automation, code-quality, design-ui, devops-deploy,
documentation, organization, productivity, research,
testing, web-development

## 5 Skills Equipo Dev — Tu equipo completo

### Instalación de las 5 de un jalón (desktop):
claude install-skill https://github.com/obra/superpowers && claude install-skill https://github.com/ChrisWiles/claude-code-showcase/tree/main/.claude/skills/systematic-debugging && claude install-skill https://github.com/muratcankoylan/agent-skills-for-context-engineering && claude install-skill https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md && claude install-skill https://github.com/anthropics/skills/tree/main/skills/skill-creator

### 1. Super Power (122K estrellas) — El Arquitecto:
Planea, delega a sub-agentes, revisa y testea solo.
Trabaja en paralelo. No improvisa — planea antes de construir.
claude install-skill https://github.com/obra/superpowers

### 2. Systematic Debugging — El Doctor:
Encuentra causa raíz, no solo tapa síntomas.
Investiga cadena completa de fallos. Previene recurrencia.
claude install-skill https://github.com/ChrisWiles/claude-code-showcase/tree/main/.claude/skills/systematic-debugging

### 3. File Search — El Rapidito:
Busca cualquier archivo en menos de 1 segundo.
Reduce desperdicio de tokens en navegación.
claude install-skill https://github.com/muratcankoylan/agent-skills-for-context-engineering

### 4. Context Optimizer (14K estrellas) — El Optimizador:
Claude solo carga el contexto relevante cuando lo necesita.
Extiende duración de sesiones. Más rendimiento por token.
claude install-skill https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md

### 5. Skill Creator (105K estrellas, oficial Anthropic) — La Fábrica:
Describe lo que necesitas en español → SKILL.md listo.
Crea habilidades personalizadas en menos de 5 minutos.
claude install-skill https://github.com/anthropics/skills/tree/main/skills/skill-creator

### Cómo trabajan juntas:
Super Power → planea y dirige el proyecto completo
Systematic Debugging → arregla errores de raíz
File Search → pasa archivos correctos al instante
Context Optimizer → cuida que no se desperdicien tokens
Skill Creator → construye herramientas que no existen

### Para agentes de clientes:
- Super Power → construir agentes complejos con sub-agentes
- Systematic Debugging → debugging antes de entregar
- Skill Creator → crear skills personalizados por cliente
- Context Optimizer → sesiones largas sin perder el hilo

## Crea Agentes con Claude Code — Flujo completo

### El flujo de 6 pasos:
1. claude (abrir Claude Code en tu proyecto)
2. Shift+Tab → Plan Mode (diseña sin tocar nada)
3. Describir el agente con detalle
4. Claude investiga y entrega plan
5. Revisar y ajustar el plan
6. Shift+Tab → Auto Mode → Claude construye

### Prompt de descripción de agente:
"Quiero crear un agente que [tarea específica].
El agente debe:
1. [acción 1]
2. [acción 2]
3. [output esperado]
Investiga mi proyecto y diseña plan completo."

### Prompt de descubrimiento (si no sabes qué agente crear):
"Hazme preguntas sobre mi día a día y tareas repetitivas.
Sugiere 3 agentes que automaticen lo más tedioso.
Para cada uno: qué haría, qué herramientas, cuánto tiempo ahorraría."

### Programar agentes con /loop:
/loop 2h revisa PRs abiertos y deja comentarios
/loop daily organiza bandeja de entrada por prioridad
/loop 5m verifica que mi sitio esté online

### MCPs que Claude detecta e instala automáticamente:
Gmail, GitHub, Browser, Google Calendar, bases de datos

---

## Managed Agents — Agente 24/7 por $0.70/hora

Agente en la nube de Anthropic. No necesitas compu encendida.
Solo pagas cuando trabaja — tiempo esperando: $0.
platform.claude.com → Agent Quickstart

### Qué puede tocar (vive en la nube):
✅ Gmail, Google Drive, Notion, WhatsApp Business
✅ Slack, Telegram, Google Calendar, Calendly
✅ CRMs, ecommerce, APIs en internet

### Qué NO puede tocar:
❌ Tu computadora local
❌ Archivos solo en laptop
❌ WhatsApp personal del celular
❌ Hardware: impresoras, cámaras

### Prompts para Agent Quickstart:

WHATSAPP CLIENTES:
"Quiero agente que conteste WhatsApp 24h.
Negocio: [descripción]. Debe: saludar con mi tono,
contestar precios/horarios, agendar en Google Calendar,
pasarme el chat si no sabe, mandarme resumen diario por Gmail.
Conectar: WhatsApp Business, Google Calendar, Gmail."

REPORTE SEMANAL:
"Agente que cada lunes 8am arme reporte semanal.
Revisa Gmail (resumen semana), Google Sheet de ventas
(totales + comparación), Google Calendar (juntas semana nueva).
Arma PDF y envíalo por correo con 3 pendientes urgentes.
Conectar: Gmail, Google Drive, Google Calendar."

### Servicios enchufables con MCP:
Gmail, WhatsApp Business, Google Drive, Notion,
Slack, Telegram, Google Calendar, GitHub, Linear

### Tips:
- Empezar con Sonnet → cambiar a Opus si necesitas más razonamiento
- Poner límite mensual en Billing para dormir tranquilo
- Pedir autorización antes de acciones importantes
- Iterar con Claude hasta que el agente quede bien

## Shopify MCP — Tu tienda en piloto automático

31 herramientas oficiales de Shopify. Claude maneja toda la tienda.
Productos, pedidos, clientes, descuentos, inventario.

### Instalación (desktop):
Claude Code:
claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest

Claude Desktop (.mcp.json):
{
  "mcpServers": {
    "shopify-dev-mcp": {
      "command": "npx",
      "args": ["-y", "@shopify/dev-mcp@latest"]
    }
  }
}

### Prompts esenciales:

SUBIR PRODUCTOS EN LOTE:
"Sube estos [N] productos con: nombre, precio, descripción.
Ponles la etiqueta [X] a todos."

CAMBIAR PRECIOS:
"Busca productos con etiqueta [X] y súbeles el precio [N]%.
Muéstrame tabla con precio anterior y nuevo antes de aplicar."

REPORTE DE VENTAS:
"¿Cuáles son mis 5 productos más vendidos esta semana?
Dame nombre, unidades vendidas e ingreso total."

PEDIDOS PENDIENTES:
"Muéstrame pedidos pendientes de envío, ordenados por fecha.
¿Cuáles tienen más de 3 días sin enviarse?"

CREAR DESCUENTO:
"Crea código BIENVENIDO con 20% en toda la tienda.
Solo una vez por cliente. Expira en 30 días."

### 31 herramientas disponibles:
Productos (8): crear, editar, buscar, lote
Pedidos (10): ver, filtrar, cancelar, reembolsar
Clientes (8): buscar, crear, actualizar, segmentar
Descuentos (3): crear códigos, ver activos
Inventario (1): ajustar por ubicación
Etiquetas (1): organizar recursos

---

## Organiza Email con Claude Desktop

Conecta Gmail a Claude Desktop. Sin código.
Plan Pro ($20/mes) o Team requerido.

### Conexión:
Claude Desktop → Settings → Connections → Google Workspace
→ Permitir permisos → listo

### 6 prompts esenciales:

ORGANIZAR POR TEMA:
"Revisa mis últimos 50 correos y agrúpalos por tema:
trabajo, personal, facturas, newsletters y otros."

ETIQUETAR URGENTES:
"De mis correos no leídos, identifica cuáles necesitan
respuesta hoy y cuáles pueden esperar. Explica por qué."

RESUMIR CONVERSACIONES:
"Resume los 3 hilos más largos de esta semana.
Puntos clave y acciones pendientes."

BUSCAR FACTURAS:
"Busca en correos del último mes facturas y recibos.
Lista con fecha, remitente y monto."

BORRADORES DE RESPUESTA:
"Revisa correos sin responder de los últimos 3 días
y redacta borradores cortos y profesionales."

LIMPIEZA:
"Identifica newsletters y correos automáticos repetidos.
Dame lista para decidir cuáles cancelar."

### Seguridad:
- Claude pide confirmación antes de cada acción
- No envía correos sin tu aprobación
- Revocar acceso: Settings → Connections → desconectar

## VibeCoding 101 — De idea a app publicada

### Checklist completo:
1. Escribe idea y público objetivo en una frase
2. Genera PRD con el prompt (ver abajo)
3. Elige herramienta según nivel
4. Conecta backend (Supabase/Firebase)
5. Si usas IA con memoria → agregar Pinecone
6. Cierra MVP y valida flujo extremo a extremo
7. Publica en Vercel → evalúa App Store / Play Store

### Herramientas por nivel:
Sin código: Lovable, Bolt, Base44, Replit
Con algo de código: Cursor, Windsurf, Claude Code
Backend: Supabase, Firebase
Publicar web: Vercel
App Store: $100/año (Apple), $25 único (Google)

### Prompt PRD (para Claude o ChatGPT):
"Actúa como PM senior y crea PRD completo en español.
Contexto: nombre [X], problema [X], usuario [X],
resultado esperado [X], plataformas [X],
must-have [X], nice-to-have [X], restricciones [X].

Incluye: resumen ejecutivo, problema y oportunidad,
ICP, objetivos, alcance v1 (in/out scope), requisitos
funcionales y no funcionales, arquitectura sugerida,
user stories, criterios de aceptación, KPIs, riesgos,
plan en fases (MVP→v1→v2). En markdown, sin relleno."

---

## Arquitecto de Ingresos — Plan de monetización en 24h

Prompt táctico que convierte tu contexto en plan ejecutable.
Principio 80/20. Sin relleno. Con prioridades claras.

### Qué entrega:
1. Diagnóstico táctico adaptado a tu contexto
2. KILLER_MOVE_24H → la acción de mayor impacto hoy
3. LOGIC_GATE → modelo mental aplicado (80/20, Inversión)
4. PROFIT_MATRIX → tabla de 3-7 palancas con:
   impacto %, confianza %, tiempo a resultado, esfuerzo
5. AUDIT_TRAIL → datos verificados vs supuestos
6. SPRINT_PLAN_14_DIAS → plan día a día con entregables

### Cómo usarlo:
1. Copiar el prompt maestro
2. Pegarlo en Claude (en conversación con historial tuyo)
3. Ejecutar primero el KILLER_MOVE_24H
4. Seguir el sprint de 14 días

### Prompt maestro (versión corta para referencia):
"Actúa en MODO EJECUCIÓN DE INGRESOS.
Usa TODO el historial disponible de mi contexto.
Aplica Pareto 80/20 sobre mis canales y activos.
Entrega en orden: diagnóstico táctico → KILLER_MOVE_24H
→ LOGIC_GATE → PROFIT_MATRIX → AUDIT_TRAIL
→ SPRINT_PLAN_14_DIAS → riesgos.
Sin motivación genérica, sin relleno, solo acción."

### Para clientes:
- Usar como sesión de discovery de monetización
- PROFIT_MATRIX = propuesta de valor estructurada
- SPRINT_14_DIAS = entregable concreto para el cliente

## Comando de Sistema — Crea system prompts profesionales

System prompt que te guía por 5 fases para crear
otros system prompts. Una pregunta a la vez.

### Cómo usarlo:
1. Copiar el system prompt completo (tododeia.com/community/comando-de-sistema)
2. Pegarlo en el campo de system prompt de tu agente
3. Responder las preguntas fase por fase
4. Recibir el prompt final en bloque de código listo para copiar

### Las 5 fases:
Fase 1 → propósito, audiencia, plataforma
Fase 2 → nombre, tono, restricciones (nunca hacer/decir)
Fase 3 → conocimiento, contexto, reglas y pasos
Fase 4 → inputs típicos, formato de respuesta
Fase 5 → casos especiales, qué hacer si no sabe

### Estructura del prompt final que genera:
# Identidad (quién es la IA y su propósito)
## Personalidad y Tono
## Contexto y Conocimiento
## Reglas y Comportamiento
## Formato de Respuesta
## Límites

### Para agentes de clientes:
- Usar para crear system prompt del agente de WhatsApp
- Crear system prompt del agente de ventas
- Crear system prompt del CRM personalizado
- Iterar hasta que el cliente lo apruebe

---

## Construye con Estructura — Prompt maestro de producto

Convierte idea suelta en ruta de ejecución clara.
5 fases: Descubrimiento → Planeación → Construcción → Pulido → Entrega

### Cómo usarlo:
"Actúa como mi cofundador técnico.
Idea del producto: [X]
Usuario objetivo: [X]
Problema que resuelve: [X]
Nivel de seriedad: [explorar/uso personal/compartir/lanzar]
Tiempo y recursos: [X]"

### Las 5 fases que ejecuta:
1. DESCUBRIMIENTO → separa v1 de versiones futuras
2. PLANEACIÓN → plan técnico simple, complejidad, dependencias
3. CONSTRUCCIÓN → por etapas visibles, prueba antes de avanzar
4. PULIDO → errores, casos límite, móvil y desktop
5. ENTREGA → deploy, instrucciones, documentación, mejoras v2

### Formato de respuesta que entrega:
Diagnóstico inicial → Plan v1 (in/out scope) →
Enfoque técnico simple → Etapas de construcción →
Dependencias → Validación → Plan de entrega

### Reglas clave del prompt:
- Tú = product owner (decisiones de negocio)
- Claude = cofundador técnico (ejecuta)
- Señala cuando estés sobrecomplicando
- Avanza rápido pero con visibilidad
- Si es muy amplio → pedir recortar a MVP de 7 días
