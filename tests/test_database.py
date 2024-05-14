from praktikum.database import Database


class TestDatabase:

    def test_buns_list_count(self):
        database: Database = Database()
        assert len(database.available_buns()) == 3


    def test_ingredients_list_count(self):
        database: Database = Database()
        assert len(database.available_ingredients()) == 6