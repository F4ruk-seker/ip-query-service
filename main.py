from fastapi import FastAPI, Request
from program import query
from program.database import save_query, get_ip_from_id


app = FastAPI()

try:
    SERVER_IP = query.get_ip_data('').get('host')
except:
    pass

@app.get("/")
async def question_client_ip(request: Request):
    client_ip = request.client.host
    result = query.get_ip_data(client_ip)
    result['client_ip'] = client_ip
    result = save_query(result)
    if SERVER_IP != client_ip and SERVER_IP != result.get('host'):
        result.pop('client_ip')
        return result


@app.get("/{ip:str}")
async def question_ip(ip: str, request: Request):
    client_ip = request.client.host

    result = query.get_ip_data(ip)
    result['client_ip'] = client_ip
    result = save_query(result)

    if SERVER_IP != ip and SERVER_IP != result.get('host'):
        result.pop('client_ip')
        return result


@app.get('/id/{id}')
async def get_questioned_thread(id):
    return  get_ip_from_id(id)