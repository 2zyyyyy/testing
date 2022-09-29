



# SQL必知必会

# 第一章 了解SQL

## 1.1 数据库基础

### 1.1.1 什么是数据库

​	数据库软件应该称为数据库管理系统（DBMS）。

​	基础概念讲解，偏理论。

### 1.1.2 表

​	对于数据库而言，表是一种结构化的文件，可用于存储某种特定类型的数据。

- 表（table）某种特定类型数据的结构化清单，每个表都有一个唯一的标识，也就是表名。

- 表名：唯一，数据库名+表名组合，同一个数据库表名唯一，但是在不同的数据库中允许使用相同的表名。

- 模式（schema） 关于数据库和表的布局及特性的信息。

### 1.1.3 列和数据类型

​	表由列组成，列中存储着表中某部分的信息。

- 列（colomn）表中的一个字段，所有的表都是有一个或者多个列组成的。
- 分解数据：正确的将数据分解成多个列极为重要。数据库中每一个列都有相应的数据类型，数据类型定义可以存储的数据种类。
- 数据类型（datatype）所容许的数据的类型，每个列都有相应的数据类型，它限制（或容许）该列中存储的数据。**数据类型可以帮助正确地分类数据，并在优化磁盘使用方面期重要的作用。**
- 数据类型兼容：大概意思就是不同的DBMS相同的数据类型有不同的名称，需要用户在创建表结构的时候记住这些差异

### 1.1.3 行

​	表中的数据是安航存储的。数据库中锤子的为列，水平的为行。

- 行（row）表中的一条记录
- 是记录还是行：很大程度上可以交换使用，但是从技术角度上来说**行才是正确的术语**

### 1.1.5 主键

​	表中每一行都应该有可以唯一标识自己的一列（或一组列）。

- 主键（primary key）一列（或一组列），其值能够唯一标识表中每个行。
- 应该总是定义主键：虽然并不总是都需要主键，但大多数数据库设计人员都保证他们创建的每个表具有一个主键，以便于以后的数据库操纵和管理。

​    表中的任何列都可以作为主键，只要满足以下条件：

+ 任意两行都不具有相同的主键值；
+ 每个行都必须具有一个主键值（主键列不允许为null）；
+ 主键列中的值不允许修改或更新；
+ 主键值不能重用（如果某行从表中删除，它的主键不能赋值给以后的新行）。

​    主键一般定义在表的一列上，但这并不是必须的，也可以一起使用多个列作为主键。在使用多个列作为主键时，上述条件必须应用到构成主键的所有列，所有列值的组合必须是唯一的（但单个列的值可以不唯一）。



## 1.2 什么是SQL

​	SQL称为结构化查询语言（Structured Query Language），SQL是一种专门用来与数据库通信的语言。

​	与其他语言（如Python、Golang这样的程序设计语言）不一样，SQL由很少的词组成，它有以下优点：

- SQL不是某个特定数据库供应商专有的语言，几乎所有重要的DBMS都支持SQL
- SQL简单易学
- SQL看似简单，实际是一种强有力的语言，灵活使用其语言元素，可以进行非常复杂和高级的数据库操作



## 1.3 动手实践

	### 1.3.1 场景

​	假想的玩具经销商使用的订单录入系统的组成部分，这些表用来完成以下几项任务：

- 管理供应商；
- 管理产品目录；
- 管理客户列表
- 录入客户订单。

### 1.3.2 表的描述

​		完成它们需要5个表，以下对每个表内的列名进行介绍。

- Vendors表：存储销售产品的供应商，每个供应商在这个表中有一个记录，供应商ID列（vend_id）用户产品与供应商的匹配。

  <center>表A-1 Vendors表的列</center>
| 列           | 说明             |
| ------------ | ---------------- |
| vend_id      | 唯一的供应商ID   |
| vend_name    | 供应商名称       |
| vend_address | 供应商地址       |
| vend_city    | 供应商城市       |
| vend_state   | 供应商的省       |
| vend_zip     | 供应商的邮政编码 |
| vend_country | 供应商的国家     |
|              |                  |

- 所有的表都应该有主键。这个表应该用vend_id作为它的主键。

Products表：包含产品目录，每行一个产品。每个产品有唯一的ID（prod_id），并借助vend_id（供应商表的唯一ID）与供应商相关联。

<center>表A-2 Products表的列</center>
| 列         | 说明                            |
| ---------- | ------------------------------- |
| prod_id    | 唯一的产品ID                    |
| vend_id    | 产品供应商ID（vendors.vend_id） |
| prod_name  | 产品名称                        |
| prod_price | 产品价格                        |
| prod_desc  | 产品描述                        |

- 所有表都应该有主键。这个表应该用prod_id作为它的主键。

- 为实施引用完整性，应该在vend_id上定义一个外键，关联它到vendors的vend_id列。

Customers表：Customers表存储所有客户信息。每个客户有唯一的ID（cust_id）。

<center>表A-3 Customers表的列</center>
| 列           | 说明           |
| ------------ | -------------- |
| cust_id      | 唯一的客户ID   |
| cust_name    | 客户名         |
| cust_address | 客户的地址     |
| cust_city    | 客户的城市     |
| cust_state   | 客户的省       |
| cust_zip     | 客户的邮政编码 |
| cust_country | 客户的国家     |
| cust_contact | 客户的联系名   |
| cust_email   | 客户的电子邮箱 |
|              |                |

- 所有表都应该有主键，这个表应该用cust_id作为他的主键。

Orders表：Orders表存储客户订单（非订单细节）。每个订单唯一地进行编号（order_num）。Orders表按cust_id列（Customers.cust_id）关联到相应的客户。

<center>表A-4 Orders表的列</center>
| 列         | 说明                            |
| ---------- | ------------------------------- |
| order_num  | 唯一的订单号                    |
| order_data | 订单日期                        |
| cust_id    | 订单客户ID（Customers.cust_id） |

- 所有表都应该有主键，这个表应该用order_num作为他的主键
- 为实施引用完整性，应该在cust_id上定义一个外键，关联它到Customers的cust_id列。

OrderIterms表：存储每个订单中的实际物品，每个订单的每个物品一行。对于Orders表的每一行，在OrderIterms表中便有一行或者多行。每个订单物品由订单号外加订单物品（第一个物品，第二个物品等）唯一标识。订单物品用order_num列（Orders.order_num）与其相应的订单关联。此外，每个订单物品包含该物品的产品ID（Products.prod_id）。

<center>表A-5 OrderIterms表的列</center>
| 列         | 说明                       |
| ---------- | -------------------------- |
| order_num  | 订单号(Orders.order_num)   |
| order_item | 订单物品号（订单内的顺序） |
| prod_id    | 产品ID（Products.prod_id） |
| quantity   | 产品数量                   |
| Item_price | 物品价格                   |

- 所有表都应该有主键，这个表应该用order_num和order_item作为它的主键。
- 为实施引用完整性，应该在order_num和prod_id上定义外键，关联order_num到Orders.order_num,关联prod_id到Products.prod_id列。



# 第二章 检索数据

​	主要内容介绍使用select语句从表中检索数据。

## 2.1 SELECT语句

- 关键字（keyword）作为SQL组成部分的保留字。关键字不能用做表或列的名字。要注意以下几点
- 关键字随不同的DBMS⽽变化，并⾮下⾯的所有关键字都被所有DBMS采⽤。
- 许多DBMS扩展了SQL保留字，使其包含专⻔⽤于实现的术语。多数DBMS专⽤的关键字未列在下⾯。
- 为保证以后的兼容性和可移植性，应避免使⽤这些保留字，即使它们不是你使⽤的DBMS的保留字。

## 2.2 检索单个列

输入：

```sql
SELECT prod_name FROM Products;
```

输出：

```sql
+---------------------+
| prod_name           |
+---------------------+
| Fish bean bag toy   |
| Bird bean bag toy   |
| Rabbit bean bag toy |
| 8 inch teddy bear   |
| 12 inch teddy bear  |
| 18 inch teddy bear  |
| Raggedy Ann         |
| King doll           |
| Queen doll          |
+---------------------+
```

- 提示：结束SQL语句需要使用`;`。多数DBMS不需要再单条SQL语句后面加分号，但也有DBMS可能必须在单条SQL语句后加上分号。
- 提示：SQL语句大小写，SQL语句不区分大小写，因此select与SELECT是相同的。
- 提示：使用空格，在处理SQL语句时，其中所有的空格都被忽略（单行和多行）。

## 2.3 检索多个列

​	如想查询多个列，需要在select后面给出多个列名，列名之间用`,`分隔。

- 提示：当心逗号，最后一列不需要`,`。

​    以下将从products中查询显示3个列

输入：

```sql
SELECT prod_id, prod_name, pord_price FROM Products;
```

输出：

```sql
+---------+---------------------+------------+
| prod_id | prod_name           | prod_price |
+---------+---------------------+------------+
| BNBG01  | Fish bean bag toy   | 3.49       |
| BNBG02  | Bird bean bag toy   | 3.49       |
| BNBG03  | Rabbit bean bag toy | 3.49       |
| BR01    | 8 inch teddy bear   | 5.99       |
| BR02    | 12 inch teddy bear  | 8.99       |
| BR03    | 18 inch teddy bear  | 11.99      |
| RGAN01  | Raggedy Ann         | 4.99       |
| RYL01   | King doll           | 9.49       |
| RYL02   | Queen doll          | 9.49       |
+---------+---------------------+------------+
```

# 2.4 检索所有列

​	select后面跟`*`则表示查询所有列。

输入：

```sql
SELECT * FROM Products;
```

输出：

```sql
+---------+---------+-----------------+------------------------+-------------------+
|                                                        |                         |
| prod_id | vend_id | prod_name | prod_price | prod_desc |                         |
| ------- | ------- | --------- | ---------- | --------- |                         |
|         |         |           |            |           |                         |
+---------+---------+----------------+--------------------------+------------------+
| BNBG01 | DLL01 | Fish bean bag toy   | 3.49  | Fish bean bag toy, complete with  | |bean bag worms with which to feed it                                              |
| ------ | ----- | ------------------- | ----- | -----------------------------------                                                           
| BNBG02 | DLL01 | Bird bean bag toy   | 3.49  | Bird bean bag toy, eggs are not   |    included                                                                           |
| ------ | ----- | ------------------- | ----  | -----------------------------------                                                           
| BNBG03 | DLL01 | Rabbit bean bag toy | 3.49  | Rabbit bean bag toy, comes with   | bean bag carrots                                                                   |
| ------ | ----- | ------------------- | ----  | -----------------------------------                                                          
| BR01   | BRS01 | 8 inch teddy bear   | 5.99  | 8 inch teddy bear, comes with cap | and jacket                                                                         |
| ----   | ----- | ------------------- | ----  | -----------------------------------
| BR02   | BRS01 | 12 inch teddy bear  | 8.99  | 12 inch teddy bear, comes with cap| and jacket                                                                         |
| ----   | ----- | ------------------- | ----  | -----------------------------------
| BR03   | BRS01 | 18 inch teddy bear  | 11.99 | 18 inch teddy bear, comes with cap| and jacket                                                                         |
| ----   | ----- | ------------------- | ----- | -----------------------------------
| RGAN01 | DLL01 | Raggedy Ann         | 4.99  | 18 inch Raggedy Ann doll          |                            
| ------ | ----- | ------------------- | ----  | ------------------------          |                           
| RYL01  | FNG01 | King doll           | 9.49  | 12 inch king doll with royal      | garments and crown                                                                 | 
| -----  | ----- | --------------------| ----  | -----------------------------------                                                          
| RYL02  | FNG01 | Queen doll          | 9.49  | 12 inch queen doll with royal     | garments and crown                                                                 |
| -----  | ----- | --------------------| ----  | -----------------------------------                                                              
+---------+---------+---------------------+------------+---------------------------+
```



