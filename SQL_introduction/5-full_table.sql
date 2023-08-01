-- this is a script that prints full description of table 'first_table' from hbtn_0c_0database
SET @table_name = 'first_table';
SET @database_name = 'hbtn_0c_0';

SELECT
    CONCAT(
        'CREATE TABLE `', @table_name, '` (',
        GROUP_CONCAT(
            CONCAT('`', COLUMN_NAME, '` ', COLUMN_TYPE,
            IF(IS_NULLABLE = 'NO', ' NOT NULL', ''),
            IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', IFNULL(QUOTE(COLUMN_DEFAULT), 'NULL')), ''),
            IF(EXTRA = 'auto_increment', ' AUTO_INCREMENT', ''),
            ',')
            ORDER BY ORDINAL_POSITION
        ),
        IFNULL(
            CONCAT(
                ', PRIMARY KEY (',
                GROUP_CONCAT(
                    IF(COLUMN_KEY = 'PRI', CONCAT('`', COLUMN_NAME, '`'), NULL)
                    ORDER BY ORDINAL_POSITION
                ),
                ')'
            ),
            ''
        ),
        ') ENGINE=', ENGINE, ' DEFAULT CHARSET=', CHARACTER_SET_NAME
    ) AS CreateTableStatement
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = @database_name
    AND TABLE_NAME = @table_name
GROUP BY
    TABLE_NAME,
    ENGINE,
    CHARACTER_SET_NAME;
