data_file_old = "Data/data_train.csv"
data_file_new = "Data/data_train_new.csv"
def load_ratings():
    """Loads the rating data from the specified file.
    Does not yet build the rating matrix. Use 'ratings_to_matrix' to do that.
    Assumes the file has a header (which is ignored), and that the ratings are
    then specified as 'rXXX_cXXX,X', where the 'X' blanks specify the row, the
    column, and then the actual (integer) rating.
    """
    ratings = []
    with open(data_file_old, 'r') as file:
        # Read header.
        _ = file.readline()
        for line in file:
            key, value_string = line.split(",")
            rating = int(value_string)
            row_string, col_string = key.split("_")
            row = int(row_string[1:])
            col = int(col_string[1:])

            if rating < 1 or rating > 5:
                raise ValueError("Found illegal rating value [%d]." % rating)

            ratings.append((row - 1, col - 1, rating))
    
    with open(data_file_new, 'w') as file:
        for i, j, rating in ratings:
            file.write('%d\t %d\t %d\n' % (i,j,rating))

if __name__ == "__main__":
    load_ratings()
