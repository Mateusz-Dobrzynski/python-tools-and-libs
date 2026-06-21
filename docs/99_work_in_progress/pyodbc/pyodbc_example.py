import hashlib
import logging
import logging.config
import os
import uuid

import pyodbc
import yaml

with open("logging_conf.yaml", "r", encoding="utf-8") as f:
    logging.config.dictConfig(yaml.safe_load(f))

logger = logging.getLogger(__name__)

HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
PORT = os.getenv("MYSQL_PORT", "3306")
DATABASE = os.getenv("MYSQL_DB", "fridge")
USER = os.getenv("MYSQL_USER", "root")
PASSWORD = os.getenv("MYSQL_PASSWORD", "")


DRIVER = "MariaDB Unicode"  # The driver name must the output of `odbcinst -q -d`

connection_string = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={HOST};"
    f"PORT={PORT};"
    f"DATABASE={DATABASE};"
    f"UID={USER};"
    f"PWD={PASSWORD};"
)


def get_hash(plain: str) -> str:
    return hashlib.md5(plain.encode()).hexdigest()


def new_uuid() -> str:
    return str(uuid.uuid4())


def print_pretty_output(rows, columns):
    output = "Query result: \n"
    output += "\n── users ──────────────────────────────────────────────────────────\n"
    col_widths = {
        col: max(len(col), max(len(str(row[i])) for row in rows))
        for i, col in enumerate(columns)
    }

    header = "  ".join(col.ljust(col_widths[col]) for col in columns)
    divider = "  ".join("-" * col_widths[col] for col in columns)
    output += f"{header}\n"
    output += f"{divider}\n"
    for row in rows:
        output += (
            "  ".join(str(val).ljust(col_widths[col]) for col, val in zip(columns, row))
            + "\n"
        )

    output += f"\n{len(rows)} row(s) returned."
    logger.info(output)


# ── seed data ─────────────────────────────────────────────────────────────────

USERS = [
    ("alice", "alice@example.com", "hunter2"),
    ("bob", "bob@example.com", "correct-horse"),
    ("charlie", "charlie@example.com", "battery-staple"),
]

# ── main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    logger.info(f"Connecting to {HOST}:{PORT}/{DATABASE} as {USER} …")
    conn = pyodbc.connect(connection_string, autocommit=False)
    cursor = conn.cursor()

    logger.info("Dropping table `users` (if exists)…")
    cursor.execute("DROP TABLE IF EXISTS users")

    logger.info("Creating table `users`…")
    cursor.execute("""
        CREATE TABLE users (
            uuid          CHAR(36)     NOT NULL UNIQUE,
            username      VARCHAR(64)  NOT NULL UNIQUE,
            email         VARCHAR(255) NOT NULL UNIQUE,
            password_hash CHAR(64)     NOT NULL,
            PRIMARY KEY (uuid)
        )
    """)

    logger.info(f"Inserting {len(USERS)} user(s)…")
    insert_sql = """
        INSERT INTO users (uuid, username, email, password_hash)
        VALUES (?, ?, ?, ?)
    """
    for username, email, plain_password in USERS:
        cursor.execute(
            insert_sql,
            (
                new_uuid(),
                username,
                email,
                get_hash(plain_password),
            ),
        )

    conn.commit()

    cursor.execute("SELECT uuid, username, email, password_hash FROM users")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print_pretty_output(rows, columns)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
