with open("/var/log/auth.log", mode = 'r', encoding='UTF-8') as f:
    logs = f.read()
    print(logs)