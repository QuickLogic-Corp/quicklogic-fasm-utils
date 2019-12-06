from .db_entry import DbEntry


class Table(object):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.mapping = {}
        with open(filepath, 'r') as f:
            for l in f:
                entry = DbEntry.from_dbline(l)
                self.mapping[entry.signature] = entry

    def get_entry(self, featurename: str):
        if featurename not in self.mapping:
            return None
        return self.mapping[featurename]


class Database(object):
    def __init__(self, db_root: str):
        self.db_root = db_root
        self.tables = {}

    def add_table(self, tablename: str, filepath: str):
        self.tables[tablename] = Table(filepath)

    def get_table(self, tablename: str):
        return self.tables[tablename]

    def get_feature_from_table(self, tablename: str, featurename: str):
        return self.tables[tablename].get_entry(featurename)

    def get_feature(self, featurename: str):
        for table in self.tables.values():
            feature = table.get_entry(featurename)
            if feature is not None:
                return feature
        return None
