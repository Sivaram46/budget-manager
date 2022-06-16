USE budget_manager;


CREATE TABLE income_categories (
    category VARCHAR (30) NOT NULL,
    PRIMARY KEY (category)
);

CREATE TABLE expense_categories (
    category VARCHAR (30) NOT NULL,
    PRIMARY KEY (category)
);

INSERT INTO income_categories VALUES ('Salary');
INSERT INTO income_categories VALUES ('Interest');
INSERT INTO income_categories VALUES ('Reward');
INSERT INTO income_categories VALUES ('Invest');

INSERT INTO expense_categories VALUES ('Food');
INSERT INTO expense_categories VALUES ('Travel');
INSERT INTO expense_categories VALUES ('Fun');
INSERT INTO expense_categories VALUES ('Health');

CREATE TABLE income (
    
    income_id INTEGER NOT NULL AUTO_INCREMENT,
    income_date DATE,
    income_amount INTEGER,
    income_description VARCHAR (100),
    income_category VARCHAR (30),

    PRIMARY KEY (income_id),
    FOREIGN KEY (income_category) REFERENCES income_categories (category)
);

CREATE TABLE expense (
    expense_id INTEGER NOT NULL AUTO_INCREMENT,
    expense_date DATE,
    expense_amount INTEGER,
    expense_description VARCHAR (100),
    expense_category VARCHAR (30),
    
    PRIMARY KEY (expense_id),
    FOREIGN KEY (expense_category) REFERENCES expense_categories (category)
);

INSERT INTO expense VALUES (0, DATE('2022-04-10'), 100, 'Dinner', 'Food');
INSERT INTO income VALUES (0, DATE('2022-04-11'), 1000, 'Part time salary', 'Salary');