import os
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

res = generator(
    "working with technology is ",
    max_length=300
)

clear = lambda: os.system('cls')
clear()

print(res)