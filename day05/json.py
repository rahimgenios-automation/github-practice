import json
x = '{"Name":"Abdul", "Gender":"Male"}'
y = json.loads(x)
print(y["Gender"])