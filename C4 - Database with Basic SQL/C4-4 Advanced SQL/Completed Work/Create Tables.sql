CREATE TABLE Customers (
    Id INTEGER NOT NULL,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    City TEXT,
    Country TEXT NOT NULL,
    Phone TEXT NOT NULL,
    PRIMARY KEY(Id)
);

CREATE TABLE Products (
    Id INTEGER NOT NULL,
    ProductName TEXT,
    UnitPrice NUMERIC,
    Package TEXT,
    SupplierName TEXT,
    SupplierCountry TEXT,
    PRIMARY KEY(Id)
);

CREATE TABLE Orders (
    Id INTEGER NOT NULL,
    OrderDate TEXT NOT NULL,
    CustomerID INTEGER NOT NULL,
    ProductID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    FOREIGN KEY(CustomerID) REFERENCES Customers(Id),
    FOREIGN KEY(ProductID) REFERENCES Products(Id),
    PRIMARY KEY(Id)
);
