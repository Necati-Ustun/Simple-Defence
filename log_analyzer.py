import scapy.all as scapy


def read_pcap():
    packetReader = scapy
    packetList = packetReader.rdpcap("test.pcapng")  # Okunacak olan dosya
    for i in range(len(packetList)):
        t = packetList[i].show()
        print(t)
