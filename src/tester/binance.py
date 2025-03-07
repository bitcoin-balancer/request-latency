from typing import Dict
from requests import get, Session
from time import time
import hmac
import hashlib
from .tester import Tester

class BinanceTester(Tester):
  """BinanceTester Class

  This class is responsible for testing the Binance exchange.
  """

  def __init__(self, api_key: str, api_secret: str):
    super().__init__(api_key, api_secret)

  ##################
  # PUBLIC REQUEST #
  ##################

  def _execute_public_request(self) -> None:
    """Sends an HTTP request to a public endpoint.
    """
    res = get('https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=128')
    if res.status_code != 200:
      raise ValueError(f'Failed to execute the public request. The received status code is {res.status_code} ({res.reason})')




  ###################
  # PRIVATE REQUEST #
  ###################

  def __hash_query_string(self, query_string: str) -> str:
    """Hashes the query string that will be added to the endpoint's URL.

    Args:
      query_string: str
        The query string that will be hashed.

    Returns:
      str
    """
    return hmac.new(
        self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256
    ).hexdigest()



  def __get_unix_timestamp(self):
    """Returns the current Unix timestamp in milliseconds.

    Returns:
      int
    """
    return int(time() * 1000)


  def __build_private_endpoint_url(self, query_string: str) -> str:
    """Builds the URL for the private endpoint. It includes the query_string and the signture.
    
    Args:
      query_string: str
        The query string to be added to the URL.

    Returns: str
    """
    return f'https://api.binance.com/api/v3/account?{query_string}&signature={self.__hash_query_string(query_string)}'



  def __build_request_headers(self) -> Dict[str, str]:
    """Builds the headers that will be included on the request.

    Returns:
      dict
    """
    return { "Content-Type": "application/json;charset=utf-8", "X-MBX-APIKEY": self.api_key }



  def _execute_private_request(self) -> None:
    """Sends an HTTP request to a private endpoint.
    """
    # init the query string
    query_string = f'timestamp={self.__get_unix_timestamp()}'

    # init the endpoint's URL
    url = self.__build_private_endpoint_url(query_string)

    # send and validate the request
    session = Session()
    session.headers.update(self.__build_request_headers())
    res = session.get(url)
    if res.status_code != 200:
      raise ValueError(f'Failed to execute the private request. The received status code is {res.status_code} ({res.reason})')