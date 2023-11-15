"""Assessment module."""

from linga.scenario import Levels


def create_assessment_prompt(
    comics_text: str, chat_history: str, level: Levels, native_language: str
) -> str:
    """creates assessment prompt"""
    requested_questions_count = 10
    prompt = (
        f"You are an English teacher, teaching foreign students, who speak {native_language}. "
        f"You gave them comics to read. Here is the comics text {comics_text} that you need to "
        f"prepare multiple choice questions for to check how well students learned the new "
        f"English words from the comics. Write {requested_questions_count} questions in "
        f"{native_language} and send them to me. Make sure to fit the questions for {level.name} "
        f"level. Use the following format: 'question' 'answer1' 'answer2' 'answer3' 'answer4' "
        f"'correct answer' for each question and return a json in the following schema]"
        """{
             "$schema": "http://json-schema.org/draft-04/schema#",
              "type": "array",
              "items": [
                {
                 "type": "object",
                  "properties": {
                         "question": {
                         "type": "string"
                    },
                    "answer1": {
                         "type": "string"
                    },
                    "answer2": {
                         "type": "string"
                    },
                    "answer3": {
                         "type": "string"
                    },
                    "answer4": {
                         "type": "string"
                    },
                    "correct_answer": {
                         "type": "string"
                    }
                  },
                  "required": [
                    "question",
                    "answer1",
                    "answer2",
                    "answer3",
                    "answer4",
                    "correct_answer"
                  ]
                }
              ]
            }"""
    )

    if chat_history:
        prompt += (
            f""
            f"Use the following chat history {chat_history} to see what questions were already "
            f"asked. Repeat one of questions that was repeated less than others and that user "
            f"gave correct answer for. Also repeat one question that user answered incorrectly."
        )

    return prompt
