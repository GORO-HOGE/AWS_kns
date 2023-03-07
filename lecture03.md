### 次回までの課題

#### サーバーについて調べてみましょう。
- AP サーバーの名前とバージョンを確認してみましょう。
```
user:~/environment/raisetech-live8-sample-app (main) $ puma --version
puma version 5.6.5
user:~/environment/raisetech-live8-sample-app (main) $ 
```
- AP サーバーを終了させた場合、引き続きアクセスできますか？結果を確認して、また AP サー
バーを起動してください。

起動時
![3_001](https://user-images.githubusercontent.com/126846580/223045378-91d43ea5-21d8-4288-98dd-354d2303498d.png)

終了時
![3_002](https://user-images.githubusercontent.com/126846580/223045363-e6b09892-edea-4aaf-a741-0a6dedc9cbea.png)

#### DB サーバーについて調べてみましょう。
- サンプルアプリケーションで使った DB サーバー（DB エンジン）の名前と、今 Cloud9 で動作しているバージョンはいくつか確認してみましょう。

 DB サーバー（DB エンジン）の名前:MySQL<br>
 バージョン: 8.0.32
```
Your MySQL connection id is 35
Server version: 8.0.32 MySQL Community Server - GPL
```

- DB サーバーを終了させた場合、引き続きアクセスできますか？
エラーが出る再度作成すると正常に動作する
![3_003](https://user-images.githubusercontent.com/126846580/223046156-552d1561-7330-47db-a21f-e3c4ded46b4e.png)

- Rails の構成管理ツールの名前は何でしたか？確認してみてください。
Bundler

- 今回の課題から学んだことを報告してください。
今回コピー元のアプリケーションがあえてエラーが出るようになっており、そのエラーを調べて修正していく課題でした。
Ruby の経験がなく、エラーが出るたびつらかったが、ひとまず正常に動作してほっとした。
0 からWebアプリケーションを作成する際は、このようなエラー修正能力がもっと必要でまだ自分の実力不足をかんじた。
