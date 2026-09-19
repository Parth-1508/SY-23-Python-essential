coded_msg = input ("Enter your coded message:")
secret_msg = input ("Enter your secret message to look for:")
if secret_msg in coded_msg:
	print("Decoder:Your Secret message is included")
else:
	print("Decoder:No Secret Message Found")