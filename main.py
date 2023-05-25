from ui import Window
import sys
from PyQt5.QtWidgets import QApplication
import speedtest
import time
"""
def test_wifi_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1000000 # vitesse de téléchargement en Mbps
    upload_speed = st.upload() / 1000000 # vitesse d'envoi en Mbps

    return (download_speed, upload_speed)

download_speed, upload_speed = test_wifi_speed()
print(f"Vitesse de téléchargement : {download_speed:.2f} Mbps")
print(f"Vitesse d'envoi : {upload_speed:.2f} Mbps")
"""
if __name__=="__main__":
    testWifiApp=QApplication(sys.argv)
    window=Window(320,180,'Test Speed Wifi','.//photo//wifi.png','.//photo//wifibg.png','',True)
    #testHello=window.newLabel(0,0,300,50,'font-size:25px;color:red;','<b>Test Speed Wifi</b>',True)
    vitesseT=window.newLabel(0,50,300,50,'font-size:14px;color:red;','<b>Vitesse de téléchargement : </b>',False)
    vitesseE=window.newLabel(0,80,300,50,'font-size:14px;color:red;','<b>Vitesse d\'envoi : </b>',False)
    vitesseTV=window.newLabel(190,50,150,50,'font-size:18px;color:black;',"",True)
    vitesseEV=window.newLabel(190,80,200,50,'font-size:18px;color:black;',"",True)
    def test_wifi_speed():
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1000000 # vitesse de téléchargement en Mbps
        upload_speed = st.upload() / 1000000 # vitesse d'envoi en Mbps
        vitesseTV.setText(f"{download_speed:.2f} Mbps")
        vitesseEV.setText(f"{upload_speed:.2f} Mbps")
    def refreshF():
        window.close()
        test_wifi_speed()
        window.show()
    refresh=window.newButton(100,130,100,30,'color:black;background-color:pink;font-size:20px;font-family:;','Refresh',refreshF)
    refreshF()
    sys.exit(testWifiApp.exec_())
