from fastapi import FastAPI

# obj
app = FastAPI()

name: str = 'Test'


@app.get('/')
def home():
    return {"message": "Hello world"}

@app.get('/name/awesome/asd/{id}', )
def name(): 
    return {'name': 'Muhammad'}

