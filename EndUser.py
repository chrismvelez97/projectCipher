import cipherFunctions as cipher

message = input("Enter message here:\n")

numList = cipher.messageToNumber(message)

shift = cipher.shiftNumbers(numList)

encryption = cipher.checkOutOfBounds(shift)

encryption = cipher.shiftAsEncryption(encryption)


print("Your encrypted message is:\n{}".format(encryption))
