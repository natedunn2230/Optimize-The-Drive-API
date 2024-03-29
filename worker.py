import config
import redis
from app import app
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = config.REDIS_URL

conn = redis.from_url(redis_url)
queue = Queue(connection=conn)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()