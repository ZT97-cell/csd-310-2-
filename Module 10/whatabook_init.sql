/*
Title: whatabook_init.sql
Author: Zachary Tharp
Date: August 3, 2023
Description: The creation of the whatabook database, user, and tables. The insertion of values into those tables
*/

-- creating whatabook databse
CREATE DATABASE whatabook;

-- creating the whatabook_user
CREATE USER 'whatabook_user'@'locahlhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- granting priveleges to whatabook_user
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- creating the user table
CREATE TABLE user (
	user_id INT  NOT NULL  AUTO_INCREMENT,
    first_name  INT  NOT NULL,
    last_name  INT  NOT NULL,
    PRIMARY KEY (user_id)
);

-- creating the book table
CREATE TABLE book (
	book_id  INT  NOT NULL  AUTO_INCREMENT,
    book_name  VARCHAR(200)  NOT NULL,
    author  VARCHAR(200)  NOT NULL,
    details  VARCHAR(500),
    PRIMARY KEY (book_id)
);

-- creating the store table
CREATE TABLE store (
	store_id  INT  NOT NULL  AUTO_INCREMENT,
    locale  VARCHAR(500)  NOT NULL,
    PRIMARY KEY (store_id)
);

-- creating the wishlist table 
CREATE TABLE wishlist (
	wishlist_id  INT  NOT NULL  AUTO_INCREMENT,
	user_id  INT  NOT NULL,
	book_id  INT  NOT NULL,
	PRIMARY KEY (wishlist_id),
	CONSTRAINT fk_user
	FOREIGN KEY (user_id)
		REFERENCES user(user_id),
	CONSTRAINT fk_book
	FOREIGN KEY (book_id)
		REFERENCES book(book_id)
);

-- inserting the store records
INSERT INTO store(locale)
	VALUES ('1912 S Park St. Pocahontas,AR 72455');
    
-- inserting book records
INSERT INTO book (book_name, author)
	VALUES ('Watchmen', 'ALvin Moore');
    
INSERT INTO book (book_name, author)
	VALUES ('The Old Man and the Sea', 'Ernest Hemmingway');

INSERT INTO book (book_name, author)
	VALUES ('The Invisibe Man', 'H.G. Wells');
    
INSERT INTO book (book_name, author)
	VALUES ('The Count of Monte Cristo', 'Alexandre Dumas');
    
INSERT INTO book (book_name, author)
	VALUES ('The Great Gatsby', 'F.Scott Fitzgerald');
    
INSERT INTO book (book_name, author)
	VALUES ('Journey to the Center of the Earth', 'Jules Verne');
    
INSERT INTO book (book_name, author)
	VALUES ('Slaughter House 5', ' Kurt Vonnegut');
    
INSERT INTO book (book_name, author)
	VALUES ('Mother Night', 'Kurt Vonnegut');

INSERT INTO book (book_name, author)
	VALUES ('The Sun Also Rises', 'Ernest Hemmingway');
    
INSERT INTO book (book_name, author)
	VALUES ('For Whom the Bell Tolls', 'Ernest Hemmingway');
    
-- inserting into user records
INSERT INTO user (first_name, last_name)
	VALUES ('Aaron', 'Rodgers');
    
INSERT INTO user (first_name, last_name)
	VALUES ('Kirk', 'Cousins');
    
INSERT INTO user (first_name, last_name)
	VALUES ('Josh', 'Allen');
    
-- inserting into wishlist records
INSERT INTO wishlist (user_id, book_id)
	VALUES (
	(SELECT user_id FROM user WHERE first_name = 'Aaron'),
        (SELECET book_id FROM book WHERE book_name = 'Mother Night')
	);

INSERT INTO wishlist (user_id, book_id)
	VALUES (
	(SELECT user_id FROM user WHERE first_name = 'Kirk'),
        (SELECT book_id FROM book WHERE book_name = 'Slaughter House 5')
	);
    
INSERT INTO wishlist (user_id, book_id)
	VALUES (
	(SELECT user_id FROM user WHERE first_name = 'Josh'),
        (SELECT book_id FROM book WHERE book_name = 'The Sun Also Rises')
	);
        




