# Rate

A simple API template for estimating the MtGox USD<->BTC exchange rate.

## Setup

```sh
$ pip install -r requirements.txt
```

That should be everything you need. Run the runner like so:

```sh
$ python runner.py
```

Now visit [http://localhost:5000/](http://localhost:5000/) in
your browser...

Or use curl:

```sh
$ curl --data "amount=42&type=asks" http://localhost:5000/api/rate
```
