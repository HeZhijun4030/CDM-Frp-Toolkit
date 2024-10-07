# CDMFrpc

# 环境依赖
- Python 3.8+

# 使用
### 使用配置文件
````python
from pyfrpc import FrpcClient

# 使用配置文件初始化客户端
frpc_with_file = FrpcClient(config_path='/path/to/your/config.ini')

# 启动 FRPC 客户端
frpc_with_file.start()

# 停止 FRPC 客户端
frpc_with_file.stop()
 ````

### 使用代码中定义的配置
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

# 配置项说明
以下是一些常见的配置项及其说明：

- **server_addr**: FRP 服务端的地址和端口，格式为 IP:Port。
- **token**: 用于身份验证的令牌。
- **user**: 用户名。
- **admin_addr**: 管理接口的监听地址和端口，格式为 Port。
- **admin_user**: 管理接口的用户名。
- **admin_pwd**: 管理接口的密码。

#### 更多配置项可以参考 [FRP 官方文档。](https://github.com/fatedier/frp/blob/master/README_zh.md)