import vertexai
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
)

class IncomeStatement:

    def __init__(self) -> None:
            self.total_revenue = FunctionDeclaration(
                name="get_total_revenue",
                description="Get the last 12 month company’s total revenues finance report.",
                parameters={
                    "type": "object",
                    "properties": {
                        "total_revenue": {"type": "string", "description": "company name"}
                    },
                },
            )
            
            self.income_statement_tool = Tool(
                function_declarations=[
                    self.total_revenue,
                   
                ],
            )

    def getTools(self):
          return self.income_statement_tool