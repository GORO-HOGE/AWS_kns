### 第5回課題

- EC2 上にサンプルアプリケーションをデプロイして、動作させてください。

nginx は動作して MyQSL サーバはインストールしていない状態

![5_002](https://user-images.githubusercontent.com/126846580/224253929-10ca47ef-34c4-47c8-81ee-dd310760a1a0.png)

Webアプリケーションが動作することを確認(ALB経由)

![5_003](https://user-images.githubusercontent.com/126846580/224253941-a2cbbd67-168e-453f-8387-711698df0694.png)

上記従業員データがDBのものと一致していることを確認

![5_004](https://user-images.githubusercontent.com/126846580/224253949-8f1f4329-d4d2-4945-bf51-447bbcc92559.png)


- 動作したら、ELB(ALB)を追加してみましょう。

![5_005](https://user-images.githubusercontent.com/126846580/224254426-8927d727-512d-4d73-b7a4-ef8cdaceac7f.png)

![5_006](https://user-images.githubusercontent.com/126846580/224254432-963eb7e9-a08d-4a17-9192-ccc8ba071860.png)


- ELB を加えて動作が確認できたら、さらに S3 を追加してみましょう。S3 をどのように使うかはお任せします。

今回はELBのアクセスログをS3に格納する
ELBのアクセスログ設定

![5_008](https://user-images.githubusercontent.com/126846580/224255279-578e9124-e4af-4bdf-9ebc-f9678dec07d2.png)

S3の中にアクセスログが格納されていることを確認

![5_007](https://user-images.githubusercontent.com/126846580/224254464-a84f6f21-9b1c-4548-b710-afcf92a4f877.png)

- ここまでが問題無く動作したら、その環境を構成図に書き起こしてください。

![構成図2 drawio](https://user-images.githubusercontent.com/126846580/224588637-14430bdd-e1e1-42e1-a3b3-d200a7a12d06.png)
