#importando 

import speedtest
def main():
    st = speedtest.Speedtest() 
    print(f"{'{:.2f}'.format(st.download()/1024/1024)}")
    print(f"{'{:.2f}'.format(st.upload()/1024/1024)}")

