import socket

def sniff(interface):
    # Create a raw socket
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    # Bind the socket to the specified interface
    sniffer.bind((interface, 0))

    # Set the socket to promiscuous mode
    sniffer.setsockopt(socket.SOL_SOCKET, socket.SO_PROMISCUOUS, 1)

    # Start capturing packets
    while True:
        packet = sniffer.recvfrom(65535)
        print(packet)

if __name__ == "__main__":
    # Get the interface name from the user
    interface = input("Enter the interface name: ")

    # Start sniffing packets
    sniff(interface)
