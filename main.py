from fastapi import FastAPI, HTTPException, status , Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from typing import Optional
app = FastAPI()

class Issue(BaseModel): #response model
    bookTitle: str
    genre: str
    published: bool = True #deafault Value
    rating: Optional[int]  = None

my_issues = [
    {"bookTitle": "To Kill a Mockingbird", "genre": "Fiction", "id": 123},
    {"bookTitle": "1984", "genre": "Dystopian", "id": 456},
    {"bookTitle": "Pride and Prejudice", "genre": "Romance", "id": 789},
    {"bookTitle": "The Great Gatsby", "genre": "Classic", "id": 321},
    {"bookTitle": "The Lord of the Rings", "genre": "Fantasy", "id": 654},
    {"bookTitle": "Harry Potter and the Philosopher's Stone", "genre": "Fantasy", "id": 987},
    {"bookTitle": "The Catcher in the Rye", "genre": "Coming-of-Age", "id": 234},
    {"bookTitle": "The Hobbit", "genre": "Fantasy", "id": 567},
    {"bookTitle": "Moby-Dick", "genre": "Adventure", "id": 890},
    {"bookTitle": "To the Lighthouse", "genre": "Modernist", "id": 432}
]

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/issues')
async def get_all_issue_details():
    return {"issue_details": my_issues}

@app.post("/newissues")
async def create_issue(issue: Issue):
    issue_dict = issue.dict()
    issue_dict["id"] = randrange(0,1000)
    my_issues.append(issue_dict)
    return {"new_book_issued": issue_dict}

# @app.get("issues/{id}")
# def get_post(id:int, response: Response):
#     issue = find_issue(id)
#     if not issue:
#         response.status_code = status.HTTP_404_NOT_FOUND
#     return {"issue details": issue}

@app.get("/issues/{id}")
def get_post(id:int):
    issue = {"bookTitle": "To the Lighthouse", "genre": "Modernist", "id": 432}
    issue = find_issue(id)
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id ={id} was not found")
    return {"issue_details":issue}


def find_issue(id: int):
    for issue in my_issues:
        if issue["id"] == id:
            return issue
    return None 

@app.delete("/issues/{id}")
async def delete_issue(id:int):
    print(id)
    index = find_issue(id)
    if not index :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with Id ={id} was not found")
    my_issues.pop(index)
    return {"Message":"Post deleted"}


def find_index(id: int):
    for i,j in enumerate(my_issues):
        if j["id"] == id:
            return i

@app.put(("/issues/{id}"))
def update_issue(id:int,issue: Issue):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Issue with Id = {id} was not found")
    updated_issue = issue.dict()
    updated_issue["Id"] = id
    my_issues[index]  = updated_issue
    return{"Message":f"Issue with {id} updated"}