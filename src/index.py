from inquirer import prompt, List, Text
from shared import EXCHANGES, IScriptInput
from validations import validate_input
from tester import get_tester

# prompt the user to input the required data
answers: IScriptInput = prompt([
  List('exchange', message='Select an exchange', choices=EXCHANGES),
  Text('api_key', message='Enter your API Secret'),
  Text('api_secret', message='Enter your API Secret'),
])

# validate the input
validate_input(answers)

# instantiate the tester
tester = get_tester(answers)

# run the test and output the results
tester.run()