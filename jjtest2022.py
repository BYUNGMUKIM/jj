import time
import pyupbit
import datetime

access = "F3c4LD0DaKdxkU2spiORY1rRKQQH7drO8eybjHqD"          # 본인 값으로 변경
secret = "PvzT2Kl4XF8UBHdMnLAjOUO01ViJ2mZTVASZc1LU"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


accesss = "MKj7qSJev41IXCCf5GJBG084WT0s3Zv1uxuaZFk3"          # 본인 값으로 변경
secrett = "WcqjzhcfYTUv4tOaDesi6skG82nxXu3y99Hk3nqf"          # 본인 값으로 변경
upbitt = pyupbit.Upbit(accesss, secrett)


print(upbit.get_balance("KRW"))
print(upbit.get_balance("XRP"))
print(upbitt.get_balance("ETH"))
print(pyupbit.get_current_price("KRW-XRP"))
print(pyupbit.get_current_price("KRW-XRP") - 10)
print(pyupbit.get_current_price("KRW-ETH"))
print(pyupbit.get_current_price("KRW-ETH") - 30000)

while True:
    try:
        
        if 4900000 < upbit.get_balance("KRW"):            
            current_price = pyupbit.get_current_price("KRW-XRP")
            target_price = pyupbit.get_current_price("KRW-XRP") - 10
            upbit.buy_limit_order("KRW-XRP", target_price, 20000/target_price)
            print("매도",target_price,upbit.get_balance("KRW"))
            print(20000/target_price)
        elif 4720 < upbit.get_balance("XRP"): 
                current_price = pyupbit.get_current_price("KRW-XRP")
                target_price1 = pyupbit.get_current_price("KRW-XRP") + 10
                upbit.sell_limit_order("KRW-XRP",current_price + 10, 20000/current_price)
                print(current_price+10)
                print(20000/current_price)
        elif 2170000 < upbitt.get_balance("KRW"):            
            current_pricee = pyupbit.get_current_price("KRW-ETH")
            target_pricee = pyupbit.get_current_price("KRW-ETH") - 30000
            upbitt.buy_limit_order("KRW-ETH", target_pricee, 60000/target_pricee)
            print(target_pricee,upbitt.get_balance("KRW"))
            print(60000/target_pricee)
        elif 0.012 < upbitt.get_balance("ETH"): 
                current_pricee = pyupbit.get_current_price("KRW-ETH")                
                upbitt.sell_limit_order("KRW-ETH",current_pricee + 30000, 60000/current_pricee)
              
               
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)