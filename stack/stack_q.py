def validate_format(chars: str) -> bool:
	lookup = {'{': '}', '[': ']', '(': ')'}
	stack = []

	for char in chars:
		if char in lookup.keys():
			stack.append(lookup[char])
		if char in lookup.values():
			if not stack:
				return False
			if char != stack.pop():
				return False
	if stack:
		return False

	return True


if __name__ == '__main__':
	j = "}"
	print(validate_format(j))
