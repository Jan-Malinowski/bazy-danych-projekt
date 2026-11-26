import csv
import random
from datetime import datetime
from decimal import Decimal
from pathlib import Path


COMPANY_NAMES = {
    "NVDA": "NVIDIA Corporation",
    "ANT": "Anthropic, PBC",
    "SPCX": "Space Exploration Technologies Corp. (SpaceX)",
    "INTC": "Intel Corporation",
    "SNDK": "Sandisk Corporation",
    "PLUG": "Plug Power Inc.",
    "GRAB": "Grab Holdings Limited",
    "RIG": "Transocean Ltd.",
    "IREN": "IREN Limited",
    "CRWV": "CoreWeave, Inc.",
    "INSM": "Insmed Incorporated",
    "NOK": "Nokia Oyj",
    "VALE": "Vale S.A.",
    "AAL": "American Airlines Group Inc.",
    "STLA": "Stellantis N.V.",
    "AMZN": "Amazon.com, Inc.",
    "WULF": "TeraWulf Inc.",
    "AAPL": "Apple Inc.",
    "MU": "Micron Technology, Inc.",
    "BMNR": "Bitmine Immersion Technologies",
    "F": "Ford Motor Company",
    "AMD": "Advanced Micro Devices, Inc.",
    "HL": "Hecla Mining Company",
    "GOOGL": "Alphabet Inc. (Klasa A)",
    "NBIS": "Nebius Group N.V.",
    "ORCL": "Oracle Corporation",
    "TSLA": "Tesla, Inc.",
    "AVGO": "Broadcom Inc.",
    "MRVL": "Marvell Technology, Inc.",
    "MSFT": "Microsoft Corporation",
    "DELL": "Dell Technologies Inc.",
    "WMT": "Walmart Inc.",
    "XOM": "ExxonMobil Corporation",
    "LRCX": "Lam Research Corporation",
    "PLTR": "Palantir Technologies Inc.",
    "META": "Meta Platforms, Inc.",
    "NFLX": "Netflix, Inc.",
    "AMAT": "Applied Materials, Inc.",
    "MSTR": "Strategy (MicroStrategy)",
    "KO": "The Coca-Cola Company",
    "ADI": "Analog Devices, Inc.",
    "PYPL": "PayPal Holdings, Inc.",
    "PFE": "Pfizer Inc.",
    "NIO": "NIO Inc.",
    "BABA": "Alibaba Group Holding",
    "O": "Realty Income Corporation",
    "DIS": "The Walt Disney Company",
    "GEV": "GE Vernova Inc.",
    "V": "Visa Inc.",
    "LLY": "Eli Lilly and Company",
}


def main():
    data_dir = Path(__file__).resolve().parent.parent / "Data"
    history_path = data_dir / "History.csv"
    stocks_path = data_dir / "Stocks.csv"

    latest_prices = {}
    with history_path.open(mode="r", newline="", encoding="utf-8") as history_file:
        reader = csv.DictReader(history_file)
        for row in reader:
            ticker = row["ticker"].strip().upper()
            price_date = datetime.strptime(row["price_date"], "%m/%d/%Y")
            price = Decimal(row["price"])

            if ticker not in COMPANY_NAMES:
                raise ValueError("Brak nazwy firmy dla tickera: {}".format(ticker))

            current = latest_prices.get(ticker)
            if current is None or price_date >= current[0]:
                latest_prices[ticker] = (price_date, price)

    with stocks_path.open(mode="w", newline="", encoding="utf-8") as stocks_file:
        writer = csv.writer(stocks_file)
        writer.writerow(["ticker", "comp_name", "curr_price", "amm"])

        for ticker, (_, price) in latest_prices.items():
            writer.writerow(
                [
                    ticker,
                    COMPANY_NAMES[ticker],
                    format(price, ".2f"),
                    random.randint(0, 1000),
                ]
            )


if __name__ == "__main__":
    main()

