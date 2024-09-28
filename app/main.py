from pydoc import text
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from urllib.parse import unquote
from sentence_transformers import SentenceTransformer
import uvicorn
import faiss
import click
import json


import numpy as np

from typing import List

with open('data/tags_list.json', 'r', encoding='utf-8') as f:
    tags_list = json.load(f)

app = FastAPI()
index = faiss.read_index("data/tags_index.ivf", faiss.IO_FLAG_MMAP)
model = SentenceTransformer('DeepPavlov/rubert-base-cased-sentence', )

TOP_N = 3
# 1, 2, 3, 5, 10

@app.get(f"/tags/")
async def get_tags(text: str) :
    click.echo(f"Text: {text}")
    text_emb_vector = model.encode(text, convert_to_tensor=True).cpu()
    score, prediction = index.search(np.array([text_emb_vector]), TOP_N)
    tags_result = np.array(tags_list)[prediction]
    click.echo(f'Tags: {tags_result}')
    return JSONResponse(content={"tags": tags_result.tolist()})

@click.command()
@click.option('--port', type=int, default=8008, help='Port to listen on')
def main(port):
    click.echo(f'Server listening on port {port}')
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == '__main__':
    main()

