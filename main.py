# 导入FastAPI框架及其相关功能
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 导入自定义的路由模块
from get import router as get_router    # 路由处理GET请求
from post import router as post_router  # 路由处理POST请求

# 从logger_config模块中导入日志记录器
from logger_config import logger

# 实例化FastAPI应用
app = FastAPI()

# 注册路由到FastAPI应用中。通过include_router方法，可以将多个路由模块添加到应用中。
app.include_router(get_router)   # 注册GET路由
app.include_router(post_router)  # 注册POST路由

# 添加CORSMiddleware中间件以支持跨域请求
# CORS（Cross-Origin Resource Sharing）允许或限制来自外部域的请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # 允许所有域名请求
    allow_credentials=True,  # 允许请求带有凭据
    allow_methods=["*"],     # 允许所有的HTTP方法
    allow_headers=["*"],     # 允许请求携带所有的头信息
)

# 定义应用启动事件
@app.on_event("startup")
async def startup_event():
    # 在应用启动时记录日志信息
    logger.info("Application is starting up...")

# 定义应用关闭事件
@app.on_event("shutdown")
async def shutdown_event():
    # 在应用关闭时记录日志信息
    logger.info("Application is shutting down...")

# 仅当该脚本直接运行时才执行以下代码块
if __name__ == "__main__":
    # 导入Uvicorn，用于运行FastAPI应用的ASGI服务器
    import uvicorn  
    logger.info("Starting server...")
    # 使用Uvicorn运行应用：指定应用为main模块中的app实例
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    logger.info("Server stopped.")