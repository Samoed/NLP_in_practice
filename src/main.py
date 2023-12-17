import gradio as gr

from src.model import Model
from src.propmpts import VACANCY, EXAMPLE_RESUME, ICONIC_RESUME

model = Model()


def print_suggestions(resume, vacancy, iconic_resume) -> str:
    return model.resume_suggestion(resume, vacancy, iconic_resume)


def interface() -> gr.Interface:
    with gr.Blocks(title="Resume suggestions") as block:
        with gr.Row():
            resume = gr.TextArea(lines=20, label="Resume", placeholder="Paste your resume here", value=EXAMPLE_RESUME)
            vacancy = gr.TextArea(lines=20, label="Vacancy", placeholder="Paste vacancy description here",
                                  value=VACANCY)
        with gr.Row():
            iconic_resume = gr.TextArea(lines=20, label="Iconic Resume", placeholder="Iconic resume will appear here",
                                        value=ICONIC_RESUME)
            result = gr.TextArea(lines=20, label="Result", placeholder="Result will appear here", interactive=False)
        submit = gr.Button(value="Submit")

        submit.click(print_suggestions, [resume, vacancy, iconic_resume], result)
    return block


if __name__ == "__main__":
    interface().queue().launch()
