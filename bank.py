from pandas_datareader import wb

bank = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'EG','ET' ], start=2005, end=2020)
print(bank)
