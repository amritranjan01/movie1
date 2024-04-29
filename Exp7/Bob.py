import socket
port = 12345
client_socket = socket.socket()
client_socket.connect(('localhost', port))

                                            #<3 Generating public key of Bob and sending it to Alice (which would be intruded)>
yd1 = int(client_socket.recv(1024).decode())
print("Received public key for Bob:", yd1)
xb = int(input("Enter private key of Bob:"))
yb = pow(2,xb,29) #Public Key of BOB
print(f"Public key of Bob is: {yb}")

                                            #4. Calculating the secret key
k1 = pow(yd1,xb,29)
print(f"Secret key decrypted by Bob: {k1}")
client_socket.send(str(yb).encode())  
client_socket.close()
