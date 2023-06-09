class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
print(object_1.val)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1
print(object_1.val)
object_1.val=1500
print(object_3.val)


print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"
print(string_1)
print(string_2)

print(string_1 == string_2, string_1 is string_2)