from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import GroupModel
import unittest

engine = create_engine("sqlite:///test.db")
Session = sessionmaker(bind=engine)

class GroupModelTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        GroupModel.metadata.create_all(engine)

    def tearDown(self):
        self.session.rollback()
        GroupModel.metadata.drop_all(engine)
        self.session.close()

    def test_create_group(self):
        group = GroupModel(name="Group 1")
        self.session.add(group)
        self.session.commit()
        assert group in self.session

    def test_read_group(self):
        group = GroupModel(name="Group 1")
        self.session.add(group)
        self.session.commit()
        assert group.read(self.session) == group

    def test_update_group(self):
        group = GroupModel(name="Group 1")
        self.session.add(group)
        self.session.commit()
        group.name = "New Group Name"
        group.update(self.session)
        assert group.read(self.session).name == "New Group Name"

    def test_delete_group(self):
        group = GroupModel(name="Group 1")
        self.session.add(group)
        self.session.commit()
        group.delete(self.session)
        assert group not in self.session