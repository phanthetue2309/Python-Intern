import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)
print(t)

print(zlib.decompress(t))

print(zlib.crc32(s))