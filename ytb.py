from pytube import YouTube

created_program=" Created Dharma Lesmana"
program_language="Python For Language "
name_program="Artifical Intelligence for easier YT link and Cracker Program"

print(created_program)
print("\r",name_program)
print("\r",program_language)
print("="*50)

SAVE_PATH=r"C:/Users/Dharma/Downloads"
youtube_url = input("Masukkan URL Yt : ")

try:
    youtube_obj = YouTube(youtube_url)
    stream = youtube_obj.streams.filter(mime_type='video/mp4')
    for choose in stream:
        print(choose)
    res=str(input("Masukkan Res = "))
    youtube_obj.streams.get_by_resolution(resolution=res).download(output_path=SAVE_PATH, filename='YTDownloadGreenDay')
    print("Sucessfull download")
except:
    print("Some Program has not working")



