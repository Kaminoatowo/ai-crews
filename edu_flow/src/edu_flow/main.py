#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from edu_flow.crews.edu_research_crew.edu_research_crew import EduResearchCrew
from edu_flow.crews.edu_content_crew.edu_content_crew import EduContentCrew


class EduFlow(Flow):

    input_variables = {
            "audience_level": "beginner",
            "topic": "Maxwell's equations",
        }

    @start()
    def generate_researched_content(self):
        return EduResearchCrew().crew().kickoff(self.input_variables).pydantic()

    @listen(generate_researched_content)
    def generate_eucational_content(self, plan):
        final_content = []
        for section in plan.sections:
            final_content.append(EduContentCrew().crew().kickoff(self.input_variables).pydantic())
        print(final_content)

def kickoff():
    edu_flow = EduFlow()
    edu_flow.kickoff()


def plot():
    edu_flow = EduFlow()
    edu_flow.plot()


if __name__ == "__main__":
    kickoff()
