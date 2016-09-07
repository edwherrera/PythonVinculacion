import models


class _BaseRepository:
    def get_all(self):
        return self.model.select()

    def get(self, **query):
        return self.model.get(**query)

    def add(self, **params):
        return self.model.create(**params)

    def delete(self, **params):
        found = self.get(**params)
        found.delete_instance()
        return found


class Role(_BaseRepository):
    def __init__(self):
        self.model = models.Role


class User(_BaseRepository):
    def __init__(self):
        self.model = models.User

    def get_by_role(self, role):
        return models.UserRole.select(UserRole, User, Role).join(User).join(Role).where(models.Role.name == role)


class Faculty(_BaseRepository):
    def __init__(self):
        self.model = models.Faculty


class Major(_BaseRepository):
    def __init__(self):
        self.model = models.Major


class Class(_BaseRepository):
    def __init__(self):
        self.model = models.Class


class Period(_BaseRepository):
    def __init__(self):
        self.model = models.Period


class Project(_BaseRepository):
    def __init__(self):
        self.model = models.Project


class ProjectMajor(_BaseRepository):
    def __init__(self):
        self.model = models.ProjectMajor


class Role(_BaseRepository):
    def __init__(self):
        self.model = models.Role


class Section(_BaseRepository):
    def __init__(self):
        self.model = models.Section
