from shared import IExchangeID, EXCHANGES, IScriptInput

def __validate_exchange(id: IExchangeID) -> None:
    if id not in EXCHANGES:
        raise ValueError('Please select a valid exchange')

def __validate_api_key(api_key: str) -> None:
    """Validates the entered API Key.
    Args:
      api_key (str): The API Key to validate.
    Raises:
      ValueError: If the API Key is not a string or is empty
    """
    if not isinstance(api_key, str) or len(api_key) == 0:
        raise ValueError('Please enter a valid API Key')
    
def __validate_api_secret(api_secret: str) -> None:
    """Validates the entered API Secret.
    Args:
      api_secret (str): The API Key to validate.
    Raises:
      ValueError: If the API Secret is not a string or is empty
    """
    if not isinstance(api_secret, str) or len(api_secret) == 0:
        raise ValueError('Please enter a valid API Secret')
    
def validate_input(input: IScriptInput) -> None:
    """Validates the input dict to ensure the data passed by the user is valid.
    Args:
      input (IScriptInput): The input data to validate.
    Raises:
      ValueError: If the input data is invalid.
    """
    __validate_exchange(input['exchange'])
    __validate_api_key(input['api_key'])
    __validate_api_secret(input['api_secret'])