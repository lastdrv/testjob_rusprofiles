-- так то по правильному повторяющиеся данные надо бы разнести по разным таблицам
-- типа статуса и ОКВЭД, а вместо них поставить внешние ключи на другие таблицы
CREATE TABLE IF NOT EXISTS tbl_test(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	created DATETIME DEFAULT NOW(),
	title VARCHAR(200),
	ogrn VARCHAR(15),
	okpo INT,
	status VARCHAR(40),
	-- regdate DATE,
	regdate VARCHAR(40),
	money INT,
	okved VARCHAR(40),
	PRIMARY KEY (id)
);

-- INSERT INTO tbl_test (title,ogrn,okpo,status,regdate,money) VALUES('title','ogrn',1,'status','regdate',2,'okved');
