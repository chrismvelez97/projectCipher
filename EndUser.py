import cipherFunctions as cipher
'''This is the old way it was done but now
    we wrapped our statements into a cipherFunctions
    and then used a while loop to have the
    program continue to hash different messages
    until the command "exit" is entered.'''

# message = input("Enter message here:\n")
#
# numList = cipher.messageToNumber(message)
#
# shift = cipher.shiftNumbers(numList)
#
# encryption = cipher.checkOutOfBounds(shift)
#
# encryption = cipher.shiftAsEncryption(encryption)
#
#
# print("Your encrypted message is:\n{}".format(encryption))
#
message = input("Enter message here:\n")
while message != "exit":
    cipher.displayCipher(message)
    message = input("Enter message here:\n")
