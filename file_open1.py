from importlib.machinery import PathFinder
import os


c_dir = r"C:\\"
d_dir = r"D:\\"
e_dir = r"E:\\"
itemc = os.listdir(c_dir)
itemd = os.listdir(d_dir)
iteme = os.listdir(e_dir)
ans = []

def PathRemover(path, value):
    
    lst = [itm for itm in path.split(r'\\')]
    lst.remove(value)
    ans = r'\\'.join(lst)
    return ans

def isValidPath(path):
    try:
        listofdir = os.listdir(path)
        return listofdir
    except (PermissionError, NotADirectoryError, FileNotFoundError):
        return []
app = []
folder = []
file = []
def SearchFile(path, name):
    listofdir = isValidPath(path);
    if listofdir is []:
        return
    if "System Volume Information" in listofdir:
        listofdir.remove("System Volume Information")
    for itm in listofdir:
       
        if name in itm.lower() and '.lnk' in itm:
            app.append(path+itm)
            continue
        elif name in itm.lower() and '.' in itm:
            file.append(path+itm)
            continue
        elif name in itm.lower():
            folder.append(path+itm)
        path += itm + r"\\"
        SearchFile(path, name)
        path = PathRemover(path, itm)


#SearchFile(c_dir, "All", ans)
query = "google"
SearchFile(r"C:\\Shortcuts\\", query)
SearchFile(d_dir, query)
SearchFile(e_dir, query)
print("Apps are :- ")
for itm in app:
    print(itm)
print("\nFiles are:- ")
for itm in file:
    print(itm)
print("\nFolders are :- ")
for itm in folder:
    print(itm)