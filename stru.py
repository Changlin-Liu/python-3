import struct
import binascii
values = (1, b'abc', 2.7)     #定义一个元组，包含int、str、float三种数据类型
s = struct.Struct('I3sf')     #定义struct对象，并制定format'I3sf',I表示int3s表示三个字符的字符串f表示float
packed_data = s.pack(*values)     #pack将字符串转换为二进制字节串
unpacked_data = s.unpack(packed_data)     #unpack将字节串转换为元组

print('Original values:', values)
print('Format string :', s.format)
print('Uses :', s.size, 'bytes')
print('Packed Value :', binascii.hexlify(packed_data))
print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)