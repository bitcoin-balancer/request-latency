from typing import Literal, TypedDict

# supported exchange IDs
IExchangeID = Literal['binance', 'bitfinex', 'kraken']

# the data that will be entered by the user
class IScriptInput(TypedDict):
  exchange: IExchangeID
  api_key: str
  api_secret: str