警告：使用通配符，一般情况下，除非你需要表中的每一列，否则最好不要使用`*`通配符，因为会降低检索和应用程序的性能。

- 提示：检索未知列，使⽤通配符有⼀个⼤优点。由于不明确指定列名（因为星号检索每
  ⼀列），所以能检索出名字未知的列。

## 2.5 检索不同的值

​	如果不希望select返回的数据中某个值每次都出现，例如想要检索products表中所有产品供应商的ID

输入：

```sql
SELECT vend_id FROM Products
```

输出：

```sql
| vend_id |
+---------+
| BRS01   |
| BRS01   |
| BRS01   |
| DLL01   |
| DLL01   |
| DLL01   |
| DLL01   |
| FNG01   |
| FNG01   |
+---------+
```

selsct语句返回的9行数据（即使表中只有3个产品供应商），因为products表中有9中产品，这个时候就需要使用DISTINCT关键字（数据库只返回不同的值）

输入：

```sql
SELECT DISTINCT vend_id FROM Products;
```

输出：

```sql
+---------+
| vend_id |
+---------+
| BRS01   |
| DLL01   |
| FNG01   |
+---------+
```

- 分析：`SELECT DISTINCT vend_id`告诉DBMS只返回（具有唯一性）的`vend_id`行,如上输出，只有三行。如果使用`DISTINCT`关键字，它必须直接放在列名的前面。
- 警告：不能部分使用DISTINCT，DISTINCT关键字作用于所有的列，不仅仅是跟在其后面的那一列，你指定`SELECT DISTINCT vend_id, prod_price`,除非指定的两列完全相同，否则所有的航都会被检索出来。

## 2.6 限制结果

​	select语句返回指定表中所有匹配的行，如果只想返回第一行或者一定数量的行，需要带上指定的关键字，但是各种数据库中这一SQL实现并不相同。

- SQL Server：`SELECT TOP 5 prod_name FROM Products;`
- DB2：`SELECT prod_name FROM Products FETCH FIRST 5 ROWS ONLY;`
- Oracle：`SELECT prod_name FROM Products WHERE ROWNUM <=5;`
- MySQL、MariaDB、PostgreSQL、SQLite：`SELECT * FROM Products LIMIT 5;`

## 2.7 使用注释

​	SQL语句是由DBMS处理的指令，如果希望包括不进行处理和执行的文本，应该如何处理呢？

- `—-`、`#`：单行注释
- `/* …… */`：多行注释

## 2.8 小结

​	这⼀课学习了如何使⽤SQL的SELECT语句来检索单个表列、多个表列以及所有表列。你也学习了如何返回不同的值，如何注释代码。同时不幸的是，更复杂的SQL使得SQL代码变得不轻便。下⼀课将讲授如何对检索出来的数据进⾏排序。



# 第三章 排序检索数据

​	主讲SELECT语句和ORDER BY子句，根据需要排序检索出的数据。

## 3.1 排序数据

​	select默认返回的数据是没有排序的，数据一般将以它在底层中出现的顺序显示。

- 子句（clause）：SQL语句由子句构成，有些子句是必须的，有些则是可选的。一个子句通常由一个关键字加上所提供的数据组成。
- ORDER BY：order by子句取一个或多个列的名字，据此对输出进行排序

输入：

```sql
SELECT prod_name FROM Products ORDER BY prod_name
```

输出：

```sql
+---------------------+
| prod_name           |
+---------------------+
| 12 inch teddy bear  |
| 18 inch teddy bear  |
| 8 inch teddy bear   |
| Bird bean bag toy   |
| Fish bean bag toy   |
| King doll           |
| Queen doll          |
| Rabbit bean bag toy |
| Raggedy Ann         |
+---------------------+
```



- ORDER BY 子句的位置：在指定⼀条ORDER BY⼦句时，应该保证它是SELECT语句中最后⼀条⼦句。如果它不是最后的⼦句，将会出现错误消息。
- 通过非选择列进行排序：通常，ORDER BY⼦句中使⽤的列将是为显⽰⽽选择的列。但是，实际上并不⼀定要这样，⽤⾮检索的列排序数据是完全合法的。

## 3.2 按多个列排序

​	如果要检索出的数据根据不止一个列进行数据排序，在ORDER BY 关键字后面指定多个列名。

输入：

```sql
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price, prod_name;
```

输出：

```sql
+---------+------------+---------------------+
| prod_id | prod_price | prod_name           |
+---------+------------+---------------------+
| BNBG02  | 3.49       | Bird bean bag toy   |
| BNBG01  | 3.49       | Fish bean bag toy   |
| BNBG03  | 3.49       | Rabbit bean bag toy |
| RGAN01  | 4.99       | Raggedy Ann         |
| BR01    | 5.99       | 8 inch teddy bear   |
| BR02    | 8.99       | 12 inch teddy bear  |
| RYL01   | 9.49       | King doll           |
| RYL02   | 9.49       | Queen doll          |
| BR03    | 11.99      | 18 inch teddy bear  |
+---------+------------+---------------------+
```
- 对于上述例⼦中的输出，仅在多个⾏具有相同的prod_price值时才对产品按prod_name进⾏排序。如果prod_price列中所有的值都是唯⼀的，则不会按prod_name排序。

## 3.3 按列位置排序

​	除了能用列名指出排序顺序外，ORDER BY还支持按相对位置进行排序。

输入：

```
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY 2, 3;
```

输出：

```sql
+---------+------------+---------------------+
| prod_id | prod_price | prod_name           |
+---------+------------+---------------------+
| BNBG02  | 3.49       | Bird bean bag toy   |
| BNBG01  | 3.49       | Fish bean bag toy   |
| BNBG03  | 3.49       | Rabbit bean bag toy |
| RGAN01  | 4.99       | Raggedy Ann         |
| BR01    | 5.99       | 8 inch teddy bear   |
| BR02    | 8.99       | 12 inch teddy bear  |
| RYL01   | 9.49       | King doll           |
| RYL02   | 9.49       | Queen doll          |
| BR03    | 11.99      | 18 inch teddy bear  |
+---------+------------+---------------------+
```

## 3.4 指定排序方向

数据排序不限于升序排序（从A到Z），这只是默认的排序顺序。还可以使⽤ORDER BY⼦句进⾏降序（从Z到A）排序。为了进⾏降序排序，必须指定DESC关键字。

输入：

```sql
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price DESC;
```

输出：

```sql
+---------+------------+---------------------+
| prod_id | prod_price | prod_name           |
+---------+------------+---------------------+
| BR03    | 11.99      | 18 inch teddy bear  |
| RYL01   | 9.49       | King doll           |
| RYL02   | 9.49       | Queen doll          |
| BR02    | 8.99       | 12 inch teddy bear  |
| BR01    | 5.99       | 8 inch teddy bear   |
| RGAN01  | 4.99       | Raggedy Ann         |
| BNBG01  | 3.49       | Fish bean bag toy   |
| BNBG02  | 3.49       | Bird bean bag toy   |
| BNBG03  | 3.49       | Rabbit bean bag toy |
+---------+------------+---------------------+
```

- 最贵的排在最前面

​    如果需要用多个列排序（根据价格降序），在加上产品名称。

输入：

```sql
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price DESC, prod_name;
```

输出：

```sql
+---------+------------+---------------------+
| prod_id | prod_price | prod_name           |
+---------+------------+---------------------+
| BR03    | 11.99      | 18 inch teddy bear  |
| RYL01   | 9.49       | King doll           |
| RYL02   | 9.49       | Queen doll          |
| BR02    | 8.99       | 12 inch teddy bear  |
| BR01    | 5.99       | 8 inch teddy bear   |
| RGAN01  | 4.99       | Raggedy Ann         |
| BNBG02  | 3.49       | Bird bean bag toy   |
| BNBG01  | 3.49       | Fish bean bag toy   |
| BNBG03  | 3.49       | Rabbit bean bag toy |
+---------+------------+---------------------+
```

- 分析：DESC关键字只应⽤到直接位于其前⾯的列名。在上例中，只对prod_price列指定DESC，对prod_name列不指定。因此，prod_price列以降序排序，⽽prod_name列（在每个价格内）仍然按标准的升序排序。
- 警告：如果想在多个列上进⾏降序排序，必须对每⼀列指定DESC关键字。

## 3.5 小结

​	这⼀课学习了如何⽤SELECT语句的ORDER BY⼦句对检索出的数据进⾏排序。这个⼦句必须是SELECT语句中的最后⼀条⼦句。根据需要，可以利⽤它在⼀个或多个列上对数据进⾏排序。



# 第四章 过滤数据

​	这⼀课将讲授如何使⽤SELECT语句的WHERE⼦句指定搜索条件。

## 4.1 使用WHERE子句

​	数据库表⼀般包含⼤量的数据，很少需要检索表中的所有⾏。通常只会根据特定操作或报告的需要提取表数据的⼦集。只检索所需数据需要指定搜索条件（search criteria），搜索条件也称为过滤条件（filter condition）。

输入：

```sql
 SELECT prod_name, prod_price FROM Products WHERE prod_price = 3.49;
```

输出：

```sql
+---------------------+------------+
| prod_name           | prod_price |
+---------------------+------------+
| Fish bean bag toy   | 3.49       |
| Bird bean bag toy   | 3.49       |
| Rabbit bean bag toy | 3.49       |
+---------------------+------------+
```

- 提示：SQL过滤与应用过滤，数据也可以在应⽤层过滤。为此，SQL的SELECT语句为客⼾端应⽤检索出超过实际所需的数据，然后客⼾端代码对返回数据进⾏循环，提取出需要的⾏。通常，这种做法极其不妥。优化数据库后可以更快速有效地对数据进⾏过滤。⽽让客⼾端应⽤（或开发语⾔）处理数据库的⼯作将会极⼤地影响应⽤的性能，并且使所创建的应⽤完全不具备可伸缩性。此外，如果在客⼾端过滤数据，服务器不得不通过⽹络发送多余的数据，这将导致⽹络带宽的浪费。
- 警告，WHERE子句的位置：在同时使⽤ORDER BY和WHERE⼦句时，应该让ORDER BY位于WHERE之后，否则将会产⽣错误。

## 4.2 WHERE子句操作符

​	以下列出WHERE子句所支持的操作符：

