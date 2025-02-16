from typing import Generic, TypeVar
from data.repositories.sql.sql_base_repository import SQLBaseRepositoryAsync


class BaseRepositoryService():
    def __init__(self, repository: SQLBaseRepositoryAsync):
        self.repository = repository
