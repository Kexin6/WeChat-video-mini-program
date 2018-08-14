def makeAlbum(singer, name, numberSongs = ''):
    album = {singer: name}
    #return album
    flag = True
    while flag:
       print("Please enter a singer and a name (q for quit)")
       singerInput = input("singer: ")
       if singerInput == 'q':
           #flag = False
            break

       nameInput = input("Album name: ")
       if nameInput == 'q':
           #flag = False
            break
       albumInput =  {singerInput:nameInput}

       print(albumInput)





makeAlbum('hi', 'hey')