<center>表4-1 WHERE 语句操作符</center>
| 操作符  | 说明               |
| ------- | ------------------ |
| =       | 等于               |
| <>      | 不等于             |
| !=      | 不等于             |
| <       | 小于               |
| <=      | 小于等于           |
| !<      | 不小于             |
| >       | 大于               |
| >=      | 大于等于           |
| !>      | 不大于             |
| BETWEEN | 在指定的两个值之间 |
| IS NULL | 为NULL值           |
|         |                    |

### 4.2.1 检查单个值

- 例：列出所有价格小于10美元的产品

```sql
SELECT prod_name, prod_price FROM Products WHERE prod_price <= 10;
```

```sql
+---------------------+------------+
| prod_name           | prod_price |
+---------------------+------------+
| Fish bean bag toy   | 3.49       |
| Bird bean bag toy   | 3.49       |
| Rabbit bean bag toy | 3.49       |
| 8 inch teddy bear   | 5.99       |
| 12 inch teddy bear  | 8.99       |
| Raggedy Ann         | 4.99       |
| King doll           | 9.49       |
| Queen doll          | 9.49       |
+---------------------+------------+
```

### 4.2.2 不匹配检查

- 列出供应商不是DLL01制造的商品。

```SQL
SELECT vend_id, prod_name FROM Products WHERE vend_id <> "DLL01";
```

```SQL
+---------+--------------------+
| vend_id | prod_name          |
+---------+--------------------+
| BRS01   | 8 inch teddy bear  |
| BRS01   | 12 inch teddy bear |
| BRS01   | 18 inch teddy bear |
| FNG01   | King doll          |
| FNG01   | Queen doll         |
+---------+--------------------+
```

- 警告：是!=还是<>?,!=和<>通常可以互换。但是，并⾮所有DBMS都⽀持这两种不等于操作符。例如，Microsoft Access⽀持<>⽽不⽀持!=。如果有疑问，请参阅相应的DBMS⽂档。

### 4.2.3 范围值检查

- 例：检索价格在5美元和10美元之间的所有产品：

  ```SQL
  SELECT prod_name, prod_price FROM Products WHERE prod_price BETWEEN 5 AND 10;
  ```

  ```SQL
  +--------------------+------------+
  | prod_name          | prod_price |
  +--------------------+------------+
  | 8 inch teddy bear  | 5.99       |
  | 12 inch teddy bear | 8.99       |
  | King doll          | 9.49       |
  | Queen doll         | 9.49       |
  +--------------------+------------+
  ```

- 在使⽤BETWEEN时，必须指定两个值⸺所需范围的低端值和⾼端值。这两个值必须⽤AND关键字分隔。BETWEEN匹配范围中所有的值，包括指定的开始值和结束值。

### 4.2.4 控制检查

​	在创建表时，表设计人员可以指定其中的列能否不包含值。在一个列不包含值时，称其包含控制NULL。

- NULL（no value）,它与字段包含0、空字符串或仅仅包含空格不同。

- 确定值是否为NULL，不能简单地检查是否= NULL。SELECT语句有⼀个特殊的WHERE⼦句，可⽤来检查具有NULL值的列。这个WHERE⼦句就是IS NULL⼦句。其语法如下：

  ```sql
  SELECT cust_name FROM Customers WHERE cust_email IS NULL;
  ```

  ```sql
  +---------------+
  | cust_name     |
  +---------------+
  | Kids Place    |
  | The Toy Store |
  +---------------+
  ```

## 4.3 小结

​	这⼀章介绍了如何⽤SELECT语句的WHERE⼦句过滤返回的数据。我们学习了如何检验相等、不相等、⼤于、⼩于、值的范围以及NULL值等。



# 第五章 高级数据过滤

​	这⼀章讲授如何组合WHERE⼦句以建⽴功能更强、更⾼级的搜索条件。学习如何使⽤NOT和IN操作符。

## 5.1 组合WHERE子句

​	使用WHERE子句时增加多个条件过滤数据。

- 操作符（operator），用来联结或改变WHERE子句的子句的关键字，也称为**逻辑操作符**（logical operator）。

### 5.1.1 AND操作符

​	通过增加条件过滤数据，可以使用AND操作符给WHERE子句附加条件。

- 例：检索由供应商”DLLO1“制造且价格小于等于4美元的所有产品名称和价格。

  ```sql
  SELECT prod_id, prod_name, prod_price FROM Products WHERE vend_id = "DLL01" AND prod_price <= 4;
  ```

  ```sql
  +---------+---------------------+------------+
  | prod_id | prod_name           | prod_price |
  +---------+---------------------+------------+
  | BNBG01  | Fish bean bag toy   | 3.49       |
  | BNBG02  | Bird bean bag toy   | 3.49       |
  | BNBG03  | Rabbit bean bag toy | 3.49       |
  +---------+---------------------+------------+
  ```

  

### 5.1.2 OR操作符

​	OR操作符与AND操作符正好相反，它指⽰DBMS检索匹配任⼀条件的⾏。事实上，许多DBMS在OR WHERE⼦句的第⼀个条件得到满⾜的情况下，就不再计算第⼆个条件了（在第⼀个条件满⾜时，不管第⼆个条件是否满⾜，相应的⾏都将被检索出来）。

- 例：检索由任⼀个指定供应商制造的所有产品的产品名和价格。

  ```SQL
  SELECT prod_name, prod_price FROM Products WHERE vend_id = "DLL01" OR vend_id = "BRS01";
  ```

  ```SQL
  +---------------------+------------+
  | prod_name           | prod_price |
  +---------------------+------------+
  | 8 inch teddy bear   | 5.99       |
  | 12 inch teddy bear  | 8.99       |
  | 18 inch teddy bear  | 11.99      |
  | Fish bean bag toy   | 3.49       |
  | Bird bean bag toy   | 3.49       |
  | Rabbit bean bag toy | 3.49       |
  | Raggedy Ann         | 4.99       |
  +---------------------+------------+
  ```

- OR：WHERE⼦句中使⽤的关键字，⽤来表⽰检索匹配任⼀给定条件的⾏。

### 5.1.3 求值顺序

​	WHERE⼦句可以包含任意数⽬的AND和OR操作符。允许两者结合以进⾏复杂、⾼级的过滤。

- SQL（像多数语⾔⼀样）在处理OR操作符前，优先处理AND操作符。

  ```sql
  SELECT vend_id, prod_name, prod_price FROM Products WHERE vend_id = "DLL01" OR vend_id = "BRS01" AND prod_price >= 10;
  ```

  ```sql
  +---------+---------------------+------------+
  | vend_id | prod_name           | prod_price |
  +---------+---------------------+------------+
  | BRS01   | 18 inch teddy bear  | 11.99      |
  | DLL01   | Fish bean bag toy   | 3.49       |
  | DLL01   | Bird bean bag toy   | 3.49       |
  | DLL01   | Rabbit bean bag toy | 3.49       |
  | DLL01   | Raggedy Ann         | 4.99       |
  +---------+---------------------+------------+
  ```

  当SQL看到上述WHERE⼦句时，它理解为：由供应商BRS01制造的价格为10美元以上的所有产品，以及由供应商DLL01制造的所有产品，⽽不管其价格如何。换句话说，由于AND在求值过程中优先级更⾼，操作符被错误地组合了。

  如果要解决这个问题就需要加入括号对操作符进行明确的分组，如：

  ```sql
  SELECT vend_id, prod_name, prod_price FROM Products WHERE (vend_id = "DLL01" OR vend_id = "BRS01") AND prod_price >= 10;
  ```

  ```sql
  +---------+--------------------+------------+
  | vend_id | prod_name          | prod_price |
  +---------+--------------------+------------+
  | BRS01   | 18 inch teddy bear | 11.99      |
  +---------+--------------------+------------+
  ```

  - 提⽰：在WHERE⼦句中使⽤圆括号，任何时候使⽤具有AND和OR操作符的WHERE⼦句，都应该使⽤圆括号明确地分组操作符。不要过分依赖默认求值顺序，即使它确实如
    你希望的那样。使⽤圆括号没有什么坏处，它能消除歧义。

## 5.2 IN操作符

​	IN操作符⽤来指定条件范围，范围中的每个条件都可以进⾏匹配。IN取⼀组由逗号分隔、括在圆括号中的合法值。

- 例：检索由供应商DLL01和BRS01制造的所有产品。

  ```SQL
  SELECT prod_name, prod_price FROM Products WHERE vend_id IN ("DLL01", "BRS01");
  ```

  ```SQL
  +---------------------+------------+
  | prod_name           | prod_price |
  +---------------------+------------+
  | 8 inch teddy bear   | 5.99       |
  | 12 inch teddy bear  | 8.99       |
  | 18 inch teddy bear  | 11.99      |
  | Fish bean bag toy   | 3.49       |
  | Bird bean bag toy   | 3.49       |
  | Rabbit bean bag toy | 3.49       |
  | Raggedy Ann         | 4.99       |
  +---------------------+------------+
  ```

  - IN操作符优点
    - 再有很多合法选项时，IN操作符的预发更清楚、直观。
    - 在与其它AND和OR操作符组合使用IN时，求值顺序更容易管理。
    - IN操作符一般比一组OR操作符执行更快
    - IN的最大优点是可以包含其他SELECT语句，能够更动态地建立WHERE子句。
  - IN：WHERE⼦句中⽤来指定要匹配值的清单的关键字，功能与OR相当。

## 5.3 NOT操作符

​	WHERE⼦句中的NOT操作符有且只有⼀个功能，那就是否定其后所跟的任何条件。

- NOT：WHERE子句中用来否定其后条件的关键字。

- 例：列出除DLL01之外的所有供应商制造的产品。

  ```sql
  SELECT prod_name, vend_id, prod_price FROM Products WHERE NOT vend_id = "DLL01";
  ```

  ```sql
  SELECT prod_name, vend_id, prod_price FROM Products WHERE vend_id <> "DLL01";
  ```

  ```sql
  +--------------------+---------+------------+
  | prod_name          | vend_id | prod_price |
  +--------------------+---------+------------+
  | 8 inch teddy bear  | BRS01   | 5.99       |
  | 12 inch teddy bear | BRS01   | 8.99       |
  | 18 inch teddy bear | BRS01   | 11.99      |
  | King doll          | FNG01   | 9.49       |
  | Queen doll         | FNG01   | 9.49       |
  +--------------------+---------+------------+
  ```

## 5.4 小结

​	这⼀章讲授如何⽤AND和OR操作符组合成WHERE⼦句，还讲授了如何 明确地管理求值顺序，如何使⽤IN和NOT操作符。

# 第六章 用通配符进行过滤

​	这⼀章介绍什么是通配符、如何使⽤通配符以及怎样使⽤LIKE操作符 进⾏通配搜索，以便对数据进⾏复杂过滤。

## 6.1 LIKE操作符

​	针对未知值进行过滤。

- 通配符（wildcard）：用来匹配值的一部分的特殊字符。
- 搜索模式（search patterm）：由字面值、通配符或两者组合构成的搜索条件。

