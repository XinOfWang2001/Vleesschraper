----- Create JOIN query
INSERT INTO Meatproduct 
(DateCode, Date, SuperMarket, Title, Capitalized_Title, Normal_Price, Current_Price, Discount, Weight) 
SELECT sm.DateCode, sm.Date, sm.SuperMarket, sm.Title, sm.Capitalized_Title, sm.Normal_Price, sm.Current_Price, sm.Discount, sm.Weight
FROM Stage_Meats sm
    WHERE NOT EXISTS (
        SELECT 1 
        FROM MeatProduct mp 
        WHERE mp.DateCode = sm.DateCode 
        AND mp.Capitalized_Title = sm.Capitalized_Title
    );