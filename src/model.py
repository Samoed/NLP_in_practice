from llama_cpp import Llama

from prompts import PROMPT


class Model:
    def __init__(self, path: str = "model/model_with_lora-q2_k.gguf"):
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
        completion = self.llama(prompt, temperature=0.2, top_k=15, top_p=0.95)
        return completion["choices"][0]["text"]
