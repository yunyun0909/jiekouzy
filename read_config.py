import yaml


class Readconfig:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file, "r", encoding="utf-8") as f:
            # 为了避免警报,参数里需要加入Loader=yaml.FullLoader
            dat = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
        # print(data)
        return dat

    def write_yaml(self):
        with open(self.yaml_file, "w", encoding="utf-8") as f:
            data = [{"编测编学": [{"name": "lisi"}, {"age": 20}]}]
            # 如果写入有中文，参数里要加上allow_unicode=True
            yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == "__main__":
    a = Readconfig("config.yaml")
    print(a.read_yaml())
    # b = Readconfig("config.yaml")
    # b.write_yaml()
