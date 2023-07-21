# Coding: UTF-8

from binascii import a2b_hex
from .base64tables import decoding_tables
from sys import version_info

def base64_decode(encode_value):
# Python Version Confirm
	if version_info.major > 2:
		xrange = range

# Delete Equal Fill
	encode_value = encode_value.replace("=", "")

# Convert Characters => Base-2 Numbers
	bainali_string = ''.join((decoding_tables.get(encode_value[i:i+1], 'No-Key ')) for i in xrange(0, len(encode_value), 1))

# Convert Base-2 Numbers => Base-16 Numbers AND Convert Base-16 Numbers => Characters
	decode_value = a2b_hex(''.join(format(int(bainali_string[i:i+8], 2), '02x') for i in xrange(0, len(bainali_string), 8))).decode('UTF-8')

	return decode_value