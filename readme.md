# CDM Frp Toolkit
![Static Badge](https://img.shields.io/badge/Only-CodeManStudio-blue)

---

CDM Frp Toolkit 是一个 Python 库，用于简化 FRP 客户端的使用。它提供了两种方式来初始化客户端：配置文件和代码中定义的配置。

---
# 环境依赖
- Python 3.8+
- [Frp 客户端](https://github.com/fatedier/frp/releases)

# 使用
## 客户端
### 使用配置文件

````python
from CDMFrp import FrpcClient

# 使用配置文件初始化客户端
frpc_with_file = FrpcClient(config_path='/path/to/your/config.ini')

# 启动 FRPC 客户端
frpc_with_file.start()

# 停止 FRPC 客户端
frpc_with_file.stop()
 ````

### 使用代码中定义的配置

````python
from CDMFrp import FrpcClient

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
## 服务端
````python
from CDMFrp.server import FrpsClient
from CDMFrp.logger import setup_logger

# 自定义日志配置
logger = setup_logger(level="DEBUG", log_file='frps.log')

# 使用配置文件初始化 FRPS 服务端
frps_with_file = FrpsClient(config_path='frps.ini')
frps_with_file.start()

# 使用代码中定义的配置初始化 FRPS 服务端
frps_with_code = FrpsClient(
    bind_port=7000,
    token='your_token',
    dashboard_addr='0.0.0.0',
    dashboard_port=7500,
    dashboard_user='admin_user',
    dashboard_pwd='admin_pwd',
    log_file='./frps.log',
    log_level='info',
    log_max_days=3
)
frps_with_code.start()

try:
    input("按任意键停止...\n")
finally:
    frps_with_file.stop()
    frps_with_code.stop()
````


# 日志功能
cdmfrpc 库集成了日志记录功能，以便于调试和监控。默认的日志级别为 INFO，日志格式为 
````
%(asctime)s - %(levelname)s - %(message)s。
````

启用日志
默认情况下，日志会输出到控制台。你也可以通过配置 logging 模块来自定义日志输出方式。

#### 自定义日志配置 示例：
```` python
from CDMfrpc import FrpcClient
from CDMfrpc.logger import setup_logger

# 自定义日志配置 详细设置见代码注释
logger = setup_logger(level="DEBUG", log_file='frpc.log') 


# 使用配置文件初始化客户端
frpc_with_file = FrpcClient(config_path='/path/to/your/config.ini')

# 启动 FRPC 客户端
frpc_with_file.start()

# 停止 FRPC 客户端
frpc_with_file.stop()
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