import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5_2 = hashlib.md5()
md5_2.update('how to use md5 '.encode('utf-8'))
md5_2.update('in python hashlib?'.encode('utf-8'))
print(md5_2.hexdigest())

# sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha256 = hashlib.sha256()
sha256.update('how to use sha256 in python hashlib?'.encode('utf-8'))
print(sha256.hexdigest())

# 练习
db = {
	'michael': 'e10adc3949ba59abbe56e057f20f883e',
	'bob': '878ef96e86145580c38c87f0410ad153',
	'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user,password):
	pwd = hashlib.md5()
	pwd.update(password.encode('utf-8'))
	if pwd.hexdigest() == db[user]:
		return True
	else:
		return False
# 测试
assert login('michael', '123456')
assert login('bob', 'abc999')
assert  login('alice', 'alice2008')
assert not login('michael', '12344')
assert not login('bob', '131213')
assert not login('alice', '312312')
print('ok')