通配符是SQL的WHERE子句中有特殊含义的字符，SQL支持几种通配符。为在搜索子句中使用通配符，必须使用LIKE操作符。LIKE只是DBMS，后跟的搜索模式利用通配符而匹配而不是简单的相等匹配进行比较



### 6.1.1 百分号（%）通配符

​	最常用的通配符是百分号（%）。在搜索串中，%表示任何字符出现任意次数。

- 例：找出所有以单词Fish开头的产品

``` sql
SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE "Fish%";
```

```sql
+---------+-------------------+
| prod_id | prod_name         |
+---------+-------------------+
| BNBG01  | Fish bean bag toy |
+---------+-------------------+
```

- 例：根据部分信息搜索电子邮件地址

```sql
SELECT cust_contact, cust_email FROM Customers WHERE cust_email LIKE "s%@%.com";
```

```sql
+--------------+-----------------------+
| cust_contact | cust_email            |
+--------------+-----------------------+
| John Smith   | sales@villagetoys.com |
+--------------+-----------------------+
```



### 6.1.2 下划线（_）通配符

​	与%用途一样，但它只匹配单个字符，而不是多个字符。

- 例：根据产品名称匹配

``` sql
SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '__ inch teddy bear';
```

``` sql
+---------+--------------------+
| prod_id | prod_name          |
+---------+--------------------+
| BR02    | 12 inch teddy bear |
| BR03    | 18 inch teddy bear |
+---------+--------------------+
```

这个WHERE⼦句中的搜索模式给出了后⾯跟有⽂本的两个通配符。结 果只显⽰匹配搜索模式的⾏：第⼀⾏中下划线匹配12，第⼆⾏中匹配 18。8 inch teddy bear产品没有匹配，因为搜索模式要求匹配两 个通配符⽽不是⼀个。



### 6.1.3 方括号（[]）通配符

​	指定一个字符集，必须匹配指定位置（通配符的位置）的一个字符。

- 说明：并不是所有的DBMS都支持用来创建集合的[]，只有微软的Access和SQL Server支持集合。
- 例：找出所有名字以J或者M起头的联系人

```sql
SELECT cust_contact FROM Customers WHERE cust_contact LIKE "[JM]%" ORDER BY cust_contact;
```

​	使用的是MySQL，所以未返回任何数据，因为不支持。



## 6.2 使用通配符的技巧

​	SQL的通配符搜索一般比前面讨论的其他搜索要消耗更长的处理时间，以下给出以下使用通配符时要记住的技巧

- 不要过度使用通配符。如果其他的操作符能达到相同的目的，应该使用其他操作符
- 在确定需要使用通配符时，尽量不要把它们用在搜索模式的开始处，搜索起来是最慢的
- 仔细注意通配符的位置。若放错位置可能不会返回想要的数据



## 6.3 小结

​	这一章介绍了什么事通配符，如何在WHERE子句中使用SQL通配符。



# 第七章 创建计算字段

​	这一章介绍什么事计算字段，如何创建以及如何从应用程序中使用别名引用它们。



## 7.1 计算字段

​	存储在数据库表中的数据一般不是应用程序所需要的格式。

- 例：需要显示公司名，同时还要显示公司的地址，但是这两个信息不再同一张表里。
- 城市、州、邮政编码存储在不同的列中，但邮件标签打印程序需要把他们作为一个有恰当格式的字段检索出来。
- 列数据是大小写混合的，但报表程序需要把所有数据按大写表示出来。
- 物品订单表存储物品的价格和数量，不存储每个物品的总价和（价格*数量）。但为打印发票需要物品的总价格。
- 需要根据表数据进行诸如总数、平均数的计算。

以上例子中，存储在表中的数据都无法直接满足应用程序。我们需要直接从数据库中检索出转换、计算或格式化过的数据，而不是检索出数据，然后再在客户端应用程序中重新格式化。这时候就需要计算字段了，计算的字段并不实际存在与数据库表中。计算字段是运行时在SELECT语句中创建的。



- 字段（field）
  - 基本上与列（column）的意思相同，经常互换使用，不过数据库列一般称为列，而术语字段通常与计算字段一起使用。

- 提示：客户端与服务器的格式
  - 在SQL语句中可以完成的许多转换和格式化工作都可以直接在客户端应用程序内完成。但一般来说，在数据库服务器上完成这些操作币在客户端中完成要快得多。



## 7.2 拼接字段

​	创建由两列组成的标题。

Vendors表包含供应商名和地址信息。假如要生成一个供应商报表，需要在格式化的名称（位置）中列出供应商的位置。

- 拼接（concatenate）
  - 将值连接在一起（将一个值附加到另外一个值）构成单个值。

解决方式是把两个列拼接起来。在SQL中的SELECT语句中，可使用一个特殊的操作符来拼接两个值。根据所使用的的DBMS，此操作符可以用加号（+）或者竖杠（||）表示。在MySQL和MariaDB中，必须使用特殊函数。

- 说明：+还是||？

  - Access和SQL Server使⽤+号。DB2、Oracle、PostgreSQL、 SQLite和Open Office Base使⽤||。**MySQL则是使用Contact()函数来实现**。详细请参阅具体的DBMS⽂档。

- ```sql
  # 查询产品名称和产地
  SELECT Concat(vend_name, '(', vend_country, ')') FROM Vendors ORDER BY vend_name;
  ```

  ```sql
  +-------------------------------------------+
  | Concat(vend_name, '(', vend_country, ')') |
  +-------------------------------------------+
  | Bear Emporium(USA)                        |
  | Bears R Us(USA)                           |
  | Doll House Inc.(USA)                      |
  | Fun and Games(England)                    |
  | Furball Inc.(USA)                         |
  | Jouets et ours(France)                    |
  +-------------------------------------------+
  ```

  - RTrim()：删除数据右侧多余的空格
  - LTRIM()：删除数据左侧多余的空格
  - TRim()：删除两边的空格

  ```sql
  SELECT Concat(RTrim(vend_name), '(', LTrim(vend_country), ')') FROM Vendors ORDER BY vend_name;
  ```

  ```sql
  +---------------------------------------------------------+
  | Concat(RTrim(vend_name), '(', LTrim(vend_country), ')') |
  +---------------------------------------------------------+
  | Bear Emporium(USA)                                      |
  | Bears R Us(USA)                                         |
  | Doll House Inc.(USA)                                    |
  | Fun and Games(England)                                  |
  | Furball Inc.(USA)                                       |
  | Jouets et ours(France)                                  |
  +---------------------------------------------------------+
  ```



**使用别名**

SELECT可以很好地拼接字段。但是这个拼接而成的列没有名字。为了解决这个问题可以使用SQL的别名（alias），别名用AS关键字赋予。

例：

```sql
SELECT Concat(vend_name, '(', vend_country, ')') AS vend_title FROM Vendors ORDER BY vend_name;
```

```sql
+------------------------+
| vend_title             |
+------------------------+
| Bear Emporium(USA)     |
| Bears R Us(USA)        |
| Doll House Inc.(USA)   |
| Fun and Games(England) |
| Furball Inc.(USA)      |
| Jouets et ours(France) |
+------------------------+
```

- 说明：AS通常可选
  - 在很多DBMS中，AS关键字是可选的，不过最好使用它。
- 提示：别名的其他用途
  - 常见的包括在表列名包含不合法的字符（如空格）时重新命名它，在原来的名字含混或容易误解时扩充它。
- 警告：别名
  - 既可以是一个单词也可以是一个字符串。如果是后者字符串应该在括号里。虽然这种做法是合法的，但不建议这么去做。多单词的别名可读性高，不过会给客户端应用带来各种问题。因此，别名最常见的使用是将多个单词的列名重命名为一个单词的名字。
- 说明：导出列
  - 别名又是也称为导出列（derived column），不管怎么叫，他们所代表的是相同的东西。



## 7.3 执行算数计算

​	计算字段的另一常见用途是对检索出的数据进行算数计算。

- 例：Orders表包含收到的所有订单，OrderItems表包含每个订单中的各个物品，查询订单号为20008的所有物品

  ```sql
  SELECT prod_id, quantity, item_price FROM OrderItems WHERE order_num = 20008;
  ```

  ```sql
  +---------+----------+------------+
  | prod_id | quantity | item_price |
  +---------+----------+------------+
  | RGAN01  |        5 | 4.99       |
  | BR03    |        5 | 11.99      |
  | BNBG01  |       10 | 3.49       |
  | BNBG02  |       10 | 3.49       |
  | BNBG03  |       10 | 3.49       |
  +---------+----------+------------+
  ```

  Item_price列包含订单中每项物品的单价。如下汇总物品的总价（单价*数量）

  ```sql
  SELECT prod_id, quantity, item_price, quantity*item_price AS expanded_price FROM OrderItems WHERE order_num = 20008;
  ```

  ```sql
  +---------+----------+------------+----------------+
  | prod_id | quantity | item_price | expanded_price |
  +---------+----------+------------+----------------+
  | RGAN01  |        5 | 4.99       | 24.95          |
  | BR03    |        5 | 11.99      | 59.95          |
  | BNBG01  |       10 | 3.49       | 34.90          |
  | BNBG02  |       10 | 3.49       | 34.90          |
  | BNBG03  |       10 | 3.49       | 34.90          |
  +---------+----------+------------+----------------+
  ```

  SQL支持表7-1中列出的基本算术操作符。此外，圆括号可以用来区分优先顺序。
  
  <center>表7-1算术操作符</center>
  | 操作符 | 说明 |
  | ------ | ---- |
  | +      | 加   |
  | -      | 减   |
  | *      | 乘   |
  | /      | 除   |
  |        |      |
  
- 提示：如何测试计算

  - SELECT语句为测试、检验函数和计算提供了很好的方法。虽然SELECT通常用语从表中检索数据，但是省略了FROM子句后就是简单的访问和处理表达式，例如SELECT 4 * 4;将返回16，SELECT Trim("    abc  ");将返回abc。使用Now()函数将返回当前日期和时间。

## 7.4 小结

​	这一章介绍了计算字段以及如何创建计算字段。此外，还讲述了如何创建和使用别名，一遍应用程序能引用计算字段。



# 第八章 使用数据处理函数

​	这一章介绍什么是函数，DBMS支持何种函数，以及如何使用这些函数；还讲解为什么SQL函数的使用可能会带来问题。



## 8.1 函数

​	与几乎所有DBMS都等同地支持SQL语句（如SELECT）不同，每一个DBMS都有特定的函数。实际上只有少数几个函数被所有主要的DBMS等同地支持。虽然所有类型的函数一般都可以在每个DBMS中使用，但各个函数的名称和语法可能极其不同。一下表8-1列出了3个常用函数及其在各个DBMS中的语法

<center>表8-1 DBMS函数的差异</center>
| 函数                 | 语法                                                         |
| -------------------- | ------------------------------------------------------------ |
| 提取字符串的组成部分 | Access使⽤MID()；DB2、Oracle、PostgreSQL和SQLite使⽤SUBSTR()；MySQL和SQL Server使⽤SUBSTRING() |
| 数据类型转换         | Access和Oracle使⽤多个函数，每种类型的转换有⼀个函数；DB2和PostgreSQL使⽤CAST()；MariaDB、MySQL和SQL Server使⽤CONVERT() |
| 取当前日期           | Access使⽤NOW()；DB2和PostgreSQL使⽤CURRENT_DATE；MariaDB和MySQL使⽤CURDATE()；Oracle使⽤SYSDATE；SQLServer使⽤GETDATE()；SQLite使⽤DATE(); |
|                      |                                                              |

