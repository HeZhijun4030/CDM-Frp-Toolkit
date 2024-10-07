import subprocess
import os
import signal
import tempfile

class FrpcClient:
    def __init__(self, config_path=None, **kwargs):
        """
        初始化 FRPC 客户端。

        :param config_path: 配置文件路径，如果提供了此参数，则忽略 kwargs 中的配置项。
        :param kwargs: 如果没有提供配置文件，则通过这些关键字参数传递配置。
        """
        self.config_path = config_path
        self.process = None
        if not config_path:
            # 如果没有提供配置文件，则构建一个临时配置文件
            self.config_content = self._build_config(**kwargs)
            self.config_path = self._write_temp_config(self.config_content)

    def _build_config(self, **kwargs):
        """
        构建 FRPC 配置内容。

        :param kwargs: 配置项字典。
        :return: 配置字符串。
        """
        config = '[common]\n'
        for key, value in kwargs.items():
            config += f'{key} = {value}\n'
        return config

    def _write_temp_config(self, content):
        """
        将配置内容写入临时文件。

        :param content: 配置字符串。
        :return: 临时文件路径。
        """
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
            temp_file.write(content)
            temp_file.flush()
            return temp_file.name

    def start(self):
        """
        启动 FRPC 客户端。
        """
        if not self.config_path:
            raise ValueError("配置文件路径未设置")
        self.process = subprocess.Popen(['frpc', '-c', self.config_path])

    def stop(self):
        """
        停止 FRPC 客户端。
        """
        if self.process:
            self.process.send_signal(signal.SIGINT)
            self.process.wait()
            self.process = None
        if self.config_path and os.path.exists(self.config_path):
            # 清理临时文件
            os.remove(self.config_path)

    def __del__(self):
        self.stop()