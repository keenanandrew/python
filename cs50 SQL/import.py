import csv

# opens the data source, read-only
with open("data.tsv", "r", encoding="utf-8") as titles:

    # the 'reader' looks through the tab-separated file
    reader = csv.DictReader(titles, delimiter="\t")

    # opens a new csv, or creates it if needed
    with open("shows1.csv", "w") as shows:

        # if the reader reads...
        writer = csv.writer(shows)

        # writes the header row
        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        # means for *every* row
        for row in reader:

            # neat way to skip rows with a null/weird startYear
            if row["startYear"] == "\\N":
                # skips back to start of loop
                continue

            # skips rows with startYear before 1970
            year = int(row["startYear"])
            if year < 1970:
                continue

            # filtering further...
            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

                # writes the rest of the rows
                writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])
