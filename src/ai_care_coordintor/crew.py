from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from ai_care_coordintor.tools.custom_tool import (
	DischargeTranslationTool, RiskMonitoringTool, LogisticalCoordinationTool, RecoveryOrchestrationTool
)

@CrewBase
class CareCoordinatorCrew():
	"""CareCoordinatorCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def orchestrator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['orchestrator_agent'],
			verbose=True,
			tools=[RecoveryOrchestrationTool()],
		)

	@agent
	def translator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['translator_agent'],
			verbose=True,
			tools=[DischargeTranslationTool()],
		)

	@agent
	def monitoring_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['monitoring_agent'],
			verbose=True,
			tools=[RiskMonitoringTool()],
		)

	@agent
	def logistics_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['logistics_agent'],
			verbose=True,
			tools=[LogisticalCoordinationTool()],
		)
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task