#Problem set 1 - File extensions v1 
def main ():

    file_name = input("File name: ").strip().lower()
   
    extensions = (".gif" ,
                  ".jpg" ,
                  ".jpeg" ,
                  ".png" ,
                  ".pdf" ,
                  ".txt" ,
                  ".zip" )
    
    if file_name.endswith(extensions):

        if extensions[0] in file_name:
            print("image/gif")
        elif extensions[1] in file_name:
            print("image/jpg")
        elif extensions[2] in file_name:
            print("image/jpeg")
        elif extensions[3] in file_name:
            print("image/png")
        elif extensions[4] in file_name:
            print("application/pdf")
        elif extensions[5] in file_name:
            print("text/plain")
        elif extensions[6] in file_name:
            print("application/zip")
    else:
        print("application/octet-stream ")
    
    
main ()