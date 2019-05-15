import os
import time


fp = open("commands.txt", "r")

commands = []
for line in fp:
    if line.strip() == "": 
        continue
    commands.append(line.strip())

#print (commands)  

def make_external_command(term, cmd):
    ex_cmd = "target_term -run "
    ex_cmd = ex_cmd + str(term)+" "
    
    ex_cmd = ex_cmd + cmd   #I might have to incorporate skip 
                            #characters here to support quoted inputs
    return ex_cmd
                
i = 0

while(i<len(commands)):
    time.sleep(0.5)
    print("next command:")
    print (commands[i])
    h = (input ("h for help #:")).strip()
    
    if h == "e":
        #os.system(cmd)
        cmd = make_external_command(1,commands[i])
        print ('executing:',commands[i])
        os.system(cmd)
        i += 1
    elif h == "p":
        if i is not 0:
            cmd = make_external_command(1,commands[i-1])
        print("re_executing: ",commands[i-1])
        os.system(cmd)
    elif h== "q":
        break
    elif h=="s":
        print("skipping")
        i+=1
    elif h=="h":
        print("e: execute next command","\np: execute previous command","\ns: skip current command","\nq: quit")
    else:
        continue


