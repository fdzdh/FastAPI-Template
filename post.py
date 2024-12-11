# 导入FastAPI的APIRouter类和Pydantic的BaseModel类
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union  # 导入用于类型注解的Union类型

# 从logger_config模块中导入自定义的日志记录器
from logger_config import logger

# 定义数据传输对象（DTO）或模型，用于验证和解析请求体
class Item(BaseModel):
    name: str = '小明'                       # 名称属性，默认值为'小明'
    description: Union[str, None] = None    # 可选的描述字段
    price: float                            # 价格字段
    tax: Union[float, None] = None          # 可选的税字段

# 实例化APIRouter以处理POST请求
router = APIRouter()

# 定义处理POST请求的路径操作函数
@router.post("/post")
async def create_item(item: Item):
    # 使用日志记录器记录传入的Item对象信息
    logger.info(f"Received item: name={item.name}, price={item.price}")
    # 返回接收到的Item对象，FastAPI将其转换为JSON响应
    return item