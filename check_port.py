import socket

def check_port(port, host, protocol):

    # UDP
    if protocol == 1:
        trans_prot = socket.SOCK_DGRAM
    # TCP
    elif protocol == 2:
        trans_prot = socket.SOCK_STREAM
    # Bad Number
    else:
        raise Exception("Unsupported Protocol")

    # Creates a socket with a timeout of 0.1 so after 0.1 we go to next port if it doesnt work
    sock = socket.socket(socket.AF_INET, trans_prot)
    sock.settimeout(0.1)
    
    # Try to connect 
    result = sock.connect_ex((host, port))
    sock.close()

    # Tell us if the connection suceeded
    return result == 0

def main():
    for i in range(65535):
        trial1 = check_port(i, "10.144.203.168", 2)#Assigns true or false depending of if the port is open to trial1
        if(trial1 == True):#Prints the open ports
            print str(i)
main()