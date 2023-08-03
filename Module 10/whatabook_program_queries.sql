/*
Title: whatabook_program_queries
Author: Zachary Tharp
Date: August 3, 2023
Description: whatabook program queries
*/

use whatabook

-- select query to view user wishlist
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
	INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN user On wishlist.book_id = book.book_id
WHERE user.user_id = 1;

-- select query to view user wishlist
SELECT store_id, locale from store;

-- select querey to view a full list of WhatABook books
SELECT book_id, book_name, author, details from book;

-- select query to show books that are not already in a user's wishlist. 
-- the user_id will need to be replaced with the actual values the user selects in the program
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

-- insert statements to add a new book to wishlist.
-- the values will need to be replaced with values the user selects in the program
INSERT INTO wishlist (user_id, book_id)
	VALUES (1, 9)
    
-- remove a book from a user wishlist
-- the user_id and book_id will need to be replace with values that are selected by the user in the program
DELETE FROM wishlist WHERE user_id =1 AND book_id = 9;
    

