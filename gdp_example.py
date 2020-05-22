import wbdata 
import pandas
import matplotlib.pyplot as plt
 
#set up the countries I want
countries = ["IN","CHN","USA"]
 
#set up the indicator I want (just build up the dict if you want more than one)
indicators = {'NY.GDP.PCAP.KD.ZG':'GDP per capita'}
#'NY.GDP.PCAP.PP.CD':'GDP per capita',

#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False, keep_levels=False)

dfu = df.unstack(level=0)

dfu.plot()
plt.legend(loc='best')

plt.title("GDP per capita, PPP annual growth (%)")
plt.xlabel('Year')
plt.ylabel('Statistics')

plt.show()


# s = wbdata.get_source(12)  ## for getting source
# s = wbdata.get_indicator(source=12)
# s = wbdata.search_countries("IN")
#s = wbdata.get_data("IC.BUS.EASE.XQ", country='USA')
#print(s)