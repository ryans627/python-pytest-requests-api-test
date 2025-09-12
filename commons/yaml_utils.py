import yaml


class YamlUtil:
    """YAML文件读写常用类"""
    def __init__(self, file_path):
        """
        :param file_path:
        """
        self.file_path = file_path

    def read(self):
        f = open(self.file_path, encoding="utf-8")
        data = yaml.safe_load(f)
        return data

    def write(self, data):
        f = open(self.file_path, "w", encoding="utf-8")
        yaml.safe_dump(data, f)
        return True

