
# net_traffic_stats

net_traffic_stats is a python tool which read and analyze Wireshark netscan dump file.  
net_traffic_stats counts the numbers of package each host sent and recieved and lists first 5 result in graphic mode.


# install python-pcapng package

pip install python-pcapng

[source](https://github.com/rshk/python-pcapng)



# How to run it   
  python net_traffic_stats.py \[file name\]
  
  for example:
  run commond line, user will see a graphic result.
  python net_traffic_stats.py dump.pcapng 
  
  ![graphic result](http://www.99sns.com/net_traffic_stats.png)
  
  # Reference of source
  1. how to read and analyze Wireshark file: https://github.com/rshk/python-pcapng/tree/master/examples 
  2. how to draw bars: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html 
  
  
