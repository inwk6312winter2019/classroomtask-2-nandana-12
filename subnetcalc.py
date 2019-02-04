class subnetcalc():

	def __init__(self,ipaddr = [0,0,0,0],subnet_mask = [0,0,0,0]):
		self.ipaddr = ipaddr
		self.subnet_mask = subnet_mask

	def __str__(self):
		ipformat = ""
		for i in self.ipaddr:
			ipformat = ipformat + str(i) + "."
		return ("The address is : " + ipformat)

myipaddr = subnetcalc([192,168,2,1],[255,255,255,0])
print(myipaddr)
 