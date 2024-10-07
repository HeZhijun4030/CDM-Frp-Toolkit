# CDMFrpc

# 环境依赖
- Python 3.8+

# 使用
- 使用配置文件
````python
from pyfrpc import FrpcClient

# 使用配置文件初始化客户端
frpc_with_file = FrpcClient(config_path='/path/to/your/config.ini')

# 启动 FRPC 客户端
frpc_with_file.start()

# 停止 FRPC 客户端
frpc_with_file.stop()
 ````

- 使用代码中定义的配置
````python
from pyfrpc import FrpcClient

# 使用代码中定义的配置初始化客户端
frpc_with_code = FrpcClient(
    server_addr='0.0.0.0:7000',
    token='your_token',
    user='your_user',
    admin_addr=7400,
    admin_user='admin_user',
    admin_pwd='admin_pwd'
)

# 启动 FRPC 客户端
frpc_with_code.start()

# 停止 FRPC 客户端
frpc_with_code.stop()
````