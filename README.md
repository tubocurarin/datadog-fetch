# datadog-fetch

Fetch metric data from Datadog!

## Usage

I recommend the usage of `pipenv`, so everything stays easily in a virtualenv.

1. Install dependencies via `pipenv install`.
2. Run `pipenv run fetch`

## Help

From `./fetch --help`:

```
usage: fetch [-h] [--period PERIOD] [--out OUT] query

Fetches metric data from Datadog. To run this script, two environment
variables are required: DATADOG_API_KEY and DATADOG_APP_KEY. See
https://app.datadoghq.com/account/settings#api on how to obtain them.

positional arguments:
  query            Metric query to fetch data from.

optional arguments:
  -h, --help       show this help message and exit
  --period PERIOD  Time period over which you want to fetch data (in seconds).
                   (default: 3600)
  --out OUT        File name to store data to. Displays to terminal by
                   default.
```
