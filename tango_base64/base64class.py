# Coding: UTF-8
# RFC 4648 (The Base16, Base32, and Base64 Data Encodings)
# https://tex2e.github.io/rfc-translater/html/rfc4648.html#10--Test-Vectors

from sys import version_info
from binascii import a2b_hex
from .base64tables import encoding_tables, decoding_tables

class Base64:
	def __init__(self, value):
		self.before_value = value


	def base64_encode(self):
	# Python Version Confirm
		if version_info.major > 2:
			xrange = range

	# Encode String
		encode_string = self.before_value.encode('UTF-8')

	# Convert data => Base-2 Numbers
		bainali_string = ''.join(format(encode_string_tmp, '08b') for encode_string_tmp in encode_string)
		bainali_string_len = len(bainali_string)

	# Bainali Split 6bits AND Add 0 to be 6bits
		while ((bainali_string_len % 6) != 0):
			bainali_string += '0'
			bainali_string_len = len(bainali_string)
	
	# Convert 6bits  => Characters
		encode_value = ''.join((encoding_tables.get(bainali_string[i:i+6], 'No-Key ')) for i in xrange(0, len(bainali_string), 6))

	# Split 4Characters AND Add = to be 4Characters
		encode_value_len = len(encode_value)
		while ((encode_value_len % 4) != 0):
			encode_value += '='
			encode_value_len = len(encode_value)

		return encode_value


	def base64_decode(self):
	# Python Version Confirm
		if version_info.major > 2:
			xrange = range

	# Delete Equal Fill
		encode_value = self.before_value.replace("=", "")

	# Convert Characters => Base-2 Numbers
		bainali_string = ''.join((decoding_tables.get(encode_value[i:i+1], 'No-Key ')) for i in xrange(0, len(encode_value), 1))
	
	# Convert Base-2 Numbers => Base-16 Numbers AND Convert Base-16 Numbers => Characters
		decode_value = a2b_hex(''.join(format(int(bainali_string[i:i+8], 2), '02x') for i in xrange(0, len(bainali_string), 8))).decode('UTF-8')

		return decode_value