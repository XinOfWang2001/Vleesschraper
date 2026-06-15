----- Create JOIN query
INSERT INTO Meatproduct 
(DateCode, Title, Capitalized_Title, Normal_Price, Current_Price, Discount) 
SELECT sm.DateCode, sm.Title, sm.Capitalized_Title, sm.Normal_Price, sm.Current_Price, sm.Discount
FROM Stage_Meats sm
JOIN MeatProducts mp ON mp.DateCode != sm.DateCode AND mp.Capitalized_Title != sm.Capitalized_Title