import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n", file=sys.stdout)

archivist_id = input("Input Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ")
print()

print(
    f"[STANDARD] Archive status from {archivist_id}: {status}",
    file=sys.stdout)
print(
    "[ALERT] System diagnostic: Communication channels verified",
    file=sys.stderr)
print("[STANDARD] Data transmission complete", file=sys.stdout)

print("\nThree-channel communication test successful.", file=sys.stdout)
