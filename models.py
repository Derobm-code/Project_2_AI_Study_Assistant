from typing import Annotated

from pydantic import BaseModel
from annotated_types import Len

class InterviewQuestion(BaseModel):
    question: str
    testing: str
    model_answer: str


class InterviewQuestions(BaseModel):
    questions: Annotated[
        list[InterviewQuestion],
        Len(min_length=5, max_length=5)
    ]