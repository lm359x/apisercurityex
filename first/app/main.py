from fastapi import FastAPI

app = FastAPI()


@app.get("/main")
async def get_main():
    return {
        "foo": "hello",
        "first": "amigo"
    }


async def get_person():
    return {
        "name": "John Gold",
        "age": "75"
    }
