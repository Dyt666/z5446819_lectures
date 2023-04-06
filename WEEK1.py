import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')



String1 ='''John said:"Let's learn Python together"'''
print(String1)

f = 0.2 + 0.2 +0.2
print (f)
print(f==0.6) # False if print(f==0.6)


