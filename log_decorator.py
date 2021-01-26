import logging

# 设置基本配置
logging.basicConfig(level=logging.DEBUG)

# 自定义logger
logger = logging.getLogger('log')

# 定义装饰器
def log_decorator(func):
    """
    给传入的函数天机日志信息
    :param func:传入的函数
    :return:添加了log信息的函数
    """
    def wrapper(*args, **kwargs):
        # 加上log 信息
        logger.debug(f"装饰器：{log_decorator.__name__} - > 传入函数：{func.__name__}")
        # 调用传入的函数对象
        return func(*args, **kwargs)
    return wrapper