
# In this file we only change the condition from write  the file to append in the exicting file"a

st = "Hey Harry you are very brillient programer.\nIm Very exited to learn python from you."

f = open("my file.txt","a")

f.write(st)

f.close()