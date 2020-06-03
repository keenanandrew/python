import csv
import cs50

# creates empty file if needed
open("shows3.db", "w").close()

#opens that file for SQLite
db = cs50.SQL("sqlite:///shows3.db")

# creates a table 'shows' within shows3.db - by executing some SQL
db.execute("CREATE TABLE shows (tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")


# opens the data
with open("data.tsv", "r", encoding="utf-8") as titles:

    # the 'reader' looks through the tab-separated file
    reader = csv.DictReader(titles, delimiter="\t")

    # means for *every* row
    for row in reader:

        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

            if row["startYear"] != "\\N":

                startYear = int(row["startYear"])

                if startYear >= 1970:

                    tconst = row["tconst"]
                    primaryTitle = row["primaryTitle"]
                    genres = row["genres"]

                    # the ? values are placeholders for the variables that come afterwards
                    db.execute("INSERT INTO shows (tconst, primaryTitle, startYear, genres) VALUES(?, ?, ?, ?)", tconst, primaryTitle, startYear, genres)
