#Using context manager will automatically close a file without  haing it closed explicitly,
#In case of exception it will close a file ...
# with open("test2.txt",'r') as data:
#     data.write('Test')
#     # data.seek(0)
#     data.write('R')
#     print(data.read())

with open('download.jpg','rb') as rf:
    with open('download_copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


