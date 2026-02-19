print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")

print("SECURE EXTRACTION:")
try:
    with open("classified_data.txt", "r") as file:
        content = file.read()
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"ERROR {e}")

print("\nSECURE PRESERVATION:")
try:
    with open("security_protocols.txt", "a+") as file:
        file.write("\nVault automatically sealed upon completion")
        file.seek(0)
        content = file.read()
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"ERROR {e}")

print("\nAll vault operations completed with maximum security.")
