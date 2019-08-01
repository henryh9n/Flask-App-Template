#!/usr/bin/env python3

"""Document description."""

__version__ = '0.0.1'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2018, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Production"

import psycopg2
from psycopg2.extras import NamedTupleCursor


class DB(object):
    """ Weapper for psycopg 2 to interact with DB

    Parameters
    ----------
    host : str
    user : str
    pwd : str
    dbname : str
    
    """

    insert = "INSERT INTO %s(%s) VALUES (%s) %s"
    update = "UPDATE %s SET %s WHERE %s %s"
    select = "SELECT %s FROM %s %s WHERE %s %s"
    select_count = "SELECT SUM(src.count) AS count FROM (%s) AS src"
    delete = "DELETE FROM %s WHERE %s"

    def __init__(self, host: str, user: str, pwd: str, dbname: str):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        self.transaction = False
        self.conn = psycopg2.connect(
            "dbname='{}' user='{}' host='{}' password='{}'".format(
                self.dbname, self.user, self.host, self.pwd))

        super().__init__()

    def reconnect(self):
        """ Close the current connection and reconnect to the DB

        """
        self.conn.close()
        self.conn = psycopg2.connect(
            "dbname='{}' user='{}' host='{}' password='{}'".format(
                self.dbname, self.user, self.host, self.pwd))

    def execute(self, query: str, args: dict = {}) -> NamedTupleCursor:
        """ Execute the query

        Parameters
        ----------
        query : str
        args : dict

        Returns
        -------
        NamedTupleCursor

        """

        if self.conn.closed != 0:
            self.reconnect()

        cur = self.conn.cursor(cursor_factory=NamedTupleCursor)

        try:
            cur.execute(query, args)
            if not self.transaction:
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            raise Exception(ex)
        return cur

    def commit(self):
        """ Commits the open transaction if any found """
        if self.transaction:
            self.conn.commit()
            self.transaction = False

    def rollback(self):
        """ Rallbacks current transaction """
        self.conn.rollback()
        self.transaction = False
