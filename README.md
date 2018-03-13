# DSAI-AutoTrading
An auto trading program for one stock only.
We assume one can hold at most 1 unit, and at most sell short for one unit.
As for the last day, if one hold 1 unit, we'll sell it with close price.
And if one sell short for 1 unit, we'll buy it back with open price.

## Files
### Input
input files should all be csv files
Each line contains four prices:
`open, high, low, close`

### Output
output will be three action, which are:
* `1`: buy one unit
* `0`: no action
* `-1`: sell one unit

## Installation
`$pip install -r requirements.txt`

## Run
```
$python3 trader.py
    --training="training_csv_file"
    --testing="testing_csv_file"
    --output="output_file"
```

## Develop Note
[develop note](https://nbviewer.jupyter.org/github/jkrvivian/DSAI-AutoTrading/blob/master/trader.ipynb)

