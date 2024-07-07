
import vertexai, requests, sys, os
sys.path.insert(0, f'{os.getcwd()}/tools')
from income_statement import IncomeStatement
from google_finance import GoogleFinance
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
)

class Advisor:
    PROJECT_ID = "data-science-246008" 
    LOCATION = "us-central1" 

    def __init__(self) -> None:
        vertexai.init(project=self.PROJECT_ID, location=self.LOCATION)
        self.incomeStatement=IncomeStatement()
        self.googleFinance=GoogleFinance()
       

        self.model = GenerativeModel(
            "gemini-1.5-pro-001",
            generation_config=GenerationConfig(temperature=0),
            tools=[self.googleFinance.getTools()],
        )
        self.chat = self.model.start_chat()

    def advise(self):
        prompt = """
                    read some news about finance
                """

        response = self.chat.send_message(prompt)
        res = response.candidates[0].content.parts[0]
        return str(res)

