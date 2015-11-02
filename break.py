f = open('D:/Python/user.txt')
f_list = f.readlines()
f.close()

while True:
    username = input('username:').strip()
    password = input('password:').strip()
    if len(username) != 0 and len(password) != 0:
        flag = False
        for line in f_list:
            line = line.split()
            if username == line[0] and password == line[1]:
                print('Welcome %s to login system' % line[0])
                flag = True
                break
        if flag:
            break