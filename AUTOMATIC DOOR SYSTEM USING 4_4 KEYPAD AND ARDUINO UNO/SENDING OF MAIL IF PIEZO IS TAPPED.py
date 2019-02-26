import smtplib
while(1):
    readMe=open('file.txt','r')
    str=readMe.read(1)
    print(str)
    if(str=='1'):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("akash8085851357@gmail.com", "asbaitpune@101")
            
            msg = "Exam time has arrived. Please send the SECURITY CODE"
            server.sendmail("your email adresss", "sharma.vinish13498@gmail.com", msg)
            server.quit()
            print ('email sending succesfull!')
            break
            
        except:
             print ('0')
             
             


                    
readMe.close()
