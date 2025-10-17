from fastapi import FastAPI

app = FastAPI()

# primr end-poin
@app.get('/')
def read_root():
    return{'saludo':'hola'}