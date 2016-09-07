from peewee import *

db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db
            

class Faculty(BaseModel):
    name = CharField(max_length=25, unique=True)


class Major(BaseModel):
    major_id = CharField(max_length=10, unique=True)
    name = CharField(max_length=255, unique=True)
    faculty = ForeignKeyField(Faculty, related_name='majors')


class User(BaseModel):
    class Status:
        confirmed = 'confirmed'
        pending = 'pending'

    account_number = CharField(max_length=10, unique=True)
    name = CharField(max_length=255)
    email = CharField(max_length=100)
    password = CharField(max_length=100)
    major = ForeignKeyField(Major, related_name='users')
    campus = CharField(max_length='20', default='San Pedro Sula')
    creation_date = DateTimeField()
    modification_date = DateTimeField()
    settled = BooleanField(default=False)
    status = CharField(max_length=20, default=Status.pending)
    is_deleted = BooleanField(default=False)


class Class(BaseModel):
    code = CharField(max_length=5, unique=True)
    Name = CharField(max_length=25, unique=True)


class Period(BaseModel):
    number = IntegerField()
    year = IntegerField()
    start_date = CharField(max_length=25)
    end_date = CharField(max_length=25)
    is_current = BooleanField(default=False)


class Project(BaseModel):
    project_id = CharField(max_length=25)
    name = CharField(max_length=25)
    description = TextField()
    is_deleted = BooleanField(default=False)
    benefited_organization = CharField(max_length=30)


class ProjectMajor(BaseModel):
    project = ForeignKeyField(Project)
    major = ForeignKeyField(Major)


class Role(BaseModel):
    name = CharField(max_length=10, unique=True)


class UserRole(BaseModel):
    user = ForeignKeyField(User)
    role = ForeignKeyField(Role)


class Section(BaseModel):
    code = CharField(max_length=20)
    class_ = ForeignKeyField(Class, related_name='sections')
    period = ForeignKeyField(Period, related_name='sections')
    user = ForeignKeyField(User, related_name='sections')


class SectionProject(BaseModel):
    section = ForeignKeyField(Section)
    project = ForeignKeyField(Project)
    is_approved = BooleanField(default=False)
    description = TextField()
    cost = DoubleField(default=0.0)


def main():
    db.connect()
    db.create_tables([User, Major, Class, Faculty, Period, Project, ProjectMajor, Role, UserRole, Section, SectionProject], safe=True)
    

if __name__ == '__main__':
    main()
