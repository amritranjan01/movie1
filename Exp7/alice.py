import socket
port = 12345
client_socket = socket.socket()
client_socket.connect(('localhost', port))

                                            # 1. Calculating the public key of Alice and send 
#As per the algorithm it would be the first step  getting Alices public key and sending to Bob which would be intruded by Darth
xa = int(input("Enter the private key for ALice:"))
ya = pow(2,xa,29) #Public key of Alice
client_socket.send(str(ya).encode())


yd2 = int(client_socket.recv(1024).decode()) #received the public key decided by Darth
print("Received public key for Alice:", yd2) 

                                            #7. Calculate the secret key sent by Bob which does not match with Bob
k2 = pow(yd2, xa, 29)
print(f"Secret key decrypted by ALice: {k2}")
client_socket.close()
