# Multi-Agent AI Care Coordinator

This project implements a multi-agent system to support patient care coordination, leveraging AI agents to automate, monitor, and optimize the recovery journey for patients. The system is designed to enhance communication, safety, and efficiency for patients, caregivers, and clinical teams.

## Features

- **Orchestrator Agent**: Coordinates the recovery journey by managing information flow between specialists and identifying high-priority health shifts. Acts as the central intelligence, synchronizing hospital records, pharmacy updates, and caregiver calendars.
- **Translator Agent**: Converts complex medical instructions into simple, actionable daily checklists tailored to the patient's literacy level, using Watson Discovery to analyze dense clinical notes and discharge plans.
- **Monitoring Agent**: Tracks patient-reported symptoms and vitals, distinguishing between routine habits and serious health shifts, and provides early risk detection and escalation.
- **Logistics Agent**: Resolves real-world barriers such as transportation, scheduling conflicts, and pharmacy delays by integrating with EHR and external systems.

## Agents

Agents are defined in `src/ai_care_coordintor/config/agents.yaml`:

- **orchestrator_agent**: Care Orchestrator, manages information flow and synchronizes all stakeholders.
- **translator_agent**: Instruction Translator, simplifies medical instructions for patients.
- **monitoring_agent**: Companion Monitor, tracks symptoms and detects risks.
- **logistics_agent**: Medical Coordinator, handles logistics and real-world barriers.

## Tasks

Tasks are defined in `src/ai_care_coordintor/config/tasks.yaml`:

- **discharge_translation**: Analyzes unstructured clinical discharge plans and produces a simplified daily checklist.
- **risk_monitoring**: Monitors symptoms and biometric data, evaluates health trends, and triggers alerts for complications.
- **logistical_coordination**: Ensures medication adherence and schedules appointments, resolving logistical issues.
- **recovery_orchestration_task**: Synthesizes agent outputs into a unified recovery summary and maintains a transparent reasoning log.

## Installation

1. Clone the repository:

```sh
git clone <repo-url>
cd multi-agent-ai-care-coordintor
cd src
```

src\.venv\Scripts\activate 2. **(Recommended)** Create and activate a virtual environment (.venv):

```sh
# On Windows (from src directory)
python -m venv .venv
.venv\Scripts\activate
```

# On macOS/Linux (from src directory)

```sh
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies (Python 3.10–3.13 required):

> **Important:** Run this command from the `src` directory (where `pyproject.toml` is now located):

```sh
pip install -e .
```

This will install the package in editable mode and make the `ai_care_coordintor` module and scripts available system-wide.

## Usage

After installation, you can run the application using the installed scripts from anywhere (ensure your virtual environment is activated):

```sh
ai_care_coordintor   # Main entry point
run_crew             # Alias for main entry point
train                # For training mode (if implemented)
replay               # For replay mode (if implemented)
test                 # For test mode (if implemented)
```

> **Note:**
>
> - The main entry point is `run()` in `ai_care_coordintor/main.py`.
> - Ensure your terminal's working directory is the `src` folder when installing.
> - You can modify or extend the input data in `main.py` as needed for your use case.

## Project Structure

- `src/ai_care_coordintor/` — Main package
  - `main.py` — Entrypoints for running, training, replaying, and testing
  - `config/agents.yaml` — Agent definitions
  - `config/tasks.yaml` — Task definitions

## Requirements

- Python 3.10–3.13
- [crewai](https://github.com/joaomdmoura/crewAI) >= 0.80.0

## License

This project is licensed under the terms of the LICENSE file in this repository.
python -m src.ai_care_coordintor.main
