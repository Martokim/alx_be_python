CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id(foreign key reference Authors.author_id),
    price DOUBLE PRECISION,
    publication_date DATE
)
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215),
)

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    adddress TEXT
)

CREATE TABLE Order_details(
    orderdetail_id INT PRIMARY KEY,
    order_id(foreign key reference Orders.order_id),
    book_id(foreign key reference Books.book_id),
    quantity DOUBLE PRECISION,
)