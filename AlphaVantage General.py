from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib
import matplotlib.pyplot as plt

#Plotting & General Exploring into Alpha Vantage's API

#Size of charts
matplotlib.rcParams['figure.figsize'] = (15, 10)

#Plotting MSFT's returns 60min interval
ts = TimeSeries(key='YOUR_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='60min', outputsize='full')
data['close'].plot()
plt.title('Intraday Times Series for $MSFT: Hourly')
plt.show()

#Plotting SectorPerformances
sp = SectorPerformances(key='YOUR_KEY', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()

#Forex
cc = ForeignExchange(key=os.environ['YOUR_KEY'])
data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
print(data)

#Plotting CryptoCurrency: BitCoin
cc = CryptoCurrencies(key='YOUR_KEY', output_format='pandas')
data, meta_data = cc.get_digital_currency_intraday(symbol='BTC', market='CNY')
data['. price (USD)'].plot()
plt.tight_layout()
plt.title('Intraday value for bitcoin (BTC)')
plt.grid()
plt.show()

#Error with AlphaVantage API not adjusting for splits with $APPL
ts = TimeSeries(key='YOUR_KEY', output_format='pandas')
data, meta_data = ts.get_daily_adjusted(symbol='AAPL', outputsize='full')
data['close'].plot()
plt.title('Daily Adjusted for $AAPL')
plt.show()
