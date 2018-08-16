# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:12:53 2018
@author: Jamie Johns 2018

NOTE; randomally encrypts (modifys) encoding within files w.r.t to random
      numbert seed specified by user and changes file type back to ".jim"
      files
      to decrypt .jim files (return to original data and type); use random generator
      seed that was used to encrypt files

in this version of encrypt jim (encrupt_jim_2);
choose seed for random number to encrypt ( and same number needed to
perfectly decrypt)

Note: tested in windows OS 7 , unsure of what specific operating systems
this program will or will not work on



"""

import string #import sting module, for function which translate char w.r.t two strings
import os #import os module (operating system), use for browsing directory and setting text color in program
import numpy #import numpy module (used for random number generator and random permutation function)
os.system('color 1E') #set color of yellow text on blue [for cmd of script converted to program]

print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print '$$$$$$$$$$$$$$$$$$$$$$ FILE ENCRYPTER $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print ' '
print '                      Created by Jamie Johns                           '
print '                            in python 2.7    '
print ' '
print '######################## DESCRIPTION ##################################'
print 'This is a experimental program for encrypting (and decrypting) files   '
print 'with an arbitrary encryption (defined in source code).                 ' 
print 'The file type of encrypted file are ".jim" files.                      '
print ' '
print 'Since this program was created for personal use, the creator of this  ' 
print 'program takes no responsibility any for misuse of this program such as,   '
print 'but not limited to; resulting in loss of files.'
print '########################################################################'
raw_input('<Press any key to continue>')
char_orig='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' #original char
op_choose=0 #paramter which determines if correct option has been selected below
while op_choose==0: #while correct option has not been chosen
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print 'In next line enter; '
    print '                    "encrypt" to run encryption'
    print '                    "decrypt" to run descryption'
    print '                     (without quoatations)      '
    print 'Or, exit the program. '
    chce=raw_input('>Enter in choice: ') #input choice of encrypt or decrypt
    if chce in 'encrypt': #if encrypt entered
        op_choose=1 #set choice =1 (encrypt option); exit on next while loop iteration
    elif chce in 'decrypt': #if decrypt entered
        op_choose=2 #set choice =2 (decrypt option); exit on next while loop iteration
    if op_choose==0: #if no correct choice entered; flash warning and restart while loop
        print ' '
        print 'Incorrect input!!'
        print 'try again, or exit the program....'
        raw_input('<Press enter to continue>')        
                
# After correct choice chosen from above
      
if op_choose==1: #If encryption option#######################################################################################
    oper_complete=0 #param which indicates if folder read and no problem encrypting/reading files
    print 'You have chosen to perform encryption!!\n\n'
    while oper_complete==0: # while operation has been not completed with no errors
        try: # try run encryption (incl selecting folder of files to encrypt)
            print 'Below paste link to folder containing all files to'
            print 'be encrypted.'
            folda=raw_input('>input:') #folder (directory) input
            path, dirs, files = os.walk(folda).next()  #test if input directory does not result in an error (gets list of all paths and file in directory cwd)
            fold_found=1 #if no error above, working directory found (exit while loop)            
            print 'Folder has successfully been read!'
            rn_seed=input('Now, input seed for random number generator:')  # choose rand seed ("encryption/decryption key")
            numpy.random.seed(int(rn_seed)) #set seed for random number generator (used next line; w.r.t previous input)
            indx=numpy.random.permutation(len(char_orig))   #array of numbers representing 0 to number of char in "char_orig" string [list 'random' created with seed (last line)]          
            char_encrypt=[char_orig[j] for j in indx] #generator new string from "char_orig" using indexing generated in previous line
            char_encrypt=''.join(char_encrypt) #join list (previous line) as single string (for translate function)
            raw_input('<PRESS ENTER TO BEGIN ENCRYPTION>') # wait for user input to begin encryption
            print 'Staring encryption...'
            pc=0 #current percent of process complete
            for k,j in enumerate(files,start=1): #iterate through each jth file in folder (k=file number[int] in list)
                bin_data = open(path+'\\'+j,'rb') #read file j as binary data "rb"
                bf=bin_data.read() #read file
                trans = string.maketrans(char_orig,char_encrypt) #create translator
                bfn=bf.translate(trans)+'{{jim}}'+j.split('.')[1] #translate characters using "trans"
                out_file = open(path+'\\'+j.split('.')[0]+'.jim',"wb") # open new file ('.jim') for [w]riting as [b]inary
                out_file.write(bfn) #write translated (encrypted) data to new file
                out_file.close() #close new file from writing
                bin_data.close() #close old file from reading
                os.remove(path+'\\'+j) #delete old (unencrypted) file
                pc_max=0      #parameter which determine if maximum percent complete has been flashed          
                while pc_max==0: #while maximum percent complete has not been flashed  
                    if pc<=(float(100*(k-1))/float(len(files)-1)): #if actual percent complete is less than next max complete to flash (text)
                        print str(pc)+'% of total process complete'
                        pc=pc+1 #update next percent complete to flash
                    else: #else if max percent complete to flash (text) is surpassed
                        pc_max=1 #exit while loop for printing percent complete
            print 'PROCESS COMPLETE!!'
            print 'The used seed random number ("decryption key") was: '+str(rn_seed)
            print '(make sure to save this numeber[key] for decryption)'            
            raw_input('<PRESS ENTER TO EXIT PROGRAM>') #wait for user response to exit program
            oper_complete=1 #operation complete [program exit after this line]
        except Exception as er1: #if anything in "try" was problematic (error); record python error as string "er1"
            print ' '
            print 'There was a problem with opening folder (or is incorrect'
            print 'directory path) or problem with reading one or more files'
            print 'please try again, or exit the program....'
            raw_input('<PRESS ENTER TO TRY AGAIN>') #wait for user prompt to start again
            print '###############################################################'
            print 'Python related error:'            
            print er1 #print python related error 
            print '###############################################################'
            print 'You have chosen to perform encryption!!\n\n'
else: # ELSE, if decrypt option ######################################################################################################################
    oper_complete=0
    print 'You have chosen to perform decryption!!\n\n'
    while oper_complete==0: # try run decryption (incl selecting folder of files to encrypt)
        try: # try run decryption (incl selecting folder of files to decrypt)
            print 'Below paste link to folder containing all files to'
            print 'be decrypted. (only ".jim" files will be handled)'
            folda=raw_input('>input:') # wait for user input to paste directory containing jim files to decrypt
            path, dirs, files = os.walk(folda).next()  #test if input directory does not result in an error (gets list of all paths and file in directory cwd)
            fold_found=1 #if no error above, working directory found (exit while loop)            
            print 'Folder has successfully been read!'
            rn_seed=input('Now, input seed for random number generator:')              
            numpy.random.seed(int(rn_seed)) #array of numbers representing 0 to number of char in "char_orig" string [list 'random' created with seed (last line)]          
            indx=numpy.random.permutation(len(char_orig))     #array of numbers representing 0 to number of char in "char_orig" string [list 'random' created with seed (last line)]                 
            char_encrypt=[char_orig[j] for j in indx]   #generator new string from "char_orig" using indexing generated in previous line     
            char_encrypt=''.join(char_encrypt)           #join list (previous line) as single string (for translate function)  
            raw_input('<PRESS ENTER TO BEGIN DECRYPTION>') # wait for user input to begin decryption                
            print 'Staring decryption...'
            pc=0 #current percent of process complete
            files_jim=[j for j in files if '.jim' in j] #create list of only jim files (encrypted files)
            for k,j in enumerate(files_jim,start=1): #iterate through each jth (jim) file in folder (k=file number[int] in list)
                bin_data = open(path+'\\'+j,'rb') #read file j as binary data "rb"
                bf=bin_data.read()#read file
                bfo=bf.split('{{jim}}')[0] #get "binary" data of file (not really binary though?)
                trans = string.maketrans(char_encrypt,char_orig) #create translator
                bfn=bfo.translate(trans)+'{{jim}}'+j.split('.')[1] #translate characters using "trans" and grab file type which was encoded in encrypted file
                out_file = open(path+'\\'+j.split('.')[0]+'.'+bf.split('{{jim}}')[1],"wb") # open for [w]riting as [b]inary
                out_file.write(bfn) #write translated (decrypted) data to new file
                out_file.close() #close new file from writing
                bin_data.close()    #close old file from reading             
                os.remove(path+'\\'+j) #delete old (encrypted) file
                pc_max=0    #parameter which determine if maximum percent complete has been flashed                
                while pc_max==0: #while maximum percent complete has not been flashed
                    if pc<=(float(100*(k-1))/float(len(files)-1)): #if actual percent complete is less than next max complete to flash (text)
                        print str(pc)+'% of total process complete'
                        pc=pc+1 #update next percent complete to flash
                    else: #else if max percent complete to flash (text) is surpassed
                        pc_max=1 #exit while loop for printing percent complete
            print 'PROCESS COMPLETE!!'
            print 'The used seed random number ("decryption key") was: '+str(rn_seed)
            raw_input('<PRESS ENTER TO EXIT PROGRAM>') #wait for user response to exit program
            oper_complete=1 #operation complete [program exit after this line]
        except Exception as er1: #if anything in "try" was problematic (error); record python error as string "er1"
            print ' '
            print 'There was a problem with opening folder (or is incorrect'
            print 'directory path) or problem with reading one or more files'
            print 'please try again, or exit the program....'
            raw_input('<PRESS ENTER TO TRY AGAIN>')
            print '###############################################################'
            print 'Python related error:'            
            print er1 #print python related error 
            print '###############################################################'
            print 'You have chosen to perform encryption!!\n\n'