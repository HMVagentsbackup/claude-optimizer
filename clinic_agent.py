#!/usr/bin/env python3
"""
Agente de Gestión de Citas Médicas — Clínica Salud+
Medical Clinic Appointment Management Agent powered by Claude claude-opus-4-7

Usage:
    python clinic_agent.py

Requires:
    ANTHROPIC_API_KEY environment variable
"""

import os
from datetime import datetime
import anthropic

# ── Simulated In-Memory Database ─────────────────────────────────────────────

PATIENTS: dict[str, dict] = {
    "P001": {"name": "María García",     "dob": "1985-03-15", "phone": "+34 612 345 678"},
    "P002": {"name": "Juan Rodríguez",   "dob": "1972-11-20", "phone": "+34 698 765 432"},
    "P003": {"name": "Ana Martínez",     "dob": "1990-07-08", "phone": "+34 655 123 456"},
}

DOCTORS: dict[str, dict] = {
    "D001": {
        "name": "Dr. Carlos López",
        "specialty": "Medicina General",
        "slots": ["09:00", "09:30", "10:00", "10:30", "11:00", "12:00", "16:00", "16:30", "17:00"],
    },
    "D002": {
        "name": "Dra. Elena Ruiz",
        "specialty": "Pediatría",
        "slots": ["09:00", "09:30", "10:00", "11:00", "12:00", "16:00", "17:00"],
    },
    "D003": {
        "name": "Dr. Miguel Sánchez",
        "specialty": "Cardiología",
        "slots": ["10:00", "10:30", "11:00", "12:00", "15:00", "15:30", "16:00"],
    },
}

APPOINTMENTS: dict[str, dict] = {}
_counter = [1]


def _new_id() -> str:
    apt_id = f"APT{_counter[0]:04d}"
    _counter[0] += 1
    return apt_id


# ── Tool Functions ────────────────────────────────────────────────────────────

def listar_medicos(_: dict) -> str:
    lines = [f"• {did}: {doc['name']} — {doc['specialty']}" for did, doc in DOCTORS.items()]
    return "Médicos disponibles en Clínica Salud+:\n" + "\n".join(lines)


def listar_pacientes(_: dict) -> str:
    lines = [
        f"• {pid}: {pat['name']} (Nac: {pat['dob']}, Tel: {pat['phone']})"
        for pid, pat in PATIENTS.items()
    ]
    return "Pacientes registrados:\n" + "\n".join(lines)


def verificar_disponibilidad(inputs: dict) -> str:
    doctor_id = inputs.get("doctor_id", "")
    fecha = inputs.get("fecha", "")

    if doctor_id not in DOCTORS:
        return f"Error: Médico '{doctor_id}' no encontrado."
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return "Error: Formato de fecha inválido. Use YYYY-MM-DD."

    doc = DOCTORS[doctor_id]
    booked = {
        apt["time"]
        for apt in APPOINTMENTS.values()
        if apt["doctor_id"] == doctor_id
        and apt["date"] == fecha
        and apt["status"] == "confirmada"
    }
    available = sorted(set(doc["slots"]) - booked)

    if not available:
        return f"Sin horarios disponibles para {doc['name']} el {fecha}."
    slots_str = "\n".join(f"  • {t}" for t in available)
    return f"Horarios disponibles — {doc['name']} ({doc['specialty']}) — {fecha}:\n{slots_str}"


def agendar_cita(inputs: dict) -> str:
    patient_id = inputs.get("patient_id", "")
    doctor_id = inputs.get("doctor_id", "")
    fecha = inputs.get("fecha", "")
    hora = inputs.get("hora", "")
    motivo = inputs.get("motivo", "Consulta general")

    if patient_id not in PATIENTS:
        return f"Error: Paciente '{patient_id}' no encontrado."
    if doctor_id not in DOCTORS:
        return f"Error: Médico '{doctor_id}' no encontrado."
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return "Error: Formato de fecha inválido. Use YYYY-MM-DD."

    doc = DOCTORS[doctor_id]
    if hora not in doc["slots"]:
        valid = ", ".join(doc["slots"])
        return f"Error: Horario '{hora}' no válido para {doc['name']}. Horarios disponibles: {valid}"

    for apt in APPOINTMENTS.values():
        if (
            apt["doctor_id"] == doctor_id
            and apt["date"] == fecha
            and apt["time"] == hora
            and apt["status"] == "confirmada"
        ):
            return f"Error: El horario {hora} del {fecha} ya está ocupado. Verifique disponibilidad."

    apt_id = _new_id()
    APPOINTMENTS[apt_id] = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": fecha,
        "time": hora,
        "reason": motivo,
        "status": "confirmada",
        "created_at": datetime.now().isoformat(),
    }

    pat = PATIENTS[patient_id]
    return (
        f"✅ Cita confirmada exitosamente!\n"
        f"  ID de cita: {apt_id}\n"
        f"  Paciente:   {pat['name']}\n"
        f"  Médico:     {doc['name']} ({doc['specialty']})\n"
        f"  Fecha:      {fecha} a las {hora}\n"
        f"  Motivo:     {motivo}"
    )


