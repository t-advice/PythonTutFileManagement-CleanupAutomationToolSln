import os # This is python libary , allowing access to windows machine 

print("Tashwill's Automation Tool: Folder Scan")
print("-" *35)

#1. Asking which folder to scan 
#   For a quick test, i will use the "Downloads" folder
folder_path = input("C:\Users\USER\Downloads")

#2. Check if the folder actually exists
if os.path.exists(folder_path):
    print("\nScanning folder...Please wait.")

    # list all the files inside my downloads folder
    all_files = os.listdir(folder_path)

    print(f"Total items found: {len(all_files)}")
    print("-" *35)

    # 3. The filter loop
    text_file_count= 0