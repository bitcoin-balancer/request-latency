from requests import get
from .tester import Tester

class BinanceTester(Tester):
  """BinanceTester Class

  This class is responsible for testing the Binance exchange.
  """

  def __init__(self, api_key: str, api_secret: str):
    super().__init__(api_key, api_secret)



  def _execute_public_request(self) -> None:
    """Executes a public request to the exchange.
    """
    res = get('https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=128')
    if res.status_code != 200:
      raise ValueError('Failed to execute the public request.')



  def _execute_private_request(self) -> None:
    """Executes a private request to the exchange.
    """
    res = get('https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=128')
    if res.status_code != 200:
      raise ValueError('Failed to execute the private request.')