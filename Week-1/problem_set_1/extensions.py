
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
    else:
        print("false")
    
    
main ()