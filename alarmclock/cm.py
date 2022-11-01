from db import PostConnect
import time

with PostConnect(db_name="postgres") as db_m:

    # db_m.execute("select * from students")
    db_m.cur.execute(f"insert into budelnik(ism, vaqt) VALUES ('Firdavs','21:21');")
    student = db_m.cur.fetchall()
    db_m.commit()

