from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib
import matplotlib.pyplot as plt

#Class for Examples of Plotting Technical Indicators from Alpha Vantage

#Size of charts
matplotlib.rcParams['figure.figsize'] = (15, 10)

#Plotting Bollinger Bands MSFT
ti = TechIndicators(key='YOUR_KEY', output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='1min',)
data.plot()
plt.title('Bollinger Bands for  $MSFT: 1 min)')
plt.show()

#Plotting RSI MSFT
ti = TechIndicators(key='YOUR_KEY', output_format='pandas')
data, meta_data = ti.get_rsi(symbol='MSFT', interval='1min',)
data.plot()
plt.title('Relative Strength Index (RSI) for  $MSFT: 1 min)')
plt.show()

#Plotting OBV MSFT
ti = TechIndicators(key='YOUR_KEY', output_format='pandas')
data, meta_data = ti.get_obv(symbol='MSFT', interval='1min',)
data.plot()
plt.title('Relative Strength Index (OBV) for  $MSFT: 1 min)')
plt.show()

#Plotting Average Directional Movement Index MSFT
ti = TechIndicators(key='YOUR_KEY', output_format='pandas')
data, meta_data = ti.get_adx(symbol='MSFT', interval='1min',)
data.plot()
plt.title('Average Directional Movement Index (ADX) for  $MSFT: 1 min)')
plt.show()

#Plotting Stochoastic Oscillator MSFT
ti = TechIndicators(key='YOUR_KEY', output_format='pandas')
data, meta_data = ti.get_stoch(symbol='MSFT', interval='1min',)
data.plot()
plt.title('Stochoastic Oscillator (STOCH) for  $MSFT: 1 min)')
plt.show()

#Plotting Simple Moving Average MSFT
ti = TechIndicators(key='YOUR_KEY', output_format='pandas')
data, meta_data = ti.get_sma(symbol='MSFT', interval='1min',)
data.plot()
plt.title('Simple Moving Average (SMA) for  $MSFT: 1 min)')
plt.show()
