from fastapi import FastAPI

app = FastAPI()


@app.get("/main")
async def main():
    return {
        "bar": "hola",
        "second": "world"
    }


@app.get("/person")
async def person():
    return {
        "profession": "Developer",
        "company": "SomeOne"
    }
