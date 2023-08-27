from fastapi import FastAPI, Request
from fastapi import Depends, Header

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
    if _ := request.headers.get("X-Forwarded-For"):
        client_ip = _

    if len(client_ip) > 1 and type(client_ip) is list:
        client_ip = client_ip[0]

    if len(client_ip.split(',')) > 1:
        client_ip = client_ip[0]

    result = query.get_ip_data(client_ip)
    result['client_ip'] = client_ip
    result = save_query(result)

    if SERVER_IP != client_ip and SERVER_IP != result.get('host'):
        result.pop('client_ip')
        return result


@app.get("/{ip:str}")
async def question_ip(ip: str, request: Request):
    result = query.get_ip_data(ip)
    result['client_ip'] = request.client.host
    if _ := request.headers.get("X-Forwarded-For"):
        result['client_ip'] = _

    if len(result['client_ip']) > 1 and type(result['client_ip']) is list:
        result['client_ip'] = result['client_ip'][0]

    if len(result['client_ip'].split(',')) > 1:
        result['client_ip'] = result['client_ip'].split(',')[0]

    result = save_query(result)
    if SERVER_IP != ip and SERVER_IP != result.get('host'):
        result.pop('client_ip')
        return result


@app.get('/id/{id}')
async def get_questioned_thread(id):
    return get_ip_from_id(id)