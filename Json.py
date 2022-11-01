import json

student='{"name":"davron","age":"19"}'

#loads bu jsonga ugirish
y=json.loads(student)

#json.dumps bu json faylni str formatga uzgartiradi
students={"name":"davron","age":19}
yt=json.dumps(students)
print(type(yt))
print(y["age"])
