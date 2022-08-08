# WiFi-RSSI-AndroidProject
Android implementation to scan RSSI values of five access points and transfer them to server periodically.

The entire src folder of the Android project is uploaded here. The following changes need to be made before running the application:

Changes to be made in src/main/java/com/example/my/indoorlocl/GetLocRssi.java - 
	In this java file line# 71 and line# 73 - "AP1" is the SSID of WiFi access point used here for experiment. Use SSID of your own access point. Similarly names of "AP2", "AP3", "AP4", and "AP5" need to be modified.
	In line# 100 and line# 101 - in place of "IPV4:port", substitute the respective IP address and port number of your server.
	
IndoorLocserver.py contains the python implementation that uses flask server to receive RSSI values sent by android application. Change IPV4 and port number accordingly. It generates an excel sheet with each row containing the names and RSSI values of five access points. Data in the excel sheet can be processed later to get the required format.
      
