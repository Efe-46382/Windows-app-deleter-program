import os
import sys
import ctypes
import shutil

def is_admin():
    """Checks for administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return os.getuid() == 0

def delete_anything():
    print("--- Advanced Admin Removal Tool ---")
    print("Warning: This will permanently delete files, folders, or .exe apps.")
    
    target_path = input("\nEnter the full path of the item to delete: ").strip().strip('"')


    if not os.path.exists(target_path):
        print("Error: The path provided does not exist.")
        return

    
    print(f"\nTARGET ACQUIRED: {target_path}")
    choice = input("Are you sure you want to delete this? This cannot be undone. (y/n): ").strip().lower()

    if choice == 'y':
        try:
            if os.path.isfile(target_path) or os.path.islink(target_path):
                os.remove(target_path)
            elif os.path.isdir(target_path):
                shutil.rmtree(target_path)
            
            print("Action successful: Item has been deleted.")
        except PermissionError:
            print("Error: Access denied. The item may be in use by another program or protected by System/TrustedInstaller.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == 'n':
        print("Action cancelled.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    if is_admin():
        delete_anything()
        input("\nPress Enter to exit...")
    else:
        if os.name == 'nt':
        
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            print("Please run this script with root privileges (sudo).")