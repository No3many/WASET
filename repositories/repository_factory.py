# لسه هنضيف الـ Imports لما زمايلك يعملوا الملفات بتاعتهم
from repositories.user_repository import UserRepository

class RepositoryFactory:
    @staticmethod
    def get_repository(repo_type):
        if repo_type == "user":
            # return UserRepository()  <-- هنشيل الكومنت ده لما نعمل الملف
            pass
        elif repo_type == "auction":
            # return AuctionRepository()
            pass
        else:
            raise ValueError("Unknown repository type")