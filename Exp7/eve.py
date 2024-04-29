import socket
s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)

print("Server is listening, waiting for Alice and Bob")

c1, addr1 = s.accept()  #Alice
print("ALice is connected")

c2, addr2 = s.accept() #Bob 
print("Bob is connected")

p = 29 #prime number
a = 2  #primitive root

                                            #2.Selecting false key for Bob and sending
ya = int(c1.recv(1024).decode()) 

#Xd1 is the private key of the hacker
xd1 = int(input("Enter false key for Bob:"))
yd1 = pow(a, xd1, p)  #public key to be sent to Bob
print(f"Public key for Bob: {yd1}")
c2.send(str(yd1).encode())
print("Sent public key Bob")

                                            
#receive the public key of Bob .... done after all the work at Bob's end
yb = int(c2.recv(1024).decode()) 

                                            #5. Selecting the public key to be sent to the Alice

#Xd2 is used to calculate the public key for Alice
xd2 = int(input("Enter false key for Alice:"))
yd2 = pow(a, xd2, p)  
print(f"Public key for Alice: {yd2}")

                                            #6. Calculate the secret key of Bob and Alice
#Secret key of Bob 
kbob = pow(yb,xd1,29) # same as k1 calculated at Bob's end
print(f"Key of Bob calculated by Hacker(Darth):{kbob}")

#Secret key of ALice
kalice = pow(ya,xd2,29) #same as k2 calculated at Alice's end
print(f"Key of Alice calculated by Hacker(Darth):{kalice}")

c1.send(str(yd2).encode()) #Sent to the Alice
print("Sent public key for Alice to client 2")
c1.close()
c2.close()
s.close()
