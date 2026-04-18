# Clínica Salud+ — Agente de Gestión de Citas Médicas

Agente de automatización para una clínica médica que gestiona citas mediante lenguaje natural, impulsado por **Claude claude-opus-4-7**.

## Características

- **Agendar citas** — busca disponibilidad y confirma con el paciente antes de reservar
- **Consultar citas** — historial completo de citas por paciente
- **Cancelar citas** — con registro del motivo
- **Reprogramar citas** — cambia fecha/hora verificando disponibilidad
- **Buscar médicos** — por especialidad (Medicina General, Pediatría, Cardiología)
- **Listar médicos y pacientes** — directorio completo del sistema

## Arquitectura

```
Usuario (lenguaje natural)
        │
        ▼
  Claude claude-opus-4-7  ←──── System Prompt + 8 herramientas
        │
        ▼ (tool_use loop con streaming)
  Funciones Python
  (base de datos simulada)
```

El agente usa un **bucle agentic manual con streaming**: Claude decide qué herramientas usar, las llama en paralelo si es necesario, y genera la respuesta final en streaming token a token. El historial completo de la conversación se mantiene entre turnos.

## Instalación

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
python clinic_agent.py
```

## Ejemplo de uso

```
Tú: Quiero pedir cita con un cardiólogo para el 2026-05-10

Asistente: Verificaré la disponibilidad del Dr. Miguel Sánchez (Cardiología)
para el 10 de mayo de 2026...

Horarios disponibles: 10:00, 10:30, 11:00, 12:00, 15:00, 15:30, 16:00

¿A qué hora prefiere? ¿Y puede darme su nombre o ID de paciente?

Tú: Soy María García (P001), a las 10:00

Asistente: ✅ Cita confirmada!
  ID de cita: APT0001
  Paciente:   María García
  Médico:     Dr. Miguel Sánchez (Cardiología)
  Fecha:      2026-05-10 a las 10:00
  Motivo:     Consulta de Cardiología
```

## Herramientas disponibles

| Herramienta | Descripción |
|---|---|
| `listar_medicos` | Lista médicos con IDs y especialidades |
| `listar_pacientes` | Lista pacientes registrados |
| `verificar_disponibilidad` | Horarios libres por médico y fecha |
| `agendar_cita` | Crea una nueva cita |
| `consultar_citas_paciente` | Historial de citas de un paciente |
| `cancelar_cita` | Cancela una cita existente |
| `reprogramar_cita` | Cambia fecha/hora de una cita |
| `buscar_medico_por_especialidad` | Filtra médicos por especialidad |

## Datos de demostración

**Pacientes:** P001 (María García), P002 (Juan Rodríguez), P003 (Ana Martínez)

**Médicos:**
- D001: Dr. Carlos López — Medicina General
- D002: Dra. Elena Ruiz — Pediatría  
- D003: Dr. Miguel Sánchez — Cardiología