- 可以看到，与SQL语句不⼀样，SQL函数不是可移植的。这表⽰为特 定SQL实现编写的代码在其他实现中可能不正常。

- 可移植（portable）
  - 所编写的代码可以再多个系统上运行。



## 8.2 使用函数

​	大多数SQL实现支持以下类型的函数。

- 用于处理文本字符串（如删除或填充值，转换值为大写或者小写）的文本函数。
- 用于在数值数据上进行算术操作（如返回绝对值，进行代数运算）的数值函数。
- 用于处理日期和时间值并从这些值中提取特定成分（如返回两个日期之差、检查日期有效性）的日期和时间函数。
- 返回DBMS正使用的特殊信息（如返回用户登录信息）的系统函数



### 8.2.1 文本处理函数

​	之前介绍过去除列值空格的函数（TRim、LTRim、RTrim）。以下介绍UPPER()函数

```sql
# UPPER() 将文本转换为大写
SELECT vend_name, UPPER(vend_name) AS vend_name_upcase FROM Vendors ORDER BY vend_name;
```

```sql
+-----------------+------------------+
| vend_name       | vend_name_upcase |
+-----------------+------------------+
| Bear Emporium   | BEAR EMPORIUM    |
| Bears R Us      | BEARS R US       |
| Doll House Inc. | DOLL HOUSE INC.  |
| Fun and Games   | FUN AND GAMES    |
| Furball Inc.    | FURBALL INC.     |
| Jouets et ours  | JOUETS ET OURS   |
+-----------------+------------------+
```

表8-2列出了一些常用的文本处理函数。

<center>表8-2 常用文本处理函数</center>
| 函数                                | 说明                    |
| ----------------------------------- | ----------------------- |
| LEFT()(或使用子字符串函数)          | 返回字符串左边的字符    |
| LENGTH()(也使用DATALENGTH()或LEN()) | 返回字符串的长度        |
| LOWER()(ACCESS使用LCASE())          | 将字符串转换为小写      |
| TRIM()                              | 去除字符串两边的空格    |
| LTRIM()                             | 去除字符串左边的空格    |
| RTRIM()                             | 去除字符串右边的空格    |
| SOUNDEX()                           | 返回字符串的SOUNDEX的值 |
| UPPER(Access使用UCASE())            | 将字符串转换为大写      |
| RIGHT()(或使用子字符串函数)         | 返回字符串右边的字符    |
|                                     |                         |

### 8.2.2 日期和时间处理函数

- 例：Orders表中包含的订单都带有订单日期，在MySQL中检索2020年所有订单

```sql
SELECT * FROM Orders WHERE YEAR(order_date) = '2020';
SELECT * FROM Orders WHERE LEFT(order_date, 4) = '2020';
```

```sql
+-----------+---------------------+------------+
| order_num | order_date          | cust_id    |
+-----------+---------------------+------------+
|     20005 | 2020-05-01 00:00:00 | 1000000001 |
|     20006 | 2020-01-12 00:00:00 | 1000000003 |
|     20007 | 2020-01-30 00:00:00 | 1000000004 |
|     20008 | 2020-02-03 00:00:00 | 1000000005 |
|     20009 | 2020-02-08 00:00:00 | 1000000001 |
+-----------+---------------------+------------+
```



### 8.2.3 数值处理函数

<center>表8-3 常用数值处理函数</center>
| 函数   | 说明   |
| ------ | ------ |
| ABS()  | 绝对值 |
| COS()  | 余弦   |
| EXP()  | 指数值 |
| PI()   | 圆周率 |
| SIN()  | 正弦   |
| SQRT() | 平方根 |
| TAN()  | 正切   |
|        |        |

## 8.3 小结

​	这一章介绍如何使用SQL的数据处理函数。



# 第九章 汇总数据

​	这一章介绍什么事SQL的聚集函数，如何利用它们汇总表的数据。

## 9.1 聚集函数

​	我们需要汇总数据而不需要具体的数据，为此SQL提供了专门的函数。使用这些函数，SQL查询可用于检索数据，以便分析和报表生成。以满足以下场景

- 确定表中的行数（或者满足某个条件或包含每个特定值的行数）。
- 获得表中某些行的和。
- 找出表列（或所有行或某些特定的行）的最大值、最小值、平均值。

为方便该类数据的检索，SQL给出了5个聚集函数。见表9-1

- 聚集函数（aggregate function）
  - 对某些行允许的函数，计算并返回一个值。

<center>表9-1 SQL聚集函数</center>
| 函数                     | 说明         |
| ------------------------ | ------------ |
| AVG()                    | 某列的平均值 |
| COUNT()                  | 某列的行数   |
| MAX()                    | 某列的最大值 |
| MIN()                    | 某列的最小值 |
| SUM()                    | 某列值的和   |
| 以下说明各个函数的使用。 |              |



### 9.1.1 AVG()函数

​	AVG()通过对表中行数计算并计算其列值之和，求得该列的平均值。可用来返回所有列的平均值，也可返回指定列或行的平均值。

- 例：返回Products表中所有产品的平均价格

- ```sql
  SELECT AVG(prod_price) AS avg_price FROM Products;
  ```

  ```sql
  +-----------+
  | avg_price |
  +-----------+
  | 6.823333  |
  +-----------+
  ```

- 例：返回Products表中指定供应商产品的平均价格

- ```sql
  ELECT AVG(prod_price) AS avg_price FROM Products WHERE vend_id = "DLL01";
  ```

  ```sql
  +-----------+
  | avg_price |
  +-----------+
  | 3.865000  |
  +-----------+
  ```

- 警告：只用于单个列

  - AVG()只能用来确定特定数值列的平均值，而且列名必须作为函数的参数给出，为了货的多个列的平均值，必须使用多个AVG()函数。

- 说明：NULL值

  - AVG()函数忽略列值为NULL的行。



### 9.1.2 COUNT()函数

​	COUNT()函数进行计数，可利用COUNT（）确定表中行的数目或者符合特定条件的行的数目。

COUNT()函数有两只使用方式：

- 使用COUNT(*)对表中行的数目进行计数，不管表列中包含的是空值还是非空值；
- 使用COUNT(columnn)对特定列中具有值具有值的行进行计数，忽略NULL值;

- 例：返回Customers表中顾客的总数

- ```sql
  SELECT COUNT(*) FROM Customers;
  ```

  ```sql
  +----------+
  | COUNT(*) |
  +----------+
  |        5 |
  +----------+
  ```

  

- 例：返回具有电子邮件地址的客户总数

- ```sql
  SELECT COUNT(cust_email) FROM Customers;
  ```

  ```sql
  +-------------------+
  | COUNT(cust_email) |
  +-------------------+
  |                 3 |
  +-------------------+
  ```

- 这条SELECT语句使⽤COUNT(cust_email)对cust_email列中有 值的⾏进⾏计数。在此例⼦中，cust_email的计数为3（表⽰5个顾 客中只有3个顾客有电⼦邮件地址）。 

- 说明：NULL值

  - 如果指定列名，则COUNT()函数会忽略指定列的值为空的⾏，但如 果COUNT()函数中⽤的是星号（*），则不忽略。



### 9.1.3 MAX()函数

​	返回指定列中的最大值。需要指定列名。

- 例：返回Products表中价格最高的产品价格

- ```sql
  SELECT MAX(prod_price) FROM Products;
  ```

  ```sql
  +-----------------+
  | MAX(prod_price) |
  +-----------------+
  | 11.99           |
  +-----------------+
  ```

  - 提示：对非数值数据使用MAX()
    - 虽然MAX()⼀般⽤来找出最⼤的数值或⽇期值，但许多（并⾮所 有）DBMS允许将它⽤来返回任意列中的最⼤值，包括返回⽂本列 中的最⼤值。在⽤于⽂本数据时，MAX()返回按该列排序后的最后 ⼀⾏。
  - 说明：NULL值
    - MAX()函数忽略值为NULL的行。

### 9.1.4 MIN()函数

​	MIN()的功能正好与MAX()相反，返回指定列最小值。

- 例：返回Products表中价格最低的产品价格

- ```sql
  SELECT MIN(prod_price) FROM Products;
  ```

  ```sql
  +-----------------+
  | MIN(prod_price) |
  +-----------------+
  | 3.49            |
  +-----------------+
  ```

  - 提示：对非数值数据使用MIN()
    - 虽然MIN()⼀般⽤来找出最⼤的数值或⽇期值，但许多（并⾮所 有）DBMS允许将它⽤来返回任意列中的最⼤值，包括返回⽂本列 中的最⼤值。在⽤于⽂本数据时，MIN()返回按该列排序后的最前面 ⼀⾏。

  - 说明：NULL值
    - MIN()函数忽略值为NULL的行。



### 9.1.5 SUM()函数

​	返回指定列值的和（总计）。

- 例：OrderItems包含订单中实际的物品，每个物品由相应的数量。返回所订购物品的总数（quantity值之和）。

- ```SQL
  SELECT SUM(quantity) AS 'items_orderd' FROM OrderItems WHERE order_num = 20005;
  ```

- ```sql
  +--------------+
  | items_orderd |
  +--------------+
  | 200          |
  +--------------+
  ```

- 例：返回订单商品总价

- ```SQL
  SELECT SUM(quantity*item_price) AS 'total_price' FROM OrderItems WHERE order_num = 20005;
  ```

  ```sql
  +-------------+
  | total_price |
  +-------------+
  | 1648.00     |
  +-------------+
  ```

  - 提示：在多个列上进行计算
    - 如本例所示，利用标准的算数操作符，所有聚集函数都可用来执行多个列上的计算。
  - 说明：NULL值
    - SUM()函数忽略列值为NULL的行。



## 9.2 聚集不同值

​	以上5个聚集函数都可以如下使用：

- 对所有行执行计算，指定ALL参数或不指定参数。
- 只包含不同的值，指定DISTINCT参数。

- 提示：ALL为默认

  - ALL参数不需要指定，因为他是默认行为，如果不指定DISTINCT，则假定为ALL。

- 例：返回特定供应商提供的产品的平均价格

- ```sql
  SELECT AVG(prod_price) AS "avg_price" FROM Products WHERE vend_id = 'DLL01';
  ```

- ```SQL
  +-----------+
  | avg_price |
  +-----------+
  | 3.865000  |
  +-----------+
  ```

- ```SQL
  # 使用了DISTINCT，只返回不同价格商品的平均价格
  SELECT AVG(DISTINCT prod_price) AS "avg_price" FROM Products WHERE vend_id = 'DLL01';
  ```

- ```sql
  +-----------+
  | avg_price |
  +-----------+
  | 4.240000  |
  +-----------+
  ```

