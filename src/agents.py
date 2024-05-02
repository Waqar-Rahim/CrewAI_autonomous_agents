from textwrap import dedent
from crewai import Agent

from tools import ExaSearchToolset


class MeetingPrepAgents():
    def research_agent(self):
        return Agent(
            role="research Specialist",
            goal='Conduct through research on people and companies involved in the meeting',
            tools=[],
            backstory=dedent("""\
              As a Research Specialist, your mission is to uncover detailed information
              about the individuals and entities participating in the meeting. Your insights
              will lay the groundwork for strategic meeting preparation."""),
            verbose=True  
                
        )
    def industry_analysis_agent(self):
        return Agent(
            role="Industry Analyst",
            goal='Analyze the current industry trends, challenges, and oppertunities relevant to the meetings context',
            tools=[],
            backstory=dedent("""\
                As a Industry Analyst, your analysis will identify key trends,
                potential chanllenges facing the industry, and strategic oppertunities that could be leveraged
                during the meeting for strategic advantage."""),
            verbose=True
        )
    
    def meeting_strategy_agent(self):
        return Agent(
            role='Meeting Strategy Advisor',
            goal='Develop talking points, question, and strategic angles for the meeting',
            backstory=dedent("""\
                As a Strategy Advisor, your expertise will guide the development of
                talking points, insightful questions, and strategic angles
                to ensure the meeting's objective are achieved."""),
            verbose=True
        )

    def summary_and_briefing_agent(self):
        return Agent(
            role='Summary and Briefing Coordinator',
            goal='Compile all the research findings, industry analysis, and strategic talking points into a concise, comprehensive briefing document for the meeting',
            backstory=dedent("""\
                As a Summary and Briefing Coordinator, your report will include sections for
                participant bios, industry overview, talking points, and strategic recommendations."""),
            verbose=True
        )