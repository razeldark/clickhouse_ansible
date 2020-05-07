#tree view with size and count of each directory

import os
startpath = '\\\\backup1\sqlbackup'
x = open('tmp.csv','w+')
x.close()
print('dir list:')
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        x = open('tmp.csv','a+')
        print('{}{}|'.format(indent, os.path.basename(root)))
        x.write('{}{}'.format(indent, os.path.basename(root)))
        x.write(":")
        subindent = ' ' * 4 * (level + 1)
        filecount=0
        filesize=0
        for f in files:
            print('{}|_{}'.format(subindent, f),end='')
            x.write('{}{}'.format(subindent, f))
            filecount+=1
            filesize+=os.stat(root+"\\"+f).st_size
            print("  ", round((os.stat(root+"\\"+f).st_size /1073741824),2), " Gb")
        if filesize != 0:
            t = ('{}{}'.format(indent, os.path.basename(root))+":"+'{}{}'.format(subindent, f)+":  "+str(round((os.stat(root+"\\"+f).st_size /1073741824),2))+" Gb"+'{}{}'.format(indent, os.path.basename(root))+":"+"files: "+str(filecount)+":  total size: "+ str(round((filesize/1073741824),2))+ "Gb\n")
            x.write(t)
            print('{}|_'.format(subindent),end='')
            print("files: ", filecount,"  total size: ", round((filesize/1073741824),2), "Gb")
        x.close()

list_files(startpath)

