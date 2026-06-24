from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from src.cache.redis_client import redis_client



class RateLimitMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        

        client_ip = request.client.host
        
        request_count = redis_client.get(client_ip)

        if request_count is None:
            redis_client.set(client_ip, 1, ex=60)
            request_count = 1

        else:
            request_count = redis_client.incr(client_ip)

        if int(request_count) > 5:
            return JSONResponse(
                status_code=429,
                content={'message': 'Too many requests. Please try again later.'}
            )
        

        response = await call_next(request)
        
        return response