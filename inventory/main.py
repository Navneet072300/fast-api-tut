from fastapi import FastAPI
from redis_om import get_redis_connection

app = FastAPI()

redis = get_redis_connection(
    host="redis-14012.c15.us-east-1-4.ec2.redns.redis-cloud.com",
    port=11844,
    password="kQvN2PVgKy20xteMFwYXPVVEKNapY9rk",
    decode_responses=True
)


@app.get("/")
async def root():
    return {"message": "Hello World"}