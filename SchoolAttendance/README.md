# congig.ini
ここには、slackのwebhookのURLを記載

# IpList.csv
```
ip,name,IsInRoomFlag,ComeTime,LeaveTime
```

このcsvファイルは、型なので、メンバー変更などの時にのみ付け足すこと。

ip:割り当てた固有のIPアドレス  
name:名前  
ISInRoomFlag:Trueなら今部屋にいる。(Lan内にスマホがある)  
ComeTime:最初はFalse.その日最初にLan内に入ったときに時刻が一度だけ書かれる  
LeaveTime:最初はFalse.Lan内から出るたびに上書きされる。

# date.txt
日付の更新を判別するためのもの。  
内部変数だと、プログラムが止まった時に参照不能なので出力。  
このファイルは削除しないこと。  