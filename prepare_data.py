import sqlite3 as sql
import pandas as pd

FILEXLS = "data/Daycare.xls"

TABLENAME = "DAYCARE"

def extrac_column_names(df):
    ## extract each column
    columns_schema = "("
    columns        = "("
    questions      = "("
    for i, colnm in enumerate(df.columns):
        colnm = colnm.replace(" ","_").replace("(","_").replace(")","_").replace("-","_").replace("?","_").replace(",","_")
        columns_schema += "{} TEXT, ".format(colnm)
        columns        += "{}, ".format(colnm)
        questions      += "?,"
    columns_schema = columns_schema[:-2] + ")"
    columns        = columns[:-2]        + ")"
    questions      = questions[:-1]      + ")"
    return(columns_schema, columns, questions)

if __name__ == "__main__":


    df = pd.read_excel(FILEXLS)
    df = df.fillna("") ## NA is not allowed in database

    columns_schema, columns, questions = extrac_column_names(df)
    conn = sql.connect('database.db')
    conn.execute('DROP TABLE IF EXISTS {}'.format(TABLENAME))
    conn.execute('CREATE TABLE {} {}'.format(TABLENAME, columns_schema))

    with sql.connect("database.db") as con:
        cur = con.cursor()
        for irow in range(df.shape[0]):
            row = df.iloc[irow,:]
            cur.execute("INSERT INTO {} {} VALUES{}".format(
                        TABLENAME,columns,questions), tuple(str(a) for a in row.values))
        con.commit()