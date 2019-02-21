import readConfig;
class demo:
    rc = readConfig.RedaConfig()
    print(rc.get_db("host"))
