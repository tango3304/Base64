# Coding: UTF-8
# RFC 4648 (The Base16, Base32, and Base64 Data Encodings)
# https://tex2e.github.io/rfc-translater/html/rfc4648.html#10--Test-Vectors

from .base64tables import encoding_tables
from sys import version_info

def base64_encode(string):
# Python Version Confirm
	if version_info.major > 2:
		xrange = range

# Encode String 
	encode_string = string.encode('UTF-8')

# Convert Bainali
	bainali_string = ''.join(format(encode_string_tmp, '08b') for encode_string_tmp in encode_string)
	bainali_string_len = len(bainali_string)

# Bainali Split 6bits AND Add 0 to be 6bits
	while ((bainali_string_len % 6) != 0):
		bainali_string += '0'
		bainali_string_len = len(bainali_string)

# Convert 6bits Characters
	encode_value = ''.join((encoding_tables.get(bainali_string[i:i+6], 'No-Key ')) for i in xrange(0, len(bainali_string), 6))

# Split 4Characters AND Add = to be 4Characters
	encode_value_len = len(encode_value)
	while ((encode_value_len % 4) != 0):
		encode_value += '='
		encode_value_len = len(encode_value)

	return encode_value