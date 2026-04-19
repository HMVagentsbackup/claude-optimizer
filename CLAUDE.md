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
