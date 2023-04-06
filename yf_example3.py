import os
import toolkit_config as cfg
import yf_example2

# Download Qantas stock price
def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR, 'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic=tic, start=start, end=end, pth=pth)

if __name__ == "__main__":
    qan_prc_to_csv(year=2020)







import os
import toolkit_config as cfg
import yf_example2

# Download Qantas stock price
def qan_prc_to_csv(year):
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    tic='QAN.AX'
    pth = os.path.join(cfg.DATADIR, 'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic, pth, start=start, end=end)

if __name__ == "__main__":
    qan_prc_to_csv(2020)