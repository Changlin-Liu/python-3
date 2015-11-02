# import re
# test = 'new091'
# if re.match(r'\w+', test):
#     print('OK')
# else:
#     print('faild')
import re
user_account_match = re.compile(r'^[\w\.\-]+@([?:\w+\.\-]+)[a-z]+$|\
     ^0(\d{2,3})(\d{8,9})$|^1[358](\d{9})$')
result = user_account_match.match('jingqi.he@square-enix.net.cn')
print(result.groups())
print(result.group(0))
print(result.group(1))
