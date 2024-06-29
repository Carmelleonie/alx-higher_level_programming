#!/usr/bin/python3
"""
Write a script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for row in query:
        print("{}: {}".format(row.id, row.name))

