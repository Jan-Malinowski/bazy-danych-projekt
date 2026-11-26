from faker import Faker
import csv

fake = Faker("pl_PL")

amount = 200
tickers=["AAL", "AAPL", "ADI", "AMAT", "AMD", "AMZN", "ANT", "AVGO", "BABA", "BMNR", "CRWV", "DELL", "DIS", "F", "GEV", "GOOGL", "GRAB", "HL", "INSM", "INTC", "IREN", "KO", "LLY", "LRCX", "META", "MRVL", "MSFT", "MSTR", "MU", "NBIS", "NFLX", "NIO", "NOK", "NVDA", "O", "ORCL", "PFE", "PLTR", "PLUG", "PYPL", "RIG", "SNDK", "SPCX", "STLA", "TSLA", "V", "VALE", "WMT", "WULF", "XOM"]
with open('transactions.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['id_trans', 'id_emp', 'id_clt', 'ticker', 'stock_amm', 'trans_type', 'cost', 'trans_time'])

    for i in range(amount):
        id_trans = i+1
        id_emp = fake.random_int(1,50)
        id_clt = fake.random_int(1,100)
        t=fake.random_int(0,len(tickers)-1)
        ticker = tickers[t]
        stock_amm = fake.random_int(1,100)
        trans_type = fake.random_int(0,1)
        cost = 0
        trans_time = fake.date_time_between(start_date="-3d", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
            
        writer.writerow([id_trans,id_emp,id_clt,ticker,stock_amm,trans_type,cost,trans_time])
        