- 警告：DISTINCT不能用于COUNT(*)

  - 如果指定列名，则DISTINCT只能用于COUNT()。DISTINCT不用用于COUNT(*),类似的，DISTINCT必须使用列名，不能用于计算或者表达式。

- 提⽰：将DISTINCT⽤于MIN()和MAX()

  - 虽然DISTINCT从技术上可⽤于MIN()和MAX()，但这样做实际上 没有价值。⼀个列中的最⼩值和最⼤值不管是否只考虑不同值，结 果都是相同的。



## 9.3 组合聚集函数

​	组合使用多个聚集函数返回对应数据。

- 例：执行4个聚集计算，返回4个值（Products中物品的数目，产品价格的最高值、最低值以及平均值）

- ```sql 
  SELECT COUNT(*) AS num_items, MIN(prod_price) AS price_min, MAX(prod_price) AS price_max, AVG(prod_price) AS price_avg FROM Products;
  ```

  ```sql
  +-----------+-----------+-----------+-----------+
  | num_items | price_min | price_max | price_avg |
  +-----------+-----------+-----------+-----------+
  |         9 | 3.49      | 11.99     | 6.823333  |
  +-----------+-----------+-----------+-----------+
  ```

- 警告：取别名

  - 在指定别名以包含某个聚集函数的结果时，不应该使⽤表中实际的 列名。虽然这样做也算合法，但许多SQL实现不⽀持，可能会产⽣ 模糊的错误消息。



## 9.4 小结

​	聚集函数⽤来汇总数据。SQL⽀持5个聚集函数，可以⽤多种⽅法使⽤ 它们，返回所需的结果。这些函数很⾼效，它们返回结果⼀般⽐你在 ⾃⼰的客⼾端应⽤程序中计算要快得多。





# 第10章 分组数据

​	介绍如何分组数据，以便汇总内容的子集。设置2个新的SELECT语句子句：GROUP BY AND HAVING。



## 10.1 数据分组

​	如果要返回每个供应商提供的产品数⽬，该怎么办？或者返回只提供 ⼀项产品的供应商的产品，或者返回提供10个以上产品的供应商的产品，怎么办？ 这就是分组⼤显⾝⼿的时候了。使⽤分组可以将数据分为多个逻辑 组，对每个组进⾏聚集计算。



## 10.2 创建分组

​	分组是使用SELECT语句的GROUP BY子句建立的。

- 例：返回每个供应商提供的产品ID和数量

- ```sql
  SELECT vend_id, COUNT(*) AS prod_nums FROM Products GROUP BY vend_id;
  ```

  ```sql
  +---------+-----------+
  | vend_id | prod_nums |
  +---------+-----------+
  | BRS01   |         3 |
  | DLL01   |         4 |
  | FNG01   |         2 |
  +---------+-----------+
  ```




## 10.3 过滤分组

​	GROUP BY除了可以分组数据外，还允许过滤分组，规定包括那些分组，排除那些分组。例如：你可能想要列出至少有2个订单的所有顾客。为此SQL提供了另一个子句HAVING。HAVING与WHERE非常类似，事实上，目前所有提到过的所有类型的WHERE子句都可以用HAVING来替代。唯一的差别是WHERE过滤行，HAVING过滤分组。

- 提示：HAVING支持所有WHERE操作符

- 例：返回订单数大于等于2的数据

  ```sql
  SELECT cust_id, COUNT(*) AS orders FROM Orders GROUP BY cust_id HAVING COUNT(*) >= 2;
  ```

  ```SQL
  +------------+--------+
  | cust_id    | orders |
  +------------+--------+
  | 1000000001 |      2 |
  +------------+--------+
  ```

- 说明：HAVING和WHERE的差别

  - WHERE咋数据分组前进行过滤，HAVING在数据分组后进行过滤。这是一个重要的区别，WHERE派出的行不包括在分组中。这可能会改变计算值，从而影响HAVING子句中基于这些值过滤掉的分组。
  
- 例：列出具有2个以上产品且价格>=4的供应商

- ```SQL
  SELECT vend_id, COUNT(*) AS prod_nums FROM Products WHERE prod_price >=4 GROUP BY vend_id HAVING COUNT(*) >=2;
  ```

  ```SQL
  +---------+-----------+
  | vend_id | prod_nums |
  +---------+-----------+
  | BRS01   |         3 |
  | FNG01   |         2 |
  +---------+-----------+
  ```



## 10.4 分组和排序

​	GROUP BY 和ORDER BY经常完成相同的工作，但他们非常不同，理解这一点很重要。表10-1汇总了他们之间的差别。

<center>表10-1</center>
| ORDER BY                                     | GROUP BY                                                 |
| -------------------------------------------- | -------------------------------------------------------- |
| 对产生的输出排序                             | 对行分组，但输出可能不是分组的顺序                       |
| 任意列都可以使用（甚至非选择的列也可以使用） | 只可能使用选择列或表达式列，而且必须使用每个选择列表达式 |
| 不一定需要                                   | 如果与聚集韩式一起使用列（或表达式），则必须使用         |
|                                              |                                                          |

- 例：检索包含三个或更多物品的订单号和订购物品的数目

- ```sql
  SELECT order_num, COUNT(*) AS items FROM OrderItems GROUP BY order_num HAVING COUNT(*) >=3;
  ```

- ```SQL
  +-----------+-------+
  | order_num | items |
  +-----------+-------+
  |     20006 |     3 |
  |     20007 |     5 |
  |     20008 |     5 |
  |     20009 |     3 |
  +-----------+-------+
  ```

- 例：在以上基础上再根据订购物品的数目排序输出

- ```sql
  SELECT order_num, COUNT(*) AS items FROM OrderItems GROUP BY order_num HAVING COUNT(*) >=3 ORDER BY items, order_num;
  ```

- ```SQL
  +-----------+-------+
  | order_num | items |
  +-----------+-------+
  |     20006 |     3 |
  |     20009 |     3 |
  |     20007 |     5 |
  |     20008 |     5 |
  +-----------+-------+
  ```

- 分析

  - 在这个例子中，使用GROUP BY子句按订单号（order_num列）分组数据一遍COUNT(*)函数能够返回每个订单中的物品数目。HAVING子句过滤数据，使得只返回包含三个或更多物品的订单。最后用ORDER BY 进行排序输出。



## 10.5 SELECT子句顺序

​	回顾一下SELECT语句中子句的顺序。表10-2在SELECT语句中使用必须遵循的次序。

<center>表 10-2 SELECT子句及其顺序</center>
| 子句     | 说明                 | 是否必须使用           |
| -------- | -------------------- | ---------------------- |
| SELECT   | 要返回的列或者表达式 | 是                     |
| FROM     | 从中检索数据的表     | 仅在从表选择数据时使用 |
| WHERE    | 行级过滤             | 否                     |
| GROUP BY | 分组说明             | 仅在按组计算聚集时使用 |
| HAVING   | 组级过滤             | 否                     |
| ORDER BY | 输出排序顺序         | 否                     |



## 10.6 小结

​	上一章学习了如何使用SQL聚集函数对数据进行汇总计算。这一章讲授了如何使用GROUP BY子句对多数据进行汇总计算，返回每个组的结果。我们看到了如何使用HAVING子句过滤特定的组，还知道了ORDER BY 和GROUP BY 之间以及WHERE和HAVING之间的差异。





# 第11章 使用子查询

## 11.1 子查询

​	SELECT语句是SQL的查询。我们迄今为止所看到的所有SELECT语句都是简单查询，即从单个数据库表中检索数据的单条语句。

- 查询（query）
  - 任何SQL语句都是查询。但此术语一般指SELECT语句。

  SQL还允许创建子查询（subquery）,即嵌套在其他查询中的查询。

- 说明：MySQL支持
  
  - 如果使用MySQL，应该知道对子查询的支持是从4.1版本引进的。MySQL的早起版本并不支持子查询。



## 11.2 利用子查询进行过滤

- 例：列出订购物品RGAN01的所有顾客

- ```sql
  # 0.检索包含物品RGAN01的所有订单的编号
  # 1.检索具有前一步骤列出的订单编号的所有顾客ID
  # 2.检索前一步骤返回的所有顾客ID的顾客信息
  SELECT cust_id, cust_name,cust_country, cust_email FROM Customers WHERE cust_id IN (SELECT cust_id FROM OrderItems WHERE order_num IN (SELECT order_num FROM OrderItems WHERE prod_id = "RGAN01"));
  ```

- ```SQL
  +------------+---------------+--------------+-----------------------+
  | cust_id    | cust_name     | cust_country | cust_email            |
  +------------+---------------+--------------+-----------------------+
  | 1000000001 | Village Toys  | USA          | sales@villagetoys.com |
  | 1000000002 | Kids Place    | USA          | NULL                  |
  | 1000000003 | Fun4All       | USA          | jjones@fun4all.com    |
  | 1000000004 | Fun4All       | USA          | dstephens@fun4all.com |
  | 1000000005 | The Toy Store | USA          | NULL                  |
  +------------+---------------+--------------+-----------------------+
  ```

- 分析

  - 为了执行上述语句，DBMS实际上必须执行三条SELECT语句，最里边的子查询返回订单号列表，此列表用户中间子查询的WHERE子句，中间的子查询返回顾客ID列表，此顾客ID列表用于最外面查询的WHERE子句，最外层查询返回所需的数据。



## 11.3 作为计算字段使用子查询

​	使用子查询的另一方法是创建计算字段。假如需要显示Customers表中每个顾客的订单总数。订单与相应的顾客ID存储在Orders表中。执行这个操作需要遵循以下步骤：

- 0.从Customers表中检索出顾客列表

- 1.对于检索出的每个顾客，统计其在Orders表中的订单数目

- ```sql
  SELECT cust_name, cust_state,(SELECT COUNT(*) FROM Orders WHERE Orders.cust_id = Customers.cust_id) AS orders FROM Customers ORDER BY orders;
  ```

- ```sql
  +---------------+------------+--------+
  | cust_name     | cust_state | orders |
  +---------------+------------+--------+
  | Kids Place    | OH         |      0 |
  | Fun4All       | IN         |      1 |
  | Fun4All       | AZ         |      1 |
  | The Toy Store | IL         |      1 |
  | Village Toys  | MI         |      2 |
  +---------------+------------+--------+
  ```

- 分析

  - 这条SELECT语句对Customers表中每个顾客返回三列（cust_name、cust_state、orders）。orders是一个计算字段，由子查询返回。该子查询对检索出的每个顾客执行一次，在此例中，该子查询进行了5次，因为检索出了5个顾客。
    子查询中的WHERE子句与前面使用的WHERE子句稍有不同，因为它使用了完全限定的列名，而不只是列名（cust_id）。他指定表名和列名（Orders.cust_id 和 Customers.cust_id）。下面的WHERE子句告诉SQL，比较Orders表中的cust_id和当前正从Customers表中检索的cust_id。



## 11.4 总结

​	这⼀章学习了什么是⼦查询，如何使⽤它们。⼦查询常⽤于WHERE⼦ 句的IN操作符中，以及⽤来填充计算列。我们举了这两种操作类型的例⼦。