def consultar_citas_paciente(inputs: dict) -> str:
    patient_id = inputs.get("patient_id", "")
    if patient_id not in PATIENTS:
        return f"Error: Paciente '{patient_id}' no encontrado."

    pat = PATIENTS[patient_id]
    patient_apts = [
        (aid, apt) for aid, apt in APPOINTMENTS.items() if apt["patient_id"] == patient_id
    ]

    if not patient_apts:
        return f"No hay citas registradas para {pat['name']}."

    lines = [f"Citas de {pat['name']}:"]
    for aid, apt in sorted(patient_apts, key=lambda x: (x[1]["date"], x[1]["time"])):
        doc = DOCTORS[apt["doctor_id"]]
        emoji = "✅" if apt["status"] == "confirmada" else "❌"
        lines.append(
            f"  {emoji} [{aid}] {apt['date']} {apt['time']} — "
            f"{doc['name']} — {apt['reason']} ({apt['status']})"
        )
    return "\n".join(lines)


def cancelar_cita(inputs: dict) -> str:
    apt_id = inputs.get("appointment_id", "")
    motivo = inputs.get("motivo_cancelacion", "No especificado")

    if apt_id not in APPOINTMENTS:
        return f"Error: Cita '{apt_id}' no encontrada."
    apt = APPOINTMENTS[apt_id]
    if apt["status"] == "cancelada":
        return f"La cita {apt_id} ya estaba cancelada."

    apt["status"] = "cancelada"
    apt["cancellation_reason"] = motivo
    apt["cancelled_at"] = datetime.now().isoformat()

    pat = PATIENTS[apt["patient_id"]]
    doc = DOCTORS[apt["doctor_id"]]
    return (
        f"❌ Cita cancelada:\n"
        f"  ID: {apt_id}\n"
        f"  Paciente: {pat['name']}\n"
        f"  Médico:   {doc['name']}\n"
        f"  Fecha:    {apt['date']} a las {apt['time']}\n"
        f"  Motivo:   {motivo}"
    )


def reprogramar_cita(inputs: dict) -> str:
    apt_id = inputs.get("appointment_id", "")
    nueva_fecha = inputs.get("nueva_fecha", "")
    nueva_hora = inputs.get("nueva_hora", "")

    if apt_id not in APPOINTMENTS:
        return f"Error: Cita '{apt_id}' no encontrada."
    apt = APPOINTMENTS[apt_id]
    if apt["status"] == "cancelada":
        return "Error: No se puede reprogramar una cita cancelada."

    doctor_id = apt["doctor_id"]
    doc = DOCTORS[doctor_id]

    try:
        datetime.strptime(nueva_fecha, "%Y-%m-%d")
    except ValueError:
        return "Error: Formato de fecha inválido. Use YYYY-MM-DD."
    if nueva_hora not in doc["slots"]:
        valid = ", ".join(doc["slots"])
        return f"Error: Horario '{nueva_hora}' no válido. Horarios disponibles: {valid}"

    for aid, other in APPOINTMENTS.items():
        if (
            aid != apt_id
            and other["doctor_id"] == doctor_id
            and other["date"] == nueva_fecha
            and other["time"] == nueva_hora
            and other["status"] == "confirmada"
        ):
            return f"Error: El horario {nueva_hora} del {nueva_fecha} ya está ocupado."

    old_date, old_time = apt["date"], apt["time"]
    apt["date"] = nueva_fecha
    apt["time"] = nueva_hora
    apt["rescheduled_from"] = f"{old_date} {old_time}"
    apt["rescheduled_at"] = datetime.now().isoformat()

    pat = PATIENTS[apt["patient_id"]]
    return (
        f"🔄 Cita reprogramada exitosamente!\n"
        f"  ID: {apt_id}\n"
        f"  Paciente: {pat['name']}\n"
        f"  Médico:   {doc['name']}\n"
        f"  Anterior: {old_date} a las {old_time}\n"
        f"  Nueva:    {nueva_fecha} a las {nueva_hora}"
    )


