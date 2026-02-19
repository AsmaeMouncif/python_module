try:
    file = open("new_discovery.txt", "w+")
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {file.name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    file.seek(0)
    content = file.read()
    print(content)
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file.name}' ready for long-term preservation.")

except PermissionError:
    print("ERROR: Could not create storage unit.")
