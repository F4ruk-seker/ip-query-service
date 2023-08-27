import os
from model import ApiHostModel


_ = os.environ.get('API_QUERY')
API_QUERY_HOST = ApiHostModel(_)
API_QUERY_PATH = os.environ.get('API_QUERY_PATH')





