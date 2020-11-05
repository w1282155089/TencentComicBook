
# crawler 缓存时间
CACHE_TIME = 600

# 线程池大小
POOL_SIZE = 8

# 防止任务重复创建 同样的任务 10min 内只能创建一次
TASK_AVOID_REPEAT_TIME = 10 * 60

TIME_ZONE = "Asia/Shanghai"


class ConfigKey():
    MANAGE_SECRET = 'MANAGE_SECRET'
    COOKIES_DIR = 'COOKIES_DIR'
    SQLITE_FILE = 'SQLITE_FILE'
    LOG_LEVEL = 'LOG_LEVEL'
    URL_PREFIX = 'URL_PREFIX'
    CRAWLER_PROXY = 'CRAWLER_PROXY'
