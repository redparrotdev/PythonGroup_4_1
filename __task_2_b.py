keys = ["key1", "key2", "key3", "key4"]
values = [145, 12.4, False, "Some Text"]

my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)
