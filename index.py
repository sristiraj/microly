#!/bin/bash

import sqlite3



def dbcheck():
    db = sqlite3.connect(r'c:/sqlite3/mydb.db')
    csr = db.cursor()
    rows = csr.execute("select * from mytaburlmap")
    for row in rows:
        print(row)


def dbinsert(URLKey):
    db = sqlite3.connect(r'c:/sqlite3/mydb.db')
    csr = db.cursor()
    try:
        csr.execute('CREATE TABLE mytaburlmap(hash_id int,hash_name int,url char)')
    except:
        pass
    while True:
        h_value = hash(URLKey)
        rows = csr.execute("select 1 from mytaburlmap where hash_name=" + str(h_value))
        if rows.rowcount <= 0:
            break
    if h_value < 0:
        h_value *= -1
    # print(h_value)
    rows = csr.execute("select 1 from mytaburlmap where url='" + URLKey + "'")
    row = rows.fetchone()
    print(row)
    if row is not None:
        csr.close()
        db.close()
        return 'Already registered'
    else:
        csr.execute("insert into mytaburlmap values(1," + str(h_value) + ",'" + URLKey + "')")
        csr.execute('commit')
        csr.close()
        db.close()
        return 'URL Registered'


def dbgetencodedurl(URLKey):
    db = sqlite3.connect(r'c:/sqlite3/mydb.db')
    csr = db.cursor()
    rows = csr.execute("select hash_name from mytaburlmap where url='" + URLKey + "'")
    row = rows.fetchone()
    csr.close()
    db.close()
    #return 'http://127.0.0.1:8088/micro.ly/' + str(row[0])
    return 'http://127.0.0.1:8088/micro.ly/index.html'


def dbgetdecodedurl(hash_name):
    db = sqlite3.connect(r'c:/sqlite3/mydb.db')
    csr = db.cursor()
    hash_code = hash_name.split("/", len(hash_name))
    print(hash_code[-1])
    print("select URL from mytaburlmap where hash_name=" + str(hash_code[-1]) )
    rows = csr.execute("select URL from mytaburlmap where hash_name=" + str(hash_code[-1]))
    # print(rows.rowcount)
    try:
        if rows is not None:
            row = rows.fetchone()
            csr.close()
            db.close()
            return str(row[0])
        else:
            csr.close()
            db.close()
            return 'Not registered'
    except Exception as e:
        csr.close()
        db.close()
        return 'Not registered'

if __name__ == '__main__':
    print(dbinsert('https://www.google.com/tomorrowneverdies/goodoneisheretostay2'))
    print(dbgetencodedurl('https://www.google.com/tomorrowneverdies/goodoneisheretostay2'))
    print(dbgetdecodedurl('http://micro/micro.ly/496429028'))
    print(dbgetdecodedurl('http://micro/micro.ly/496429028'))
    dbcheck()
    csr.close()
    db.close()
