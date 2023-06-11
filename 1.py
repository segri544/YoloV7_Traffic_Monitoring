# idx = 1  # the ID to check for in l1
# l1=[(1,20.02),(2,21.25)]

# # iterate over each tuple in l1 and check the first element (the car ID)
# if any(entry[0] == idx for entry in l1):
#     print(f"{idx} is in l1")
# else:
#     print(f"{idx} is not in l1")



# Example list of tuples
# lst = [("car1", 10), ("car2", 20), ("car3", 30)]

# # Remove tuple where the first value is "car2"
# lst = [tup for tup in lst if tup[0] != "car2"]

# # Print the resulting list
# print(lst)

# import os
# os.system("python detect_or_track5.py --weights 982-11mb.pt  --view-img --source vid2.mp4 --conf 0.5 --show-fps --nosave")

# start=1678190916.9392571
list1 = [(5, 15.13, 1678190916.9392571), (6, 18.51, 1678190927.6431942), (1, 2.83, 1678190998.010182)]
import time

list1 = [entry for entry in list1 if entry[2]+30 < 1678190916]
print(time.time())
print(type(time.time()))