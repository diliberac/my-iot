"""Mongo database helper"""
import pymongo
from datetime import datetime
from pymongo.errors import ServerSelectionTimeoutError

import settings as sets 
import database

def connect(host, database):
    """Creates a connection"""

    print('Starting %s with pymongo %s' % (__name__, pymongo.__version__))
    print('Connecting to MongoDb: %s | database: %s' % (host, database))
    
    # create connection
    try:
        connection = pymongo.MongoClient(host, serverSelectionTimeoutMS=5000)
        connection.server_info()
    except ServerSelectionTimeoutError as ex:
        print('%s', ex)
        return None

    return  connection[database]

def insert(table, data):
    """insert data into table in mongo server"""

    data['timestamp'] = datetime.now().strftime('%F %T')
    print('DEBUG >>> insert into %s >>> %s', table, data)
    DB[table].insert_one(data.copy())
    return True


def get_table(table, date=datetime.now().strftime('%F'), limit=10):
    """get a table of mongo server by date"""

    result = list(DB[table].find({'timestamp': {'$regex': date}},
                                 {'_id': 0, 'timestamp': 1, 'value': 1})
                  .sort([('_id', -1)])
                  .limit(limit))
    result.reverse()
    return result


# Singleton object mongo database
DB = connect(host=sets.MONGO_SERVER, database=sets.MONGO_DATABASE_DEFAULT)


if __name__ == '__main__':  # pragma: no cover, don't test main
    # exploratory tests
    demo = {'test': 10.2}
    insert('dummy', demo)
    assert get_table('dummy', 'test')[0]['test'] == demo['test']
