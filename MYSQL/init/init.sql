CREATE DATABASE mydb;
USE mydb;
CREATE TABLE member(num INTEGER PRIMARY KEY AUTO_INCREMENT,email TEXT,pwd TEXT,created_at DATETIME);
CREATE TABLE item(num INTEGER PRIMARY KEY AUTO_INCREMENT,product_name TEXT,product_price INT,product_qty INT,created_at DATETIME);
CREATE TABLE _order(num INTEGER PRIMARY KEY AUTO_INCREMENT,member_id TEXT,item_id TEXT,order_qty INT,order_price INT,created_at DATETIME);
INSERT INTO member(num, email, pwd, created_at) VALUES(null, 'hann', '1111', NOW());
INSERT INTO member(num, email, pwd, created_at) VALUES(null, 'kim', '2222', NOW());
INSERT INTO member(num, email, pwd, created_at) VALUES(null, 'lee', '3333', NOW());
INSERT INTO member(num, email, pwd, created_at) VALUES(null, 'park', '4444', NOW());
INSERT INTO member(num, email, pwd, created_at) VALUES(null, 'son', '5555', NOW());

INSERT INTO member(num, email, pwd, created_at) VALUES(null, 'john', '6666', NOW());

INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'banana', 500, 50, NOW()); 
INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'apple', 2000, 50, NOW()); 
INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'kiwi', 1500, 50, NOW());
INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'grapefruit', 1500, 50, NOW());
INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'grape', 3500, 50, NOW());
INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'cherry', 5000, 50, NOW());
INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'pinepple', 8000, 50, NOW());
INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, 'mango', 8000, 50, NOW());


INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'son', 'grape', 7, 24500,  '2021-01-01 02:10:23');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'park', 'banana', 9, 4500,  '2021-01 05:10:47');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john', 'apple', 6, 12000,  '2021-01-03 05:50:16');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'hann', 'pinepple', 3, 24000,  '2021-01-04 03:10:12');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'lee', 'banana', 14, 7000,  '2021-01-05 08:10:14');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'kim', 'apple', 2, 4000,  '2021-01-06 09:10:27');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'park', 'grapefruit', 8, 12000,  '2021-01-07 12:10:09');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john', 'kiwi', 1, 1500,  '2021-01-29 01:10:28');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'hann', 'apple', 12, 60000,  '2021-01-09 07:10:48');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'kim', 'banana', 1, 500,  '2021-01-10 01:10:27');

INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'son', 'banana', 9, 4500,   '2021-01-14 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john','pinepple', 3, 24000,  '2021-01-12 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null,  'son', 'banana', 14, 7000  '2021-01-13 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'park', 'grapefruit', 8, 12000,  '2021-01-14 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'son', 'pinepple', 3, 24000, '2021-01-30 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john','apple', 12, 60000, '2021-01-20 01:10:17');


INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john', 'grape', 7, 24500,  '2021-01-29 02:10:23');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'son', 'apple', 12, 60000, '2021-01-22 05:10:47');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'park', 'apple', 6, 12000,  '2021-01-03 05:50:16');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'hann', 'pinepple', 3, 24000,  '2021-01-04 03:10:12');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'son', 'pinepple', 3, 24000,,  '2021-01-25 08:10:14');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'kim', 'apple', 2, 4000,  '2021-01-06 09:10:27');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john', 'grapefruit', 8, 12000,  '2021-01-07 12:10:09');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john', 'banana', 14, 7000  '2021-01-28 01:10:28');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'hann', 'apple', 12, 60000,  '2021-01-09 07:10:48');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'kim', 'banana', 1, 500,  '2021-01-10 01:10:27');

INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'son', 'banana', 9, 4500,   '2021-01-21 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'park','banana', 14, 7000  '2021-01-12 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null,  'hann', 'kiwi', 1, 1500,  '2021-01-17 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'lee', 'apple', 12, 60000, '2021-01-14 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'son', 'pinepple', 3, 24000, '2021-01-20 01:10:17');
INSERT INTO _order(num, member_id, item_id, order_qty, order_price, created_at) VALUES(null, 'john', 'banana', 1, 500,   '2021-01-20 01:10:17');
