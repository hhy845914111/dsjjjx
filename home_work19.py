import pandas as pd

def cal(dfobject):
    tp1 = dfobject["esp"].values
    tp2 = dfobject["totals"].values

    tp1.shape = (len(tp1), 1)
    tp2.shape = (len(tp2), 1)

    tp1 = tp1.transpose()

    return float(tp1.dot(tp2))
    
df_all = pd.read_csv("../china_stockA.csv", encoding='gbk')[["industry", "esp", "totals"]]
df_bank = df_all[df_all["industry"] == u"银行"]

print cal(df_bank) / cal(df_all)

#Good luck to your final!
#By Rex Hoo
