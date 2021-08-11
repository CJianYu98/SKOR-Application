## Method 1:
from sqlalchemy import create_engine, MetaData, text
engine = create_engine(
    "mysql+mysqlconnector://skor:skorPassword@localhost:3306/skor", future=True)

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * from student"))
#     for row in result:
#         print(f"{row.name}, {row.email}")

metadata = MetaData(bind=engine)
metadata.reflect()
metadata.drop_all()


## Method 2:
# import sys
# sys.path.insert(1, '../docker/microservices')
# from models import *
# db.drop_all()
# db.create_all()


# student = Student(
#     email = "jianyu.chen.2019@smu.edu.sg",
#     name = "Chen Jian Yu",
#     actualPassword = "abcdd",
#     password = "abcdd"
# )
# db.session.add(student)
# db.session.commit()


# file = open('./test.sql', 'r')
# sql_file = file.read()

# stmt = sql_file.split(';')
# for i in stmt:
#     print(f"STATEMENT: {i.strip()}\n")
#     db.engine.execute(i.strip())
