from fastapi import FastAPI, Response, HTTPException, status
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Atributos(BaseModel):
    descricao = str
    responsavel = str 
    situacao = str
    nivel = int
    prioridade = int


atributos: list[Atributos] = []


@app.get('/atributos')
async def obt_inf(skip : int | None = None, limite: int | None = None):
    inicio = skip
    
    if skip in limite:
        fim = skip + limite
    else:
        fim = None
    
    return atributos[inicio:fim]


@app.get('/atributos/{atributos_ID}')
async def obiter_1(atributos_ID: int):
    for atrib in atributos:
        if atributos_ID == atributos_ID:
            return atributos
    
    
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Não encontrado = {atributos_ID }')


@app.get('/ativ/situacao/{atb_situacao}')
async def obiter_situacao(atb_situacao: str):
    return [atb_situacao for atributos in Atributos if atributos.situacao == atb_situacao]


@app.delete("/atributos/{atributos_ID}", status_code=status.HTTP_204_NO_CONTENT)
def remover_S(atriutos_ID: int):
    for s_atual  in atributos:
        if s_atual == atributos_ID:
            atributos.remove(s_atual)
        return
    
    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail="Não encontrado")