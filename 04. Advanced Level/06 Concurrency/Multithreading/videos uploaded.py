import threading
import time

videos = ['video1.mp4', 'video2.mp4', 'video3.mp4', 'video4.mp4', 'video5.mp4']

""" class VideoUploader(threading.Thread):
   def run(self):
     for video in videos:
        print(f"Started uploading {video}")         
        time.sleep(0.5)
        print(f"Video uploaded {video}")
      
if __name__ == "__main__":
    thread = VideoUploader()
    thread.start()
    thread.join() """


class VideoUploader(threading.Thread):
    def __init__(self, video):
        super().__init__()
        self.video = video
        
    def run(self):
        print(f"Started uploading {self.video}")         
        time.sleep(0.5)
        print(f"Video uploaded {self.video}")
      
if __name__ == "__main__":
    videos = ["video1.mp4", "video2.mp4", "video3.mp4"]  

    threads = []
    for v in videos:
        thread = VideoUploader(v)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    print("All videos uploaded successfully!")




  

""" 

videos = ['video1.mp4', 'video2.mp4', 'video3.mp4', 'video4.mp4', 'video5.mp4']
def upload_video(video):
   print(f"Started uploading {video}")
   time.sleep(5)
   print(f"Uploaded {video}")
   
for i in range(5):
    time.sleep(0.5)
    print("Video Copyrighted")


print("All videos uploaded")
 """