import time
def getHostInfo():
    hostinfo = input("请输入主机所在交换机的名称以及主机的IP和安全组信息: ")
    #返回字符串列表
    metadata = hostinfo.split(" ")
    switch_name, hostIP, hostGroup = metadata
    #print(metadata)
    return switch_name, hostIP, hostGroup

if __name__ == "__main__":
    while True:
        switch_name, hostIP, hostGroup = getHostInfo()
        

