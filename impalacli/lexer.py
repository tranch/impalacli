import re
from pygments.lexer import words, RegexLexer
from pygments.token import *


class ImpalaLexer(RegexLexer):
    """Extends SQL lexer to add keywords."""
    name = 'Impala'
    aliases = ['impala']
    filenames = ['*.sql']

    mimetypes = ['text/x-sql']

    flags = re.IGNORECASE
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'--.*\n?', Comment.Single),
            (r'/\*', Comment.Multiline, 'multiline-comments'),
            (words((
                'ADD', 'AGGREGATE', 'ALL', 'ALTER', 'ANALYTIC', 'AND', 'ANTI', 'API_VERSION', 'AS', 'ASC', 'AVRO',
                'BETWEEN', 'BUCKETS', 'BY', 'CACHED', 'CASCADE', 'CASE', 'CAST', 'CHANGE', 'CLASS', 'CLOSE_FN',
                'COLUMN', 'COLUMNS', 'COMMENT', 'COMPUTE', 'CREATE', 'CROSS', 'CURRENT', 'DATA', 'DATABASE',
                'DATABASES', 'DELETE', 'DELIMITED', 'DESC', 'DESCRIBE', 'DISTINCT', 'DISTRIBUTE', 'DIV', 'DOUBLE',
                'DROP', 'ELSE', 'END', 'ESCAPED', 'EXISTS', 'EXPLAIN', 'EXTENDED', 'EXTERNAL', 'FALSE', 'FIELDS',
                'FILEFORMAT', 'FINALIZE_FN', 'FIRST', 'FOLLOWING', 'FOR', 'FORMAT', 'FORMATTED', 'FROM',
                'FULL', 'FUNCTION', 'FUNCTIONS', 'GRANT', 'GROUP', 'HASH', 'HAVING', 'IF', 'IGNORE', 'ILIKE', 'IN',
                'INCREMENTAL', 'INIT_FN', 'INNER', 'INPATH', 'INSERT', 'INTERMEDIATE', 'INTO', 'INVALIDATE',
                'IREGEXP', 'IS', 'JOIN', 'LAST', 'LEFT', 'LIKE', 'LIMIT', 'LINES', 'LOAD', 'LOCATION', 'MERGE_FN',
                'METADATA', 'NOT', 'NULL', 'NULLS', 'OFFSET', 'ON', 'OR', 'ORDER', 'OUTER', 'OVER', 'OVERWRITE',
                'PARQUET', 'PARQUETFILE', 'PARTITION', 'PARTITIONED', 'PARTITIONS', 'PRECEDING', 'PREPARE_FN',
                'PRODUCED', 'PURGE', 'RANGE', 'RCFILE', 'REAL', 'REFRESH', 'REGEXP', 'RENAME', 'REPLACE', 'RESTRICT',
                'RETURNS', 'REVOKE', 'RIGHT', 'RLIKE', 'ROLE', 'ROLES', 'ROW', 'ROWS', 'SCHEMA', 'SCHEMAS', 'SELECT',
                'SEMI', 'SEQUENCEFILE', 'SERDEPROPERTIES', 'SERIALIZE_FN', 'SET', 'SHOW', 'SPLIT', 'STATS', 'STORED',
                'STRAIGHT_JOIN', 'SYMBOL', 'TABLE', 'TABLES', 'TBLPROPERTIES', 'TERMINATED', 'TEXTFILE', 'THEN', 'TO',
                'TRUE', 'TRUNCATE', 'UNBOUNDED', 'UNCACHED', 'UNION', 'UPDATE', 'UPDATE_FN', 'USE', 'USING', 'VALUES',
                'VIEW', 'WHEN', 'WHERE', 'WITH'), suffix=r'\b'),
             Keyword),
            (words(('BIGINT', 'BINARY', 'BOOLEAN', 'CHAR', 'DATE', 'DATETIME', 'DECIMAL', 'FLOAT', 'INT', 'INTEGER',
                    'INTERVAL', 'STRING', 'SMALLINT', 'VARYING', 'TINYINT', 'TIMESTAMP'), suffix=r'\b'), Name.Builtin),
            (r'[+*/<>=~!@#%^&|`?-]', Operator),
            (r'[0-9]+', Number.Integer),
            # TODO: Backslash escapes?
            (r"'(''|[^'])*'", String.Single),
            (r'"(""|[^"])*"', String.Symbol),  # not a real string literal in ANSI SQL
            (r'[;:()\[\],.]', Punctuation)
        ],
        'multiline-comments': [
            (r'/\*', Comment.Multiline, 'multiline-comments'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[^/*]+', Comment.Multiline),
            (r'[/*]', Comment.Multiline)
        ]
    }
