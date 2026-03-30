from datetime import datetime
import os

# PDF_storage = os.path.join('storage','pdfs') - Alternative

class FileManager:
       def save_file(self,uploaded_file):
        #Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{uploaded_file.name}"

        file_path = os.path.join('storage','pdfs')
        file_path = os.path.join(file_path, filename)

        print(filename)
        with open(file_path,"wb") as f:
         f.write(uploaded_file.read())
        
        return file_path
       
