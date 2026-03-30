from db.repository import DocumentRepository
from core.file_manager import FileManager
from core.thumbnails import ThumbnailGenerator

class DocumentService:
    def __init__(self):
        self.repo = DocumentRepository()
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()

    def upload_document(self,uploaded_file, tags, decription, lecture_date=None):
        doc=[]
        #1. Save a file 
        file_path = self.file_manager.save_file(uploaded_file)

        #2. Generate Thumbnail
        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)

        #3. Get total Pages
        total_pages = self.thumbnail_generator.get_total_pages(file_path)

        #4. Convert to images

        #6. Save to db
        # self.repo.add_document(doc)