def buscar_medico_por_especialidad(inputs: dict) -> str:
    especialidad = inputs.get("especialidad", "")
    matches = [
        f"• {did}: {doc['name']} — {doc['specialty']}"
        for did, doc in DOCTORS.items()
        if especialidad.lower() in doc["specialty"].lower()
    ]
    if not matches:
        available = ", ".join(d["specialty"] for d in DOCTORS.values())
        return (
            f"No se encontraron médicos con especialidad '{especialidad}'.\n"
            f"Especialidades disponibles: {available}"
        )
    return f"Médicos con especialidad '{especialidad}':\n" + "\n".join(matches)


# ── Tool Dispatch ─────────────────────────────────────────────────────────────

TOOL_FUNCTIONS: dict[str, any] = {
    "listar_medicos": listar_medicos,
    "listar_pacientes": listar_pacientes,
    "verificar_disponibilidad": verificar_disponibilidad,
    "agendar_cita": agendar_cita,
    "consultar_citas_paciente": consultar_citas_paciente,
    "cancelar_cita": cancelar_cita,
    "reprogramar_cita": reprogramar_cita,
    "buscar_medico_por_especialidad": buscar_medico_por_especialidad,
}


def execute_tool(name: str, inputs: dict) -> str:
    fn = TOOL_FUNCTIONS.get(name)
    if fn is None:
        return f"Error: herramienta desconocida '{name}'."
    try:
        return fn(inputs)
    except Exception as exc:
        return f"Error ejecutando {name}: {exc}"


# ── Tool Schemas (JSON Schema) ────────────────────────────────────────────────

TOOLS: list[dict] = [
    {
        "name": "listar_medicos",
        "description": "Lista todos los médicos disponibles en la clínica con sus IDs y especialidades.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "listar_pacientes",
        "description": "Lista todos los pacientes registrados en el sistema con sus datos de contacto.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "verificar_disponibilidad",
        "description": (
            "Verifica los horarios disponibles de un médico en una fecha específica. "
            "Llama esta herramienta antes de agendar una cita si no tienes la disponibilidad."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "doctor_id": {
                    "type": "string",
                    "description": "ID del médico (ej: D001, D002, D003)",
                },
                "fecha": {
                    "type": "string",
                    "description": "Fecha en formato YYYY-MM-DD",
                },
            },
            "required": ["doctor_id", "fecha"],
        },
    },
    {
        "name": "agendar_cita",
        "description": "Agenda una nueva cita médica para un paciente con un médico específico.",
        "input_schema": {
            "type": "object",
            "properties": {
                "patient_id": {
                    "type": "string",
                    "description": "ID del paciente (ej: P001, P002, P003)",
                },
                "doctor_id": {
                    "type": "string",
                    "description": "ID del médico (ej: D001, D002, D003)",
                },
                "fecha": {
                    "type": "string",
                    "description": "Fecha de la cita en formato YYYY-MM-DD",
                },
                "hora": {
                    "type": "string",
                    "description": "Hora de la cita en formato HH:MM (24h), ej: 09:00, 10:30",
                },
                "motivo": {
                    "type": "string",
                    "description": "Motivo o descripción de la consulta",
                },
            },
            "required": ["patient_id", "doctor_id", "fecha", "hora", "motivo"],
        },
    },
    {
        "name": "consultar_citas_paciente",
        "description": "Consulta todas las citas (confirmadas y canceladas) de un paciente.",
        "input_schema": {
            "type": "object",
            "properties": {
                "patient_id": {
                    "type": "string",
                    "description": "ID del paciente (ej: P001, P002, P003)",
                },
            },
            "required": ["patient_id"],
        },
    },
    {
        "name": "cancelar_cita",
        "description": "Cancela una cita médica existente.",
        "input_schema": {
            "type": "object",
            "properties": {
                "appointment_id": {
                    "type": "string",
                    "description": "ID de la cita a cancelar (ej: APT0001)",
                },
                "motivo_cancelacion": {
                    "type": "string",
                    "description": "Razón de la cancelación",
                },
            },
            "required": ["appointment_id"],
        },
    },
    {
        "name": "reprogramar_cita",
        "description": "Reprograma una cita existente a una nueva fecha y hora.",
        "input_schema": {
            "type": "object",
            "properties": {
                "appointment_id": {
                    "type": "string",
                    "description": "ID de la cita a reprogramar (ej: APT0001)",
                },
                "nueva_fecha": {
                    "type": "string",
                    "description": "Nueva fecha en formato YYYY-MM-DD",
                },
                "nueva_hora": {
                    "type": "string",
                    "description": "Nueva hora en formato HH:MM",
                },
            },
            "required": ["appointment_id", "nueva_fecha", "nueva_hora"],
        },
    },
    {
        "name": "buscar_medico_por_especialidad",
        "description": "Busca médicos disponibles según una especialidad médica.",
        "input_schema": {
            "type": "object",
            "properties": {
                "especialidad": {
                    "type": "string",
                    "description": "Especialidad médica a buscar (ej: Cardiología, Pediatría, Medicina General)",
                },
            },
            "required": ["especialidad"],
        },
    },
]


