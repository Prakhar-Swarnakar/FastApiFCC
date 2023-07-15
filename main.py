from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/issue')
async def issue_details():
    return {"issue_details": "These are the details of the book issue"}

@app.post("/issuebook")
async def issue_book(payload: dict= Body(...)):
    print(payload)
    return {"new_book_issued": f"successfully Issued {payload['title']}"}
