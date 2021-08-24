import execjs
import json

print(execjs.get().name)

node = execjs.get()


file = 'crypto.js'
ctx = node.compile(open(file).read())

item = {
    'name': '凯文-杜兰特',
    'image': 'durant.png',
    'birthday': '1988-09-29',
    'height': '208cm',
    'weight': '108.9KG'
}

js = f"getToken({json.dumps(item, ensure_ascii=False)})"
print(js)
result = ctx.eval(js)
print(result)
