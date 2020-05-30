# TradeLog-Tradervue Timezone Converter

## Introduction 

This is a terribly written Python script I created to help me solve a problem I had exporting trades from Interactive Brokers for importing into Tradervue.

I am not a coder, so it is extremely messy and I guarantee there are many easier ways to accomplish the same thing.

## Background of the problem

I am located in Australia and daytrading the US financial markets using Interactive Brokers. I like to journal my trades using Tradervue to track my progress and gain insight into my behavior in the hopes to gradually improve my statistics. 

Interactive Brokers allows the export of trading activity to a 'TradeLog' format and luckily Tradervue accepts this as an import option.

## What is the problem?

When exporting trades from Interactive Brokers as a TradeLog file , it generates a TLG file that results in all the trades using the local timezone of the broker (Interactive Brokers - Sydney, Australia). 

Not only is this annoying because my timezone is 30 minutes behind Sydney, but also because I am trading the US markets which is 14 HOURS behind what the TLG file is showing. I need the TradeLog file to show accurate times in the EST timezone (New York) so when I import it into Tradervue, it is easy to track the relationship between my performance and the period of time in the trading session. The mini-charts on Tradervue were also messed up due to the inaccurate timezone.

## What is the solution?

I needed a way to automate the conversion of a TradeLog file from one timezone to another and generate an accurate output that could be imported into Tradervue.

So I frankenstein-ed a Python script that would convert the timezones, grab the input that was exported manually from Interactive Brokers and replace the inaccurate Date-Time-Group (DTG) with the new one so it could be imported into Tradervue.

Sounds easy? Well there were a few challenges and a few different versions BUT here we are..

**BONUS:** It should handle conversion between daylight savings timezones fine also

## Requirements

- Python 3+
- Python datetime module
- Python os module
- Python pytz module
- Python pandas module
- An exported TradeLog (TLG) file

## How to use it?

### Exporting and Converting:
- Login to the Interactive Brokers Activity Statement dashboard 
- Click on TradeLog under the Third Party Downloads section
- Select the time period of your trades and click the Run button
- Save the TradeLog file to the SAME LOCATION as this Python script
- Download TradeLog-Tradervue-TimezoneConvert.py and requirements.txt
- Execute 'pip install -r requirements.txt'
- Execute the TradeLog-Tradervue-TimezoneConvert.py script
- You will be prompted to type the name of the city you want to convert the time to (New York, in my example earlier)
- You will then be prompted to type the name of the city you want to convert the time from (Sydney, in my example earlier)
- You will be prompted to type the file name of the INPUT file (TLG file exported from broker)
- You will be prompted to type the file name of the OUTPUT file
- If everything goes smoothly, you will be left with an accurate output file in the same path

### Importing into Tradervue:
- Login to Tradervue
- Click Import Trades at the top of the page
- Select 'Interactive Brokers' from the broker/trading platform list
- Click 'Choose file' and browse to the output file the script created
- Click Upload
- PROFIT!

## Troubleshooting

Come on.. it ain't that hard.

Just follow the directions and prompts the script gives you.

If it don't work, fix it yourself.
