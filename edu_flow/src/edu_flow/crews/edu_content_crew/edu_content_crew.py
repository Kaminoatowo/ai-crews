from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class EduContentCrew():
    """EduContentCrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_writer"],
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"],
            verbose=True
        )

    @agent
    def quality_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["quality_reviewer"],
            verbose=True
        )
        
    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["writing_task"]
        )

    @task
    def editing_task(self) -> Task:
        topic = self.input_variables.get("topic")
		audience_level = self.input_variables.get("audience_level")
		file_name = f"{topic}_{audience_level}.md".replace(" ", "_")
		output_file_path = os.path.join('output', file_name)
		
        return Task(
            config=self.tasks_config["editing_task"],
            output_file=output_file_path
        )

    @task
    def quality_review_task(self) -> Task:
        return Task(
            config=self.tasks_config["quality_review_task"],
            output_file="report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EduContentCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
