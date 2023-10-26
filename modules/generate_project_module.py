import pathlib
from tinydb import TinyDB, Query

current_path = pathlib.Path(__file__).parent.resolve()

db = TinyDB(f'{current_path}/db.json')

db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})