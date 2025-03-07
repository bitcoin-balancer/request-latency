from shared import IScriptInput
from binance import BinanceTester
from bitfinex import BitfinexTester
from kraken import KrakenTester


def get_tester(input: IScriptInput) -> BinanceTester | BitfinexTester | KrakenTester:
  """Returns a tester object based on the input data.

  Args:
    input: IScriptInput
      The input data provided by the user.

  Returns:
    BinanceTester | BitfinexTester | KrakenTester
  """
  match input['exchange']:
    case 'binance':
      return BinanceTester(input['api_key'], input['api_secret'])
    case 'bitfinex':
      return BitfinexTester(input['api_key'], input['api_secret'])
    case 'kraken':
      return KrakenTester(input['api_key'], input['api_secret'])
    case _:
      raise ValueError('The chosen exchange has not yet been implemented.')