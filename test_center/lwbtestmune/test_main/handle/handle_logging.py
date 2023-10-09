import os
from loguru import logger
from datetime import datetime


class ApiAutoLog():
    """
    使用loguru封装日志
    """

    def __new__(cls, *args, **kwargs):
        log_name = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # sink = handle_ini.get_ini_value('log_path') + "{}.log".format(log_name)
        sink = os.path.abspath(os.path.dirname(os.getcwd()) + '/test_center/lwbtestmune/test_main/logs/' + "{}.log".format(log_name))
        level = "DEBUG"
        encoding = "utf-8"
        enqueue = True
        rotation = "500MB"
        retention = "1 week"

        # format建议直接使用默认的格式
        logger.add(sink=sink, level=level, encoding=encoding, enqueue=enqueue, rotation=rotation, retention=retention)

        # 当然也可以自定义format，如下示例
        # logger.add("../log/test_{time}.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {line} | {message}", encoding="utf-8", enqueue=True, rotation="500MB", retention="1 week")

        return logger


log = ApiAutoLog()
if __name__ == '__main__':
    # 打印不同类型的日志
    log.debug("这是一段debug级别日志")
    log.info("这是一段info级别日志")
    log.warning("这是一段warning级别日志")
    log.critical("这是一段critical级别日志")
