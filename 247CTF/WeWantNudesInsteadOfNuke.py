IV = bytearray.fromhex("391e95a15847cfd95ecee8f7fe7efd66")
CT = bytearray.fromhex("8473dcb86bc12c6b6087619c00b6657e")

# Hashes from the description of challenge
ORIGINAL_MESSAGE = bytearray.fromhex(
    "464952455f4e554b45535f4d454c4121")  # FIRE_NUKES_MELA!

ALTERED_MESSAGE = bytearray.fromhex(
    "53454e445f4e554445535f4d454c4121")  # SEND_NUDES_MELA!

ALTERED_IV = bytearray()

# XOR
for i in range(16):
    ALTERED_IV.append(ALTERED_MESSAGE[i] ^ ORIGINAL_MESSAGE[i] ^ IV[i])
print(f'THE FLAG IS: flag{{{ALTERED_IV.hex()},{CT.hex()}}}')
