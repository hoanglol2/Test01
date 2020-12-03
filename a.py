# create hash table.

# y/c : Hãy thêm số điện thoại của một số người vào danh bạ này?

# cách 1.
# phone_book = dict();
# # cách 2.
# # phone_book = {}; 
# phone_book['jelly'] = 876512;
# phone_book['jone'] = 911;

# print(phone_book);

# tạo 1 hash table theo dõi những người bỏ phiếu.
# voted = {};
# def check_voter(name):
# 	if voted.get(name):
# 		print ('kick them out!')
# 	else:
# 	 	voted[name] = True
# 	print ('let them vote!')

# check_voter('tom');
# check_voter('tom');


# states_needed = set (["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]);
# print (states_needed);

# arr = [1, 2, 2, 3, 3, 3];
# print(set(arr));

# Using hash table.
stations = {};
stations["kone"] = set(["id", "nv", "ut"]);
stations["ktwo"] = set(["wa", "id", "mt"]);
stations["kthree"] = set(["or", "nv", "ca"]);
stations["kfour"] = set(["nv", "ut"]);
stations["kfive"] = set(["ca", "az"]);

final_stations = set();