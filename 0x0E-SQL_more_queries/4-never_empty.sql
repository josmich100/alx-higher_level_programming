-- creates the table id_not_null on MySQL server with cols id and name
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256) NOT NULL
);
