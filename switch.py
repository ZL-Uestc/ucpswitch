"""
   用一个类表示交换机
   所具有的属性：
   1.名字
   2.所在层级
   3.与对端交换机连接的属性，这个用元组表示 用于扩散主机、安全组 生成静态路由
   从哪些端口学到了哪些主机信息
"""


class switch:
    """
   :param dev_name: 交换机名称.
   :param dev_level: 交换机所属层级.
   :param dev_connection: 交换机连接状态.
   """

    def __init__(self, dev_name, dev_level, dev_connection, dev_host_info):
      self.name = dev_name
      self.level = dev_level
      self.connection = dev_connection
      self.host_info = dev_host_info


"""
   # 连接类，描述
   # 暂不用类来描述连接 使用元组表示
"""


class portconnection:
    pass
