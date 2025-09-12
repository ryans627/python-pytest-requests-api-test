import yaml

f = open("data.yml", encoding="utf-8")
data = yaml.safe_load(f)
print(data) # [100, 200, 3.14, 'jasldjsak', 'daskiuyioqwu', 'asdasdadada', True, True, None, 'None', datetime.datetime(2025, 10, 11, 22, 30, 31)]