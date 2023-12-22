FROM python:3.10

RUN wget https://huggingface.co/Samoed/resume_llm_merged-gguf/resolve/main/model_with_lora-q2_k.gguf?download=true -P /model
#COPY ./models/llama-2-7b-airplane-tickets-q2_k.gguf /models/llama-2-7b-airplane-tickets-q2_k.gguf
WORKDIR "/src"
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV PYTHONPATH=/src
COPY ./src .
CMD ["python", "main.py"]