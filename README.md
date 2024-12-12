# py3mysql
Python3 连接Mysql简单的增删改查封装

## 使用方法
安装扩张
```
pip install pymysql
```
导入包
```python
from  MysqlDB import MysqlDB
```

```sql
-- 生成实例
 db = MysqlDB()

-- 插入
cs = db.insert(table="asin", asin=asin, title="标题"+str(random.randint(100,999)), stars=4.3)
print(cs)

-- 删除
cs = db.delete(table="T1", where="Id = 2")
print(cs)

-- 更新
cs = db.update(table="T1", Name="Python测试3", Sex="man", where="Id in(1,2)")
print(cs)

-- 查询
cs = db.getAll(table="asin", where="1")
print(cs)

```
