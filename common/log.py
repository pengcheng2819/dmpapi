import logging
import os
from datetime import datetime
import threading
import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # 如果结果路径不存在，则创建目录
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # 日志文件根据时间创建
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # 如果日志文件不存在则创建文件
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # 实例化日志类
        self.logger = logging.getLogger()
        # 定义日志等级
        self.logger.setLevel(logging.INFO)

        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)

class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log