from dataclasses import dataclass
from psycopg import Connection


@dataclass(frozen=True)
class User:
    id: int
    first_name: str
    surname: str
    middle_name: str

    @classmethod
    def from_tuple(cls, data):
        return cls(
            id=data[0],
            first_name=data[1],
            surname=data[2],
            middle_name=data[3],
        )


class Users:
    def __init__(self, connection: Connection) -> None:
        self.con = connection

    def get_all(self) -> list[User]:
        with self.con.cursor() as cur:
            cur.execute("SELECT id, first_name, surname, middle_name FROM users")
            data = cur.fetchall()

        return [User.from_tuple(d) for d in data]

    def get_one(self, id: int) -> User:
        with self.con.cursor() as cur:
            cur.execute(
                "SELECT id, first_name, surname, middle_name FROM users WHERE id = %(id)s",
                {"id": id},
            )
            data = cur.fetchone()
        return User.from_tuple(data)
