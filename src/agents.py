from textwrap import dedent
from crewai import agent

class MeetingPrepAgents():
    def research_agent(seld):
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
            #tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                As a Strategy Advisor, your expertise will guide the development of
                talking points, insightful questions, and strategic angles
                to ensure the meeting's objective are achieved."""),
            verbose=True
        )