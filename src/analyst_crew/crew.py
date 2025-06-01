from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from tools.custom_tools import read_spreadsheet_tool, process_spreadsheet_tool

@CrewBase
class AnalystCrew():
    """AnalystCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    @agent
    def file_processor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['file_processor_agent'], 
            verbose=True,
            tools=[read_spreadsheet_tool],
        )

    @agent
    def data_processor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_processor_agent'], 
            verbose=True,
            tools=[process_spreadsheet_tool],
        )

    @task
    def task_identify_and_read_sheets(self) -> Task:
        return Task(
            config=self.tasks_config['task_identify_and_read_sheets'], 
        )

    @task
    def task_process_and_save_data(self) -> Task:
        return Task(
            config=self.tasks_config['task_process_and_save_data'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AnalystCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
