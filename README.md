
#net_traffic_stats

net_traffic_stats is a python tool which read and analyze Wireshark netscan dump file.

Detail:
net_traffic_stats counts the numbers of package each host sent and recieved and lists first 5 resulti in graphic mode.


# how to install

sudo -H pip install -r requirements.txt 



# How to run it   
  python net_traffic_stats.py \[file name\]
  
  for example:
  run commond line, user will see a graphic result.
  python net_traffic_stats.py dump.pcapng 
  
  ![graphic result](http://www.99sns.com/net_traffic_stats.png)
  
  
