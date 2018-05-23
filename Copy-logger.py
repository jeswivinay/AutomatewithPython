""" python script maintaning clipboard content acccesed via Copy Paste commonas 
    Author : Eamme Vinay Kumar
    JNTU Anantapuram
"""

import os
import pyperclip as ppp
import time

"""fname=raw_input("Enter the file name")"""
savepath=os.getcwd()
fname=time.strftime("%d-%m-%y")
cn=os.path.join(savepath,fname+'.txt')
oldcopy="sample"
space=0

while(1):
        f2=open(cn,'a+')
        content=ppp.paste()
        content=content[0:50]
        """if(len(content)<50):                 //trying to put spaces
                sp=len(content)-50
                while(sp):
                        content=content+" "
                        sp=sp-1"""
        if(oldcopy==content):
            continue
        f2.write(content)
        f2.write(time.strftime('%c'))
        f2.write("\n")
        oldcopy=content
        f2.close()