# 第12章 联结表

​	这一章会介绍什么事联结，为什么使用联结，如何编写使用联结的SELECT语句。

## 12.1 联结

​	SQL最强大的功能之一就是能在数据查询的执行中联结（join）表。联结是利用SQL的SELECT能执行的最重要的操作，很好地理解联结是学习SQL极为重要的部分。在能够有效的使用联结钱，必须了解关系表以及关系数据库设计的一些基础知识。下面的介绍并不能涵盖这一主题的所有内容，但作为入门已经够了



### 12.1.1 关系表

​	理解关系表，最好是来看个例子。

有一个包含产品目录的数据库表，其中每类物品占一行。对于每一种物品，要存储的信息包括产品描述、价格，以及生产该产品的供应商。

现有同一供应商生产的多种物品，那么在何处存储供应商名称、地址、联系方式等信息呢？将这些数据与产品信息分开存储的理由是：

- 同一供应商生产的每个产品，其供应商信息都是相同的，对每个产品重复此信息既浪费时间又浪费存储空间
- 如果供应商信息发生变化，例如供应商地址或者电话号码变更，只需修改一次即可
- 如果有重复数据（即每种产品都存储供应商信息），则很难保证每次输入该数据的方式都相同，不一致的数据在报表中很难利用

​    关键是，相同的数据出现多次绝不是一件好事，这是关系数据库设计的基础。关系表的设计就是要把信息分解成多个表，一类数据一个表，各表通过某些共同值互相关联（所以才叫做关系型数据库）。

​	在这个例子中可建立两个表：一个存储供应商信息，另一个存储产品信息。Venders表包含所有供应商信息，每个供应商占一行，具有唯一标识。此标识称为主键（primary key），可以是供应商ID或任何其他唯一值。

​	Products表只存储产品信息，除了存储供应商ID（Venders表的主键）以外，他不存储其他有关供应商的信息。Venders表的主键将与Products表关联，利用供应商ID能从Venders表中找出相应供应商的详细信息。

​	这样做的好处是：

- 供应商信息不重复存储，不会浪费时间和空间
- 如果供应商信息变动，可以只更新Venders表中的单个记录，相关表中的数据不用改动
- 由于数据补充书，数据显然是一致的，使得处理数据和生成报表更简单

​    总之，关系数据可以有效地存储，方便地处理。因此，关系型数据库的可伸缩性远比非关系型数据库好。

- 可伸缩（scale）
  - 能够适应不断增加的工作量而不是白。设计良好的数据库或应用程序称为可伸缩性好（scale well）。



### 12.1.2 为什么使用联结

​		将数据分解为多个表能更有效地存储，更方便地处理，并且可伸缩性更好。但这些好处是有代价的。

如果数据存储在多个表中，怎样使用一条SELECT语句就检索出数据呢？答案是使用联结。简单说联结是一种机制，用来在一条SELECT语句中关联表，因此称为联结。使用特殊的语法，可以联结多个表返回一组输出，联结在运行时关联表正确的行。



## 12.2 创建联结

​	创建联结非常简单，指定要联结的所有表以及关联他们的方式即可。请看以下例子：

```sql
SELECT vend_name, prod_name, prod_price FROM Vendors, Products WHERE Vendors.vend_id = Products.vend_id;
```

```sql
+-----------------+---------------------+------------+
| vend_name       | prod_name           | prod_price |
+-----------------+---------------------+------------+
| Bears R Us      | 8 inch teddy bear   | 5.99       |
| Bears R Us      | 12 inch teddy bear  | 8.99       |
| Bears R Us      | 18 inch teddy bear  | 11.99      |
| Doll House Inc. | Fish bean bag toy   | 3.49       |
| Doll House Inc. | Bird bean bag toy   | 3.49       |
| Doll House Inc. | Rabbit bean bag toy | 3.49       |
| Doll House Inc. | Raggedy Ann         | 4.99       |
| Fun and Games   | King doll           | 9.49       |
| Fun and Games   | Queen doll          | 9.49       |
+-----------------+---------------------+------------+
```

- 警告：完全限定列名
  - 就像在前一章提到的，在引用的列可能出现歧义时，必须使用完全限定列名（用一个点分隔表名和列名）。如果引用一个没有用表名限制具有歧义的列名，大多数DBMS会返回错误。



### 12.2.1 WHERE子句的重要性

- 笛卡尔积（cartesian product）
  - 由没有联结条件的表关系返回的结果为笛卡尔积。检索出的行的数目将是第一个表中的行数乘以第二个表中的行数。

理解这一点请看下面的SELECT语句及其输出：

```sql
SELECT vend_name, prod_name, prod_price From Vendors, Products;
```

```sql
+-----------------+---------------------+------------+
| vend_name       | prod_name           | prod_price |
+-----------------+---------------------+------------+
| Bear Emporium   | Fish bean bag toy   | 3.49       |
| Bears R Us      | Fish bean bag toy   | 3.49       |
| Doll House Inc. | Fish bean bag toy   | 3.49       |
| Fun and Games   | Fish bean bag toy   | 3.49       |
| Furball Inc.    | Fish bean bag toy   | 3.49       |
| Jouets et ours  | Fish bean bag toy   | 3.49       |
| Bear Emporium   | Bird bean bag toy   | 3.49       |
| Bears R Us      | Bird bean bag toy   | 3.49       |
| Doll House Inc. | Bird bean bag toy   | 3.49       |
| Fun and Games   | Bird bean bag toy   | 3.49       |
| Furball Inc.    | Bird bean bag toy   | 3.49       |
| Jouets et ours  | Bird bean bag toy   | 3.49       |
| Bear Emporium   | Rabbit bean bag toy | 3.49       |
| Bears R Us      | Rabbit bean bag toy | 3.49       |
| Doll House Inc. | Rabbit bean bag toy | 3.49       |
| Fun and Games   | Rabbit bean bag toy | 3.49       |
| Furball Inc.    | Rabbit bean bag toy | 3.49       |
| Jouets et ours  | Rabbit bean bag toy | 3.49       |
| Bear Emporium   | 8 inch teddy bear   | 5.99       |
| Bears R Us      | 8 inch teddy bear   | 5.99       |
| Doll House Inc. | 8 inch teddy bear   | 5.99       |
| Fun and Games   | 8 inch teddy bear   | 5.99       |
| Furball Inc.    | 8 inch teddy bear   | 5.99       |
| Jouets et ours  | 8 inch teddy bear   | 5.99       |
| Bear Emporium   | 12 inch teddy bear  | 8.99       |
| Bears R Us      | 12 inch teddy bear  | 8.99       |
| Doll House Inc. | 12 inch teddy bear  | 8.99       |
| Fun and Games   | 12 inch teddy bear  | 8.99       |
| Furball Inc.    | 12 inch teddy bear  | 8.99       |
| Jouets et ours  | 12 inch teddy bear  | 8.99       |
| Bear Emporium   | 18 inch teddy bear  | 11.99      |
| Bears R Us      | 18 inch teddy bear  | 11.99      |
| Doll House Inc. | 18 inch teddy bear  | 11.99      |
| Fun and Games   | 18 inch teddy bear  | 11.99      |
| Furball Inc.    | 18 inch teddy bear  | 11.99      |
| Jouets et ours  | 18 inch teddy bear  | 11.99      |
| Bear Emporium   | Raggedy Ann         | 4.99       |
| Bears R Us      | Raggedy Ann         | 4.99       |
| Doll House Inc. | Raggedy Ann         | 4.99       |
| Fun and Games   | Raggedy Ann         | 4.99       |
| Furball Inc.    | Raggedy Ann         | 4.99       |
| Jouets et ours  | Raggedy Ann         | 4.99       |
| Bear Emporium   | King doll           | 9.49       |
| Bears R Us      | King doll           | 9.49       |
| Doll House Inc. | King doll           | 9.49       |
| Fun and Games   | King doll           | 9.49       |
| Furball Inc.    | King doll           | 9.49       |
| Jouets et ours  | King doll           | 9.49       |
| Bear Emporium   | Queen doll          | 9.49       |
| Bears R Us      | Queen doll          | 9.49       |
| Doll House Inc. | Queen doll          | 9.49       |
| Fun and Games   | Queen doll          | 9.49       |
| Furball Inc.    | Queen doll          | 9.49       |
| Jouets et ours  | Queen doll          | 9.49       |
+-----------------+---------------------+------------+
```

- 分析
  - 从上面的输出可以看到，相应的笛卡尔积不是我们想要的。这里返回的数据用每个供应商匹配了每个产品，包括供应商不正确的产品（即使供应商根本就没有产品）。
- 警告：不要忘了WHERE子句
  - 要保证所有联结都有WHERE子句，否则DBMS将返回比想要的数据多的多的数据。同理，要保证WHERE子句的正确性。不正确的过滤条件会导致DBMS返回不正确的数据
- 提示：叉联结
  - 有时，返回笛卡尔积的联结，也称为叉联结（cross join）。



### 12.2.2 内联结

​	目前为止使用的联结称为等值联结（equijoin），它基于两个表之间的相等测试。这种联结也称为内联结（inner join）。其实，可以对这种联结使用稍微不同的语法，明确指定联结的类型。下面的SELECT语句返回与前面例子完全相同的数据：

```sql
SELECT vend_name, prod_name, prod_price FROM Vendors INNER JOIN Products ON Vendors.vend_id = Products.vend_id;
```

```sql
+-----------------+---------------------+------------+
| vend_name       | prod_name           | prod_price |
+-----------------+---------------------+------------+
| Doll House Inc. | Fish bean bag toy   | 3.49       |
| Doll House Inc. | Bird bean bag toy   | 3.49       |
| Doll House Inc. | Rabbit bean bag toy | 3.49       |
| Bears R Us      | 8 inch teddy bear   | 5.99       |
| Bears R Us      | 12 inch teddy bear  | 8.99       |
| Bears R Us      | 18 inch teddy bear  | 11.99      |
| Doll House Inc. | Raggedy Ann         | 4.99       |
| Fun and Games   | King doll           | 9.49       |
| Fun and Games   | Queen doll          | 9.49       |
+-----------------+---------------------+------------+
```

- 分析

  - 此语句中的SELECT与前面的SELECT语句相同，但FROM子句不同。这里，两个表之间的关系是以INNER JOIN指定的部分FROM子句。在使用这种语法时，联结条件用特定的ON子句而不是WHERE子句给出。传递给ON的实际条件与传递给WHERE的相同。

  

### 12.2.3 联结多个表

​	SQL不限制一条SELECT语句中可以联结表的数目。创建联结的基本规则也相同。首先列出所有表，然后定义表之间的关系。例如：

```sql
SELECT prod_name, vend_name, prod_price, quantity FROM OrderItems, Products, Vendors WHERE Products.vend_id = Vendors.vend_id AND OrderItems.prod_id = Products.prod_id AND order_num = 20007;
```

