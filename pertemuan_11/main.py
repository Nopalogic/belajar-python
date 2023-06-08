# list -> array, mengakses dengan menggunakan index

data_list = ['ucup','otong','dudung']

print(data_list[0])

## Dictionary
# dictionary (dict) -> associative array
# identifier -> key

data_dict = {
	'key': 'value',
	'cp': 'ucup',
	'tg': 'otong',
	'dg': 'dudung',
	'nmbr': 100,
	'list': data_list,
}

print(data_dict['tg'])
print(data_dict['nmbr'])
print(data_dict['list'])

print()

dictionary = {"kucing": "meow", "Anjing": "wogf", "buaya": "kalo aku chat kamu ada yang marah ga?"}
phoneContacts = {"Ipan": 141513, "Galih": 123413, "Hamid": 11341}
emptyDictionary = {}

print(dictionary)
print(phoneContacts)
print(emptyDictionary)

print()

# operator dictionary

data_dict = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"faqih": "faqihza si kweren"}) # kalau gak ada diadd ajah
print(data_dict)

# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)

print()

# looping dictionary

teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

# looping first try (yang keluar adalah keynya)

for teman in teman_teman:
	print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
	print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
	print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
	print(item)

for key,value in teman_teman.items():
	print(f"key = {key}, value = {value}")
	
print()

# copy dictionary

teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"]="ucup si kweren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir ajah)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")
