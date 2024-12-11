# 导入FastAPI的APIRouter类，以创建路由器实例
from fastapi import APIRouter

# 实例化APIRouter以处理GET请求
router = APIRouter()

# 定义处理GET请求的路径操作函数
# 通过@router.get装饰器，将该函数绑定到路径"/get"
@router.get("/get")
async def get():
    # 返回一个JSON响应，包含键值对结构的字典
    return {"message": "Hello World"}