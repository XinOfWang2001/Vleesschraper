CREATE TABLE IF NOT EXISTS Meatproduct   (
    DateCode bigint,
    Title varchar(255),
    Capitalized_Title varchar(255),
    Normal_Price float,
    Current_Price float,
    Discount int,
    PRIMARY KEY (DateCode, Capitalized_Title)
)

