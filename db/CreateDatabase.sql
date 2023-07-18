USE MaisTodosTeste;

CREATE TABLE credit_cards (
    id integer not null auto_increment,
    exp_date varchar(10) not null,
    holder varchar(70) not null,
    card_number varchar(16) not null,
    cvv varchar(4) not null,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET character_set_connection = utf8;

INSERT INTO MaisTodosTeste.credit_cards
(exp_date, holder, card_number, cvv)
VALUES('2025-06-30','Jackeline Brito','5436575218035610','593');
INSERT INTO MaisTodosTeste.credit_cards
(exp_date, holder, card_number, cvv)
VALUES('2025-02-28','Ana Joana','5493787031323780','269');
INSERT INTO MaisTodosTeste.credit_cards
(exp_date, holder, card_number, cvv)
VALUES('2024-07-31','Flavio Coelho','5164300972138585','472');