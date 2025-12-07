from repositories.user_repository import UserRepository
from repositories.listing_repository import ListingRepository

class RepositoryFactory:
    @staticmethod
    def get_repository(repo_type):
        if repo_type == "user":
            return UserRepository()
        elif repo_type == "listing":
            return ListingRepository()
        else:
            raise ValueError("Unknown repository type")