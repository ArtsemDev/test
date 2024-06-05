import contextlib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from models import Base, engine, session_maker, Request


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


class RequestForm(BaseModel):
    name: str


app = FastAPI(lifespan=lifespan)


@app.post(path="/request", response_model=RequestForm)
async def create_request(data: RequestForm):
    with session_maker() as session:
        r = Request(**data.model_dump())
        session.add(r)
        try:
            session.commit()
        except:
            raise HTTPException(status_code=422)
        return r


if __name__ == '__main__':
    from uvicorn import run
    run(app, host="0.0.0.0", port=80)
