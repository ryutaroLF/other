# dataframeへの代入について

代入ができないときは、スライスが影響しているのかも。
引用:
```
test[1][1]=1 ではスライスが繰り返されるため、環境によってはコピーが行われることがあります。その場合、コピーに対して代入をすることになるため、元のデータには反映されません。

test.loc[1, 1]=1 と1回の操作とすれば期待どおりに動くと思います。
```

例えば、
```python
df.loc[index]["ComeTime"] = datetime.datetime.now()
```
だとエラーが出て、置き換えができなかったが、
```python
df.loc[index,"ComeTime"] = datetime.datetime.now()
```
としたらうまくいった。