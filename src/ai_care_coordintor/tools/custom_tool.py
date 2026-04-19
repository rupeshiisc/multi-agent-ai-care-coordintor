from crewai.tools import BaseTool
from ai_care_coordintor.tools.tool_helper import ToolHelper

class DischargeTranslationTool(BaseTool):
	name: str = "Discharge Translation Tool"
	description: str = "Analyzes clinical discharge plans and produces a simplified daily checklist."

	def _run(self, discharge_text: str = None) -> str:
		# Analyze discharge plan and return checklist
		return ToolHelper.analyze_discharge(discharge_text)


class RiskMonitoringTool(BaseTool):
	name: str = "Risk Monitoring Tool"
	description: str = "Monitors symptoms and biometric data, evaluates health trends, and triggers alerts."

	def _run(self, symptom_report: str = None, biometric_data: str = None) -> str:
		return ToolHelper.monitor_risk(symptom_report, biometric_data)


class LogisticalCoordinationTool(BaseTool):
	name: str = "Logistical Coordination Tool"
	description: str = "Ensures medication adherence and schedules appointments, resolving logistical issues."

	def _run(self, care_plan: str = None) -> str:
		return ToolHelper.coordinate_logistics(care_plan)


class RecoveryOrchestrationTool(BaseTool):
	name: str = "Recovery Orchestration Tool"
	description: str = "Synthesizes agent outputs into a unified recovery summary and maintains a reasoning log."

	def _run(self, translator_output: str = None, monitoring_output: str = None, logistics_output: str = None) -> str:
		return ToolHelper.orchestrate_recovery(translator_output, monitoring_output, logistics_output)
