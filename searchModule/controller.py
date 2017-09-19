import redis

from extensions import engine
from sqlalchemy.orm import sessionmaker
from collections import namedtuple
from Amfi_list.models import AmfiList
DBSession = sessionmaker(bind=engine)
session = DBSession()

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def get_amfi_list():
    print 0
    str = """select t1.* from amfi_list t1 inner join (select amfi_id, max(date) max_date
            from amfi_list
            group by amfi_id) t2
on t1.amfi_id = t2.amfi_id and t1.date = t2.max_date;"""
    list_nav = session.execute(str)
    Record = namedtuple('Record', list_nav.keys())
    records = [Record(*r) for r in list_nav.fetchall()]
    for r in records:
        print(r)
    return records



def start_data_populate():
    print "Loading entries in the Redis DB\n"
    amfi_data = get_amfi_list()
    amfi_list = []
    amfi_object_list = []
    for amfi in amfi_data:
        amfi_list.append(amfi["fund_name"])
        amfi_object_list.append(amfi)

    for i in range(0,len(amfi_list)):
        line = amfi_list[i]
        n = line
        value = line + "**zxxz**" +str(amfi_object_list[i])
        print value
        word_in_title = line.split(" ")
        for l in range(1, len(line)):
            prefix = line[0:l + 1]
            prefix = "ac_" + prefix
            r.zadd(prefix, 0, str(value))
        for word in word_in_title:
            n1 = word.strip()
            for l in range(1, len(n1)):
                prefix = n1[0:l+1]
                prefix = "ac_" + prefix
                r.zadd(prefix, 0, str(value))

start_data_populate()

def complete(prefix):
    results = r.zrange(prefix, 0, -1)
    object_list = []
    for result in results:
        temp_obj ={}
        values = result.split("**zxxz**")
        print values
        temp_obj['suggested_name'] = values[0]
        temp_obj['object'] = values[1]
        object_list.append(temp_obj)
    return object_list

def autoComplete(complete_text):
    complete_text = "ac_" + complete_text
    results = complete(complete_text)
    print results
    return results