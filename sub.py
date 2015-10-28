# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code', r)
import subprocess
# subprocess.Popen(["notepad.exe", "abc.txt"])
# subprocess.Popen('notepad.exe abc.txt')
# subprocess.Popen('vim test.txt')
# subprocess.Popen(['vim', 'test.txt'])
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'server 114.114.114.114\nexit\n')
print(output.decode('utf-8'))
print('Exit code', p.returncode)