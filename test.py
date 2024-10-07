
from CDMFrp import FrpcClient
from CDMFrp import FrpsClient
from CDMFrp.logger import setup_logger
#客户端
if __name__ == '__main__':
    logger = setup_logger(level="debug", log_file='frpc.log')

    # 示例：使用配置文件
    frpc_with_file = FrpcClient(config_path='/path/to/your/config.toml')
    frpc_with_file.start()

    # 示例：使用代码中定义的配置
    frpc_with_code = FrpcClient(
        server_addr='0.0.0.0:7000',
        token='your_token',
        user='your_user',
        admin_addr=7400,
        admin_user='admin_user',
        admin_pwd='admin_pwd'
    )
    frpc_with_code.start()

    try:
        input("按任意键停止...\n")
    finally:
        frpc_with_file.stop()
        frpc_with_code.stop()


#服务端
logger = setup_logger( level="DEBUG", log_file='frps.log')

# 使用配置文件初始化 FRPS 服务端
frps_with_file = FrpsClient(config_path='frps.toml')
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