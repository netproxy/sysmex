import email
import os
import sys


filepaths = []

def enumeml(path):
    for file_or_dir in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path,file_or_dir))
        if os.path.isdir(abs_path):
            enumeml(abs_path)
        else:
            if file_or_dir.lower().endswith('.eml'):
                filepaths.append(abs_path)
    return filepaths



filelist = enumeml('./')
for mailpath in filelist:
    fp = open(mailpath, "r")
    msg = email.message_from_file(fp)

    # 循环信件中的每一个mime的数据块
    for par in msg.walk():
        if not par.is_multipart(): # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。
            name = par.get_param("name") #如果是附件，这里就会取出附件的文件名
            #name  = msg.get("subject")
            if name:
                #有附件
                # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
                h = email.header.Header(name)
                dh = email.header.decode_header(h)
                fname = dh[0][0]
                #print ('附件名:', fname)
                data = par.get_payload(decode=True) #　解码出附件数据，然后存储到文件中
                try:
                    f = open(fname, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
                except:
                    f = open('aaaa', 'wb')
                f.write(data)
                f.close()
            #else:
            #    print (par.get_payload(decode=True)) # 解码出文本内容，直接输出来就可以了。




