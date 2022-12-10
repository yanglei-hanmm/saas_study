import re

def is_valid_email(str):
	#     someone@gmail.com    bill.gates@microsoft.com
    # /^1[3-9]\d{9}$/
	if re.match(r'^(?![0-9]+$)(?![a-zA-Z_]+$){8,16}$',str):
		print('ok')
	else:
		print('failed')

is_valid_email('aA A$-1_SDe')