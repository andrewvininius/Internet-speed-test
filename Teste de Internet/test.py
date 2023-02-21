#importando 

import speedtest

st = speedtest.Speedtest()
def main ():
    print(f"{'{:.2f}'.format(st.download()/1024/1024)}")
    print(f"{'{:.2f}'.format(st.upload()/1024/1024)}")