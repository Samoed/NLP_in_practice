from llama_cpp import Llama

from src.prompts import PROMPT


class Model:
    def __init__(self, path: str = "model/mistral-7b-openorca.Q2_K.gguf"):
        self.llama = Llama(
            model_path=path,
            n_ctx=2048 * 2,
            n_gpu_layers=30,
        )

    def resume_suggestion(self, resume: str, vacancy: str, iconic_resume: str) -> str:
        prompt = PROMPT.format(
            example_resume=resume,
            vacancy=vacancy,
            iconic_resume=iconic_resume,
        )
        completion = self.llama(prompt)
        return completion["choices"][0]["text"]
