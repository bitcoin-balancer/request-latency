# Request Latency

The `request-latency` script is designed to optimize the performance of the Balancer trading platform by identifying the geographically closest deployment region to the exchange. It accomplishes this by:

- **Measuring Network Latency:** the script sends automated HTTP requests to the exchange platform and records the round-trip time for each request.

- **Comparative Analysis:** it aggregates and compares the latency data from multiple regions to determine which one offers the fastest response times.

- **Optimized Deployment:** by identifying the region with the lowest latency, the script enables administrators to deploy services in the region that minimizes delay, thereby enhancing trading efficiency and reducing order execution time.

This script is an essential tool for ensuring that your automated Bitcoin trading on Balancer is as responsive and efficient as possible.



<br/>

## Results

### Binance

| Region        | Public Req. Mean | Private Req. Mean |
| ------------- | ---------------- | ----------------- |
| New York      | N/A              | N/A               |
| San Francisco | N/A              | N/A               |
| Amsterdan     | 1.82s           | 0.23s            |
| **Singapore**     | **0.28s**           | **0.08s**            |
| London        | 0.99s           | 0.26s            |
| Frankfurt     | 1.02s           | 0.24s            |
| Toronto       | 0.61s           | 0.16s            |
| Bangalore     | 0.43s           | 0.19s            |
| Sydney        | 0.64s           | 0.11s            |

[View test details](./results/binance.md)



### Bitfinex

| Region        | Public Req. Mean | Private Req. Mean |
| ------------- | ---------------- | ----------------- |
| New York      | 0.00s           | 0.00s            |
| San Francisco | 0.00s           | 0.00s            |
| Amsterdan     | 0.00s           | 0.00s            |
| Singapore     | 0.00s           | 0.00s            |
| London        | 0.00s           | 0.00s            |
| Frankfurt     | 0.00s           | 0.00s            |
| Toronto       | 0.00s           | 0.00s            |
| Bangalore     | 0.00s           | 0.00s            |
| Sydney        | 0.00s           | 0.00s            |

[View test details](./results/bitfinex.md)



### Kraken

| Region        | Public Req. Mean | Private Req. Mean |
| ------------- | ---------------- | ----------------- |
| New York      | 0.00s           | 0.00s            |
| San Francisco | 0.00s           | 0.00s            |
| Amsterdan     | 0.00s           | 0.00s            |
| Singapore     | 0.00s           | 0.00s            |
| London        | 0.00s           | 0.00s            |
| Frankfurt     | 0.00s           | 0.00s            |
| Toronto       | 0.00s           | 0.00s            |
| Bangalore     | 0.00s           | 0.00s            |
| Sydney        | 0.00s           | 0.00s            |

[View test details](./results/kraken.md)





<br/>

## Getting Started

1. Download the [`python3-venv`](https://docs.python.org/3/tutorial/venv.html) package:

   ```bash
   sudo apt install python3.12-venv
   ```


2. Download the script:

   ```bash
   git clone https://github.com/bitcoin-balancer/request-latency.git
   ```

3. Navigate to the script's directory:

   ```bash
   cd request-latency
   ```

4. Create and activate the virtual environment:

   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```

5. Ensure the virtual environment has been created and that you're making use of its binaries:

   ```bash
   which python3
   # /home/.../balancer/request-latency/.venv/bin/python3
   ```


6. Install the dependencies with [pip](https://pypi.org/project/pip/):

   ```bash
   pip3 install -r requirements.txt
   ```

7. Execute it by running:

   ```bash
   python3 src/index.py
   ```

8. Once the script has been started, it will ask you to pick an **exchange** and to input the **API Key** and the **API Secret** before running the tests.





<br/>

## License

[Apache v2.0](https://www.apache.org/licenses/LICENSE-2.0)