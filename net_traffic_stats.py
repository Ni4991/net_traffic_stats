#!/usr/bin/env python
#title           :net_traffic_stats.py
#description     :analyze package data from WireShark and draw bars view.
#author          :yousong zhang
#date            :20180321
#version         :1.0
#usage           :python net_traffic_stats.py dump.pcapng
#python_version  :2.7.12
#reference source:
#1. how to read and analyze Wireshark file: https://github.com/rshk/python-pcapng/tree/master/examples
#2. how to draw bars: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html



from __future__ import print_function, division

from collections import Counter

from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP

from pcapng import FileScanner
from pcapng.blocks import EnhancedPacket

import sys





if __name__ == '__main__':
    fp = open(sys.argv[1], 'rb')
    rdr = FileScanner(fp)

    ip_src_count = Counter()
    ip_dst_count = Counter()
    ip_src_size = Counter()
    ip_dst_size = Counter()

    tcp_src_count = Counter()
    tcp_dst_count = Counter()
    tcp_src_size = Counter()
    tcp_dst_size = Counter()

    for block in rdr:
        # print(repr(block))

        if isinstance(block, EnhancedPacket):
            #assert block.interface.link_type == 1  # must be ethernet!

            decoded = Ether(block.packet_data)
            # print(repr(Ether(block.packet_data))[:400] + '...')

            _pl1 = decoded.payload
            if isinstance(_pl1, IP):
                ip_src_count[_pl1.src] += 1
                ip_dst_count[_pl1.dst] += 1


                _pl2 = _pl1.payload
                if isinstance(_pl2, TCP):
                    _src = '{0}:{1}'.format(_pl1.dst, _pl2.dport)
                    _dst = '{0}:{1}'.format(_pl1.src, _pl2.sport)
                    tcp_src_count[_src] += 1
                    tcp_dst_count[_dst] += 1
    # def _rsic(o):
    #     return sorted(o.iteritems(), key=lambda x: x[1], reverse=True)

    _rsic = lambda o: sorted(o.iteritems(), key=lambda x: x[1], reverse=True)

    import matplotlib.pyplot as plt

    size = 5
    x1 = range(size)
    x2 = range(size)
    y1 = []
    y2 = []
    label1 = []
    label2 = []

    for key, val in _rsic(ip_src_count)[:size]:
        y1.append(val)
        label1.append(key)

    for key, val in _rsic(ip_src_count)[:size]:
        y2.append(val)
        label2.append(key)


    ax = plt.subplot(2, 1, 1)
    plt.title('TCP Traffic by Packet Count')
    ax.bar(x1, y1, label="Sources")
    plt.xticks(x1, label1)

    plt.ylabel('IP Sources')

    bx = plt.subplot(2, 1, 2)

    bx.bar(x2, y2, color='g')
    plt.xticks(x2, label2)

    plt.ylabel('IP Destinations')

    plt.show()
