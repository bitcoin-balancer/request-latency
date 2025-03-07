from requests import get
from .tester import Tester

class BitfinexTester(Tester):
  """
  """

  def __init__(self, api_key: str, api_secret: str):
    super().__init__(api_key, api_secret)


  def __public_request(self) -> None:
    """Executes a public request to the exchange.
    """
    raise NotImplementedError('The public request has not yet been implemented.')


  def __private_request(self) -> None:
    """Executes a private request to the exchange.
    """
    raise NotImplementedError('The public request has not yet been implemented.')