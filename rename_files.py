import os
def rename_files():
    #1 get all the file names
    file_names = os.listdir(r"C:\Users\crazy\OneDrive\Udacity\Python\prank\prank")
    print(file_names)
    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)
    os.chdir(r"C:\Users\crazy\OneDrive\Udacity\Python\prank\prank")
    #2 rename the files
    for file_name in file_names:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()


