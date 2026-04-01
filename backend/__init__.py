def cargo_price_calculator(height, depth, length, weight, kg_price=3500 ,m3_price=3000):
    
    if height <= 0 or depth <= 0 or length <= 0:
        raise ValueError("Hemjee buruu")
    
    if weight <= 0:
        raise ValueError("Jin buruu")
    
    volume = (height * depth * length) / 5000
    chargeable_weight = max(volume, weight)
    
    return chargeable_weight * kg_price


import requests
import pandas as pd
def currency_data(start_date, end_date):
    import requests
    import pandas as pd
    
    url = f"https://www.mongolbank.mn/en/gold-and-silver-price/data?startDate={start_date}&endDate={end_date}"
    response = requests.post(url)
    
    if response.status_code == 200:
        data_json = response.json()
        if data_json.get("success") == True:
            df = pd.DataFrame(data_json["data"])
            
            # ЭНЭ ХЭСГИЙГ АНХААРААРАЙ:
            # 1. 'GOLD_BUY' багана тоо биш текст байгаа тул таслалыг нь арилгана
            # 2. pd.to_numeric ашиглаж тоо руу хөрвүүлнэ. Алдаа гарвал NaN болгоно.
            df["GOLD_BUY"] = df["GOLD_BUY"].astype(str).str.replace(',', '', regex=True)
            df["GOLD_BUY"] = pd.to_numeric(df["GOLD_BUY"], errors='coerce')
            
            # Хоосон (NaN) мөрүүдийг устгах
            df = df.dropna(subset=["GOLD_BUY"])
            
            return df
        else:
            return "Дата олдсонгүй."
    else:
        return f"Холболтын алдаа: {response.status_code}"