```sql
+---------------------+-----------------+------------+----------+
| prod_name           | vend_name       | prod_price | quantity |
+---------------------+-----------------+------------+----------+
| 18 inch teddy bear  | Bears R Us      | 11.99      |       50 |
| Fish bean bag toy   | Doll House Inc. | 3.49       |      100 |
| Bird bean bag toy   | Doll House Inc. | 3.49       |      100 |
| Rabbit bean bag toy | Doll House Inc. | 3.49       |      100 |
| Raggedy Ann         | Doll House Inc. | 4.99       |       50 |
+---------------------+-----------------+------------+----------+
```

- 分析
  - 这个例子显示订单20007中的物品。订单物品存储在OrderItems表中。每个产品按其产品ID存储，它引进Products表中的产品。这些产品通过供应商ID联结到Vendors表中相应的供应商，供应商ID存储在每个产品的记录中。这里的FROM子句列出三个表，WHERE子句定义这两个联结条件，而第三个联结条件用来过滤出订单20007中的物品。
- 警告：性能考虑
  - DBMS在运行时关联指定的每个表，以处理联结。这种处理可能非常耗费资源，因此应该注意，不要联结不必要的表。联结的表越多，性能下降的越厉害。
- 警告：联结中表的最大数目
  - 虽然SQL本身不限制每个联结约束表中的数目，但实际上许多DBMS都有限制

现在回顾一下11章的例子，以下SELECT返回订购产品RGAN01的顾客的订单：

```sql
# 0.检索包含物品RGAN01的所有订单的编号
# 1.检索具有前一步骤列出的订单编号的所有顾客ID
# 2.检索前一步骤返回的所有顾客ID的顾客信息
-- 原方法
SELECT cust_id, cust_name,cust_country, cust_email FROM Customers WHERE cust_id IN (SELECT cust_id FROM OrderItems WHERE order_num IN (SELECT order_num FROM OrderItems WHERE prod_id = "RGAN01"));

-- 使用联结
SELECT cust_name,cust_country, cust_email FROM Customers, Orders, OrderItems WHERE Customers.cust_id = Orders.cust_id AND OrderItems.order_num = Orders.order_num AND prod_id = "RGAN01";

```

- 分析
  - 原方法查询需要使用3个表。但是新方法我们没有在嵌套子查询中使用他们，而是使用了两个联结来连接表。这里有三个WHERE子句条件。前两个关联联结中的表，后一个过滤产品RGAN01的数据。
- 提示：多做实验
  - 可以看到，执行任一给定的SQL操作一般不止一种方法。很少有绝对正确或者绝对错误的方法。性能可能会受操作类型、所使用的DBMS、表中的数据量】是否存在索引或键等条件的影响。因此，有必要试验不同的选择机制，找出最适合具体情况的方法。

## 12.3 小结

​	联结是SQL中一个最重要、最强大的特性，有效地使用联结需要对关系型数据库设计有基本的了解。这一章在介绍联结时，讲述了一些关系型数据库设计的基本知识，包括等值联结（也称为内联结）这种最常用的联结。下一章介绍如何创建其他类型的联结。



# 第13章 创建高级联结

​	这一章讲解另外一些联结（包括他们的含义和使用方法），介绍如何使用表别名，如何对被联结的表使用聚集函数。

## 13.1 使用表别名

​	SQL除了可以对列名和计算字段使用别名，还允许给表名起别名。这样做有两个主要理由：

- 缩短SQL语句。
- 允许在一条SELECT语句中多次使用相同的表

以下SELECT语句，与前面一章所用的语句基本相同，但是改成了使用别名：

```sql
# 第四版例子原SQL
SELECT cust_name, cust_contact FROM Customers AS c, Orders AS o, OrderItems AS oi WHERE c.cust_id = o.cust_id AND oi.order_num = o.order_num AND prod_id = "RGAN01";
# 修改了一下 主要原因有以下2点
-- 0.MySQL也允许直接使用别名 去掉了AS
-- 1.最后一个条件pord_id前面没有指定表名，在这里我指定了具体的表名(个人理解1是方便理解，无需看表结构，2是对于SELECT查询的性能可能会有一丢丢的提升，毕竟指定了具体的表名)
SELECT cust_name, cust_contact FROM Customers c, Orders o, OrderItems oi WHERE c.cust_id = o.cust_id AND oi.order_num = o.order_num AND oi.prod_id = "RGAN01";
```

```sql
+---------------+--------------------+
| cust_name     | cust_contact       |
+---------------+--------------------+
| Fun4All       | Denise L. Stephens |
| The Toy Store | Kim Howard         |
+---------------+--------------------+
```

需要注意，表别名只有在查询执行中使用。与列别名不一样，表别名不会返回到客户端。

## 13.2 使用不同类型的联结

​	迄今为止，我们使用的只是内联结或者等值联结的简单联结。现在来看看三种其他联结：

- 自联结（self-join）
- 自然联结（natural join）
- 外联结（outer join）

### 13.2.1 自联结

如前所述，使用表别名的一个主要原因是能在一条SELECT语句中不止一次引用相同的表。举例说明：

- 例：假如要给与Jim Jones同一公司的所有顾客发送一封信件。这个查询要求首先找Jim Jones工作的公司，然后找出在该公司的顾客。下面是解决此问题的一种方法：

- ```sql
  SELECT cust_id, cust_name, cust_contact FROM Customers WHERE cust_name = (SELECT cust_name FROM Customers WHERE cust_contact = 'Jim Jones');
  ```

- ```sql
  +------------+-----------+--------------------+
  | cust_id    | cust_name | cust_contact       |
  +------------+-----------+--------------------+
  | 1000000003 | Fun4All   | Jim Jones          |
  | 1000000004 | Fun4All   | Denise L. Stephens |
  +------------+-----------+--------------------+
  ```

- 分析

  - 这是第一种解决方案，使用子查询。内部的SELECT语句做了一个简单检索，返回Jim Jones工作公司的cust_name。该名字用语外部查询的WHERE子句中，以检索出为该公司工作的所有雇员。

- ```sql
  -- 使用联结的相同查询
  SELECT c1.cust_id, c1.cust_name, c1.cust_contact FROM Customers c1, Customers c2 WHERE c1.cust_name = c2.cust_name AND c2.cust_contact = 'Jim Jones';
  ```

- ```sql
  +------------+-----------+--------------------+
  | cust_id    | cust_name | cust_contact       |
  +------------+-----------+--------------------+
  | 1000000003 | Fun4All   | Jim Jones          |
  | 1000000004 | Fun4All   | Denise L. Stephens |
  +------------+-----------+--------------------+
  ```

- 分析
  
  - 此查询需要的两个表实际上市相同的表，因此Customers表在FROM子句中出现了2次，虽然这是合法的，但对Customers的引用具有歧义性，因为DBMS不知道你引用的是哪个Customers表。为了解决这个问题，需要用到表别名（C1、C2）。
  
- 提示：用自联结而不用子查询

  - 自联结通常作为外部语句，用来替代从相同表中检索数据的使用子查询语句。虽然结果是相通的，但是许多DBMS处理联结表远比处理子查询快得多。



### 13.2.2 自然联结

​	无论何时对标进行联结，应该至少有一列不止出现在一个表中（被联结的列）。标准的联结返回所有数据，相同的列甚至出现多次。自然联结排除多次出现，使每一列只返回一次。

- 例

  - ```sql
    SELECT C.*, O.order_num, O.order_date, OI.prod_id, OI.quantity, OI.item_price FROM Customers AS C, Orders AS O, OrderItems AS OI WHERE C.cust_id = O.cust_id AND OI.order_num = O.order_num AND prod_ID= 'RGAN01';
    ```

    ```SQL
    +------------+---------------+---------------------+-----------+------------
    | cust_id    | cust_name     | cust_address        | cust_city | cust_state | cust_zip | cust_country | cust_contact       | cust_email            | order_num | order_date          | prod_id |
    +------------+---------------+---------------------+-----------+------------
    | 1000000004 | Fun4All       | 829 Riverside Drive | Phoenix   | AZ         | 88888    | USA          | Denise L. Stephens | dstephens@fun4all.com |     20007 | 2020-01-30 00:00:00 | RGAN01  |
    | 1000000005 | The Toy Store | 4545 53rd Street    | Chicago   | IL         | 54545    | USA          | Kim Howard         | NULL                  |     20008 | 2020-02-03 00:00:00 | RGAN01  |
    +------------+---------------+---------------------+-----------+------------
    ```

- 分析

  - 在这个例子中，通配符只对第一个表使用。所有其他列明确指出，所有没有重复的列被检索出来。



### 13.2.3 外联结

​	许多联结将一个表中的行与另一个表中的行相关联，但有时候需要包含没有关联行的那些行。

- 对每个顾客下的订单进行计数，包含哪些至今尚未下订单的顾客
- 列出所有产品以及订购数量，包括没有人订购的产品
- 计算平均销售规模，包括那些至今尚未下订单的顾客

```sql
# 内联结，检索出所有顾客及其订单
mysql> SELECT Customers.cust_id, Orders.order_num FROM Customers INNER JOIN Orders ON Customers.cust_id = Orders.cust_id;

```

```sql
+------------+-----------+
| cust_id    | order_num |
+------------+-----------+
| 1000000001 |     20005 |
| 1000000001 |     20009 |
| 1000000003 |     20006 |
| 1000000004 |     20007 |
| 1000000005 |     20008 |
+------------+-----------+
```

外联结预发类似，要检查包括没有订单顾客在内的所有顾客

```sql
# 左外联结
# LEFT JOIN 为 LEFT OUTER JOIN简写,查询出Customers的数据
mysql> SELECT Customers.cust_id, Orders.order_num FROM Customers LEFT JOIN Orders ON Customers.cust_id = Orders.cust_id;

```

```sql
+------------+-----------+
| cust_id    | order_num |
+------------+-----------+
| 1000000001 |     20005 |
| 1000000001 |     20009 |
| 1000000002 | NULL      |
| 1000000003 |     20006 |
| 1000000004 |     20007 |
| 1000000005 |     20008 |
+------------+-----------+
```

- 分析
  - 类似上一章中的内联结，这条SELECT语句使用了关键字OUTER JOIN来制定联结类型（而不是在WHERE子句中指定）。但是，与内联结关联两个表不同的是，外联结还包括没有关联行的行。在使用OUTER JOIN语法是，必须使用RIGHT 或LEFT关键字指定包括其所有行的表（LEFT指出的是OUTER JOIN左边的表，而RIGHT指出的是OUTER JOIN右边的表）。上述例子使用LEFT JOIN从FROM子句左边的表（Customers）中选择所有行。为了从右边的表中选择所有行需要使用RIGHT OUTER JOIN

```sql
# 右外联结
# 查询出Orders表中的数据
mysql> SELECT Customers.cust_id, Orders.order_num FROM Customers RIGHT JOIN Orders ON Customers.cust_id = Orders.cust_id;
```

```SQL
+------------+-----------+
| cust_id    | order_num |
+------------+-----------+
| 1000000001 |     20005 |
| 1000000001 |     20009 |
| 1000000003 |     20006 |
| 1000000004 |     20007 |
| 1000000005 |     20008 |
+------------+-----------+
```

- 全外联结（full outer join）