# ── System Prompt ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """Eres el asistente virtual de la Clínica Salud+, especializado en gestión de citas médicas.

Puedes ayudar con:
- Agendar nuevas citas médicas
- Consultar citas existentes de pacientes
- Cancelar o reprogramar citas
- Verificar disponibilidad de médicos por fecha
- Buscar médicos por especialidad
- Listar pacientes y médicos registrados

Reglas importantes:
1. Antes de agendar una cita, SIEMPRE verifica la disponibilidad del médico en esa fecha.
2. Confirma los detalles con el usuario antes de ejecutar cancelaciones o cambios.
3. Si el usuario no proporciona el ID del paciente o médico, usa la herramienta de listado para ayudarle a identificarlos.
4. Sé amable, claro, profesional y empático.
5. Si falta información necesaria, pregunta antes de proceder.

Referencia rápida del sistema:
- Pacientes: P001 (María García), P002 (Juan Rodríguez), P003 (Ana Martínez)
- Médicos: D001 (Dr. Carlos López - Medicina General), D002 (Dra. Elena Ruiz - Pediatría), D003 (Dr. Miguel Sánchez - Cardiología)
- Formato fechas: YYYY-MM-DD | Formato horas: HH:MM (24h)
"""

# ── Main Conversational Agent Loop ────────────────────────────────────────────

def run_agent() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: Variable de entorno ANTHROPIC_API_KEY no configurada.")
        return

    client = anthropic.Anthropic()
    messages: list[dict] = []

    print()
    print("═" * 62)
    print("  🏥  Clínica Salud+ — Asistente de Citas Médicas")
    print("       Powered by Claude claude-opus-4-7")
    print("═" * 62)
    print("Escribe tu consulta o 'salir' para terminar.\n")

    while True:
        try:
            user_input = input("Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAsistente: ¡Hasta luego! 😊")
            break

        if not user_input:
            continue
        if user_input.lower() in ("salir", "exit", "quit", "bye", "adios", "adiós"):
            print("Asistente: ¡Hasta luego! Que tenga un excelente día. 😊")
            break

        messages.append({"role": "user", "content": user_input})
        print("\nAsistente: ", end="", flush=True)

        # ── Inner agentic loop: stream response, handle tool calls ────────────
        while True:
            with client.messages.stream(
                model="claude-opus-4-7",
                max_tokens=2048,
                system=SYSTEM_PROMPT,
                tools=TOOLS,
                messages=messages,
            ) as stream:
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                response = stream.get_final_message()

            # Preserve full content (including any thinking blocks) in history
            messages.append({"role": "assistant", "content": response.content})

            if response.stop_reason != "tool_use":
                break  # Final response — exit inner loop

            # Execute all tool calls returned in this response
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = execute_tool(block.name, block.input)
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )

            messages.append({"role": "user", "content": tool_results})
        # ─────────────────────────────────────────────────────────────────────

        print("\n")


if __name__ == "__main__":
    run_agent()
