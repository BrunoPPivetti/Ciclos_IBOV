from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5
 
# conecte-se ao MetaTrader 5
path_to_terminal = "C:\\Program Files\\Genial Investimentos MetaTrader 5\\terminal64.exe"

if not mt5.initialize(path=path_to_terminal):
    print("Erro ao inicializar o MT5")
    quit()

account = 1315621
password = "060221Bb!"
server = "GenialInvestimentos-PRD"

if mt5.login(account, password, server):
    print(f"Login realizado com sucesso na conta {1315621}")
else:
    print("Erro ao fazer login")
 
# consultamos o estado e os parâmetros de conexão
print(mt5.terminal_info())
# obtemos informações sobre a versão do MetaTrader 5
print(mt5.version())
 
symbol = "IBOV"
symbol2 = "VALE3"
timeframe = mt5.TIMEFRAME_D1

ibov_rates = mt5.copy_rates_range(symbol, timeframe, datetime(2015,1,3), datetime(2024,12,30))
vale_rates = mt5.copy_rates_range(symbol2, timeframe, datetime(2015,1,3), datetime(2024,12,30))

# concluímos a conexão ao MetaTrader 5
mt5.shutdown()
 
#PLOT
# a partir dos dados recebidos criamos o DataFrame
ibov_frame = pd.DataFrame(ibov_rates)
vale_frame = pd.DataFrame(vale_rates)

# transformando timestamp em datas legíveis 
ibov_frame['time'] = pd.to_datetime(ibov_frame['time'], unit ='s')
vale_frame['time'] = pd.to_datetime(vale_frame['time'], unit='s')

#filtrando apenas a coluna de fechamento
ibov_close = ibov_frame[['time','close']]
vale_close = vale_frame[['time','close']]

#plotando dados de fechamento
#plt.figure(figsize= (15,7))
#plt.plot(ibov_close['time'], ibov_close['close'], label='IBOV', color= 'b')
#plt.plot(vale_close['time'], vale_close['close'], label = 'VALE3', color ='r')
#plt.title('IBOVESPA/VALE - FECHAMENTOS DIÁRIOS')
#plt.xlabel('Data')
#plt.ylabel('Fechamento')
#plt.legend(loc='upper left')
#plt.grid(True)
#plt.show()

fig, ax1 = plt.subplots(figsize=(15, 7))

# Plotando IBOV no primeiro eixo Y
ax1.plot(ibov_close['time'], ibov_close['close'], label='IBOV', color='b')
ax1.set_xlabel('Data')
ax1.set_ylabel('Fechamento IBOV', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Criando um segundo eixo Y para VALE3
ax2 = ax1.twinx()
ax2.plot(vale_close['time'], vale_close['close'], label='VALE3', color='r')
ax2.set_ylabel('Fechamento VALE3', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Adicionando título e legenda
plt.title('Comparativo IBOV x VALE3 - Fechamentos Diários')
fig.tight_layout()  # Ajuste para evitar sobreposição de labels

# Exibindo o gráfico
plt.show()