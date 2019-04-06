def colocation(word):
    import PyPDF2
    import os
    import random
    import smtplib
    # define variable
    count = 0
	
    # listar todos os arquivos da pasta de referencias
    folder_references = []
    directory = "C:\\Users\\p1613091\\Documents\\Endnote Library\\My EndNote Library.Data\\PDF"
    for file in os.listdir(directory):
        folder_references.append(file)
    random.shuffle(folder_references) # random list
    # print ("folder_references = ",folder_references)
    for file in folder_references:
        name_pdf = os.listdir(directory + "\\" + file)
        # print ("name_pdf = ",name_pdf)
        try:
            pdfFileObj = open(directory + "\\" + file + "\\" + name_pdf[0],'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pages = pdfReader.numPages
            if pages > 100: # skip book, standards and some thesis
                print ("Name of the File = ",name_pdf)
                print ("paper skiped because it has more than 100 pages")
                print ("\n") # pular uma linha
                continue
            for k in range(0,pages):
                pageObj = pdfReader.getPage(k)
                pageTextSentence = pageObj.extractText().split(".") # separate sentences into pages
                # print ("pageTextSentence = ",pageTextSentence[0],len(pageTextSentence))
                for i in range(0,len(pageTextSentence)):
                    # print ("i =",i)
                    pageTextWords = pageTextSentence[i].split() # separate words into sentences
                    # print ("pageTextWords = ",pageTextWords,len(pageTextWords))
                    for item in pageTextWords:
                        # print (item)
                        if item == word:
                            count += 1
                            print ("\n") # pular uma linha
                            try:
                                print ("Name of the File = ",name_pdf)
                            except:
                                print ('error printing name_page')
                            try:
                                print (pageTextSentence[i].replace("\n",""))
                            except:
                                print ('error printing sentence')
                            print ("\n") # pular uma linha
            pdfFileObj.close()
        except:
            print ("file is not in english")
            try:
                print ("Name of the File = ",name_pdf)
            except:
                print ("Name of the File = ",name_pdf.encode('utf-8').strip())
                print ("bame of the file obtained with tis pice of code 'encode('utf-8').strip()'")
    print ("Foram encontrados %d itens na pesquisa" %count)
			
    # enviar email
    smtp_srv = "smtp.live.com"
    server = smtplib.SMTP(smtp_srv,587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("jjvenel@hotmail.com", "rDrrphsfscbbxmds")
    server.sendmail("jjvenel@hotmail.com", "uvevsiidzd@pomail.net", '\nfinalizou script "colocation", palavra "%s"' %word)
    server.quit()

	
import sys
word = str(sys.argv[1])
colocation(word)
