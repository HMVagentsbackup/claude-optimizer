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
