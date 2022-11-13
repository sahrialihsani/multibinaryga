from fastapi import FastAPI
from pydantic import BaseModel

import src.main as main

class InputParams(BaseModel):

    n_chrom: int
    max_gen: int
    lower_x1: float
    upper_x1: float
    lower_x2: float
    upper_x2: float
    precision: int
    crossover_rate: float
    mutation_rate: float

app = FastAPI()

@app.get("/")
async def home():
    return {"Hello": "World"}

@app.post("/run")
async def run(params: InputParams):

    params = dict(params)

    try:
    
        last_gen, solution_list = main.main(params)

        best_gen = main.get_best_gen(solution_list)

    except RuntimeError as e:

        return f"Some error happened {e}"

    return {"solution_list": solution_list, "best_gen": best_gen}




