# 导入Python内置的logging模块
import logging

# 配置日志记录以同时输出到文件和控制台
logging.basicConfig(
    level=logging.INFO,  # 设置日志记录级别为INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 定义日志输出格式
    handlers=[
        logging.FileHandler("app.log"),  # 将日志信息记录到app.log文件
        logging.StreamHandler()  # 同时将日志信息输出到控制台
    ]
)

# 创建一个特定于此模块的日志记录器实例
logger = logging.getLogger(__name__)