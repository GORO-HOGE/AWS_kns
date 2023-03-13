### 第6回課題

- あなたが最後に AWS を利用した日の記録を、どれでもよいので CloudTrail のイベントから探し出してください。

ec2 作成

![6_0001](https://user-images.githubusercontent.com/126846580/224608077-ced0ef04-8534-4212-bd3c-5e674d765156.png)

ec2 停止

![6_0002](https://user-images.githubusercontent.com/126846580/224608085-870038a5-d357-4459-b0c1-69ad91f610bd.png)

s3 作成

![6_0003](https://user-images.githubusercontent.com/126846580/224608092-dfd569f3-e247-4f21-8598-6a8017828400.png)

- 今日学んだ CloudWatch アラームを使って、ALB のアラームを設定して、メール通知してみてください。

ヘルスチェックOKアラート設定
![6_0004](https://user-images.githubusercontent.com/126846580/224632171-52679b94-e0d5-4386-bbef-63581e9e3184.png)

ヘルスチェックNGアラート設定
![6_0005](https://user-images.githubusercontent.com/126846580/224632226-6cdfc06c-f3c9-415f-965e-819ae08f1954.png)

動作テスト(Webアプリケーション停止)
![6_0006](https://user-images.githubusercontent.com/126846580/224632345-ef9bfbfa-5642-455e-9274-a73136947b66.png)

ALB上で異常を確認
![6_0007](https://user-images.githubusercontent.com/126846580/224632578-101ad398-a972-4b40-9286-a55225a606c0.png)

アラートメール受信
![6_0008](https://user-images.githubusercontent.com/126846580/224632608-410f2fd1-ce5b-4fab-a885-a77ba56383f9.png)

アラートページにてアラート状態であることを確認

![6_0009](https://user-images.githubusercontent.com/126846580/224632640-fb6b1177-4783-4c25-ad4d-e117eb91e44a.png)

動作テスト(Webアプリケーション復旧)
![6_0010](https://user-images.githubusercontent.com/126846580/224632719-6ed59550-6b0f-44ad-b9b1-f54bd546bbae.png)

アラートページにてOK状態であることを確認
![6_0011](https://user-images.githubusercontent.com/126846580/224632783-52443fb9-d6b3-480b-a70b-719d600a13b2.png)

復旧メール受信
![6_0012](https://user-images.githubusercontent.com/126846580/224632891-d30750b1-20cb-4615-a19a-5bd46a0a9e3e.png)


- AWS 利用料の見積を作成してください。

https://calculator.aws/#/estimate?id=73f3bf2ff274d9dd996bc4f1085bacca2b2ee4f1


- マネジメントコンソールから、現在の利用料を確認して教えてください。

![6_0013](https://user-images.githubusercontent.com/126846580/224633043-28ccb873-9020-4751-b711-cc5d54939ff7.png)

![6_0014](https://user-images.githubusercontent.com/126846580/224633051-442554c9-785d-4318-9119-e870cfbb0504.png)

