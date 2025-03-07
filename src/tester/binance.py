from requests import get
from .tester import Tester

class BinanceTester(Tester):
  """
  """

  def __init__(self, api_key: str, api_secret: str):
    super().__init__(api_key, api_secret)


  def __public_request(self) -> None:
    """Executes a public request to the exchange.
    """
    res = get('https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=128')
    if res.status_code != 200:
      raise ValueError('Failed to execute public request.')