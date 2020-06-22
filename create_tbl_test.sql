-- по правильному повторяющиеся данные надо бы разнести по разным таблицам
-- типа статуса и ОКВЭД, а вместо них поставить внешние ключи на другие таблицы

CREATE TABLE IF NOT EXISTS tbl_test(
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	created DATETIME DEFAULT NOW(),
	title VARCHAR(200),
	ogrn VARCHAR(20),
	okpo VARCHAR(20),
	status VARCHAR(40),
	regdate DATE,
	moneys BIGINT,
	okved VARCHAR(40),
	PRIMARY KEY (id)
);
