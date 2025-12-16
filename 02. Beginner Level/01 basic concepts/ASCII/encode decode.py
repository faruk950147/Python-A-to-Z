# ==================== What is Encoding and Decoding ====================

# Encoding:
# Encoding is the process of converting data from one form to another —
# usually from a human-readable format (like text) into a machine-readable format (like bytes or binary).

# Example:
text = "Hello"
encoded = text.encode("utf-8")  # Encode string to bytes
print(encoded)  
# Output: b'Hello'  # Converted to bytes (binary form)

# ----------------------------------------------------------------------

# Decoding:
# Decoding is the reverse process — converting the encoded data (bytes)
# back into its original form (string).

# Example:
decoded = encoded.decode("utf-8")  # Decode bytes back to string
print(decoded)
# Output: Hello  # Converted back to string
