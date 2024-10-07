
from CDMFrpc import FrpcClient
from CDMFrpc.logger import setup_logger
if __name__ == '__main__':
    logger = setup_logger(level="debug", log_file='frpc.log')

    # 示例：使用配置文件
    frpc_with_file = FrpcClient(config_path='/path/to/your/config.ini')
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