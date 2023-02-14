# I pledge my honor that I have abided by the Stevens Honor System.
# Jacob Gurevich and Max Takacs
print("Write the name of your instruction file here: ") 
assembly_message = input()
with open(assembly_message, 'r') as file:
    space = file.readline()
    data_mem = []
    pos = 0
    while (space != 'END' and space != ''):
        if (space[0:3] == 'LDR'): # 00
            pos = (int(space[4:6]))<<2 # memory location
            pos = pos + (int(space[8])) # where we load to
            if len(hex(pos)[2:4]) == 1:
                data_mem.append('0'+hex(pos)[2:4]) # making sure size is consistent with 8-bit opcode
            else:
                data_mem.append(hex(pos)[2:4])
        if (space[0:3] == 'ADD'): # 01
            pos = 1<<6
            pos = pos + (int(space[5])<<4) #reg 1
            pos = pos + (int(space[8])<<2) #reg 2
            pos = pos + (int(space[11])) # dest reg
            data_mem.append(hex(pos)[2:4])
        
        if (space[0:3] == 'SUB'): # 10
            pos = 1<<7
            pos = pos + (int(space[5])<<4) # reg 1
            pos = pos + (int(space[8])<<2) # reg 2
            pos = pos + (int(space[11])) # dest reg
            data_mem.append(hex(pos)[2:4])

        space = file.readline()
    
    file.close()

print("Name your desired instruction memory file: ")
memory = input()
with open(memory, 'w') as g:
    temp = 0
    while (temp != len(data_mem)): # formatting the imagefile
        g.write(data_mem[temp]+ ' ')
        temp += 1
    g.close()


