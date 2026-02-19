try:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = open("ancient_fragment.txt", "r")
    print(f"Accessing Storage Vault: {file.name}")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(file.read())
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")
except (FileNotFoundError, PermissionError):
    print("ERROR: Storage vault not found. Run data generator first.")
