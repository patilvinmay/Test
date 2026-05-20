import re

def extract_outer_select(sql):

    # ==========================================
    # REMOVE COMMENTS
    # ==========================================
    sql = re.sub(r'--.*?(\n|$)', ' ', sql)
    sql = re.sub(r'/\*.*?\*/', ' ', sql, flags=re.DOTALL)

    sql = sql.strip()

    # ==========================================
    # FIND FIRST SELECT
    # ==========================================
    select_pos = sql.upper().find("SELECT")

    if select_pos == -1:
        return None

    # ==========================================
    # KEEP ONLY FROM SELECT ONWARD
    # ==========================================
    sql = sql[select_pos:]

    # ==========================================
    # REMOVE EXTRA WRAPPING BRACKETS
    # ==========================================
    sql = sql.strip()

    while sql.endswith(")"):
        sql = sql[:-1].strip()

    while sql.startswith("("):
        sql = sql[1:].strip()

    # ==========================================
    # REMOVE LAST ;
    # ==========================================
    if sql.endswith(";"):
        sql = sql[:-1]

    return sql.strip()
