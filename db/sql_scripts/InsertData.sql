use kubecaf_db

INSERT INTO users
        (email, password_hash)
VALUES
  ('fsmeu@gmail.com', '41e2cbe589cb11ecdc9c82feb0710ff119fe36c018ab2bd0e93a7009f478a99c'),
  ('user@gmail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');

INSERT INTO exp_cat
	(id, name)
VALUES
  (1, 'Housing'),
  (2, 'Transportation'),
  (3, 'Food'),
  (4, 'Utilities'),
  (5, 'Insurance'),
  (6, 'Medical & Healthcare'),
  (7, 'Saving, Investing & Debt Payments'),
  (8, 'Personal Spending'),
  (9, 'Recreation & Entertainment'),
  (10, 'Miscellaneous');

INSERT INTO inc_cat
	(id, name)
VALUES
  (1, 'Salary'),
  (2, 'Donation');

INSERT INTO expenses
	(id, email, exp_date, exp_sum, exp_cat_id)
VALUES
  (1, 'fsmeu@gmail.com', '2020/02/12', 200, 3),
  (2, 'fsmeu@gmail.com', '2020/02/13', 500, 9),
  (3, 'fsmeu@gmail.com', '2020/02/14', 100, 2),
  (4, 'fsmeu@gmail.com', '2020/02/15', 400, 7),
  (5, 'fsmeu@gmail.com', '2020/02/16', 100, 1),
  (6, 'user@gmail.com', '2020/02/21', 200, 4),
  (7, 'user@gmail.com', '2020/02/22', 800, 2),
  (8, 'user@gmail.com', '2020/02/23', 700, 1),
  (9, 'user@gmail.com', '2020/02/24', 200, 10),
  (10, 'user@gmail.com', '2020/02/25', 100, 5);

INSERT INTO incomes
	(id, email, inc_date, inc_sum, inc_cat_id)
VALUES
  (1, 'fsmeu@gmail.com', '2020/02/01', 500, 1),
  (2, 'fsmeu@gmail.com', '2020/02/03', 500, 2),
  (3, 'user@gmail.com', '2020/02/01', 600, 1),
  (4, 'user@gmail.com', '2020/02/10', 100, 2);
