# pip install psycopg2-binary

import psycopg2


class DB:
    con = psycopg2.connect(
        dbname="online_shop_git",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    cur = con.cursor()

    def select(self):
        fields = ', '.join(self.fields)
        table_name = self.__class__.__name__.lower()
        query = f"""select {fields} from {table_name} ;"""
        self.cur.execute(query)
        return self.cur

    def insert(self, **kwargs):
        table_fields = ','.join(kwargs.keys())
        table_name = self.__class__.__name__.lower()
        params = tuple(kwargs.values())
        s = ','.join(['%s']*len(kwargs))
        print(params)
        query = f"""insert into {table_name}({table_fields}) values ({s})"""
        self.cur.execute(query, params)
        self.con.commit()

    def update(self):
        pass

    def delete(self):
        pass


