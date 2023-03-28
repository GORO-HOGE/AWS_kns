### 第10回課題


CloudFormation を利用して、現在までに作った環境をコード化しましょう。
コード化ができたら実行してみて、環境が自動で作られることを確認してください。

作成したコード<br>
[01_knsVPC.yml](./10_cloudformation/01_knsVPC.yml)

実行結果
![10_001](./%E7%A0%94%E4%BF%AE/10/10_001.png)

VPC
![10_002](./%E7%A0%94%E4%BF%AE/10/10_002.png)

作成したコード<br>
[02_knsSG.yml](./10_cloudformation/02_knsSG.yml)

実行結果
![10_003](./%E7%A0%94%E4%BF%AE/10/10_003.png)

SG
![10_004](./%E7%A0%94%E4%BF%AE/10/10_004.png)

作成したコード<br>
[03_knsEC2.yml](./10_cloudformation/03_knsEC2.yml)

実行結果
![10_005](./%E7%A0%94%E4%BF%AE/10/10_005.png)
![10_006](./%E7%A0%94%E4%BF%AE/10/10_006.png)

EC2
![10_007](./%E7%A0%94%E4%BF%AE/10/10_007.png)

作成したコード<br>
[04_knsRDS.yml](./10_cloudformation/04_knsRDS.yml)

実行結果
![10_008](./%E7%A0%94%E4%BF%AE/10/10_008.png)
![10_009](./%E7%A0%94%E4%BF%AE/10/10_009.png)

RDS
![10_010](./%E7%A0%94%E4%BF%AE/10/10_010.png)

作成したコード<br>
[05_knsS3.yml](./10_cloudformation/05_knsS3.yml)

実行結果
![10_011](./%E7%A0%94%E4%BF%AE/10/10_011.png)
![10_012](./%E7%A0%94%E4%BF%AE/10/10_012.png)

作成したコード<br>
[06_knsELB.yml](./10_cloudformation/06_knsELB.yml)

実行結果
![10_013](./%E7%A0%94%E4%BF%AE/10/10_013.png)
![10_014](./%E7%A0%94%E4%BF%AE/10/10_014.png)

ELB
![10_015](./%E7%A0%94%E4%BF%AE/10/10_015.png)

リスナー
![10_016](./%E7%A0%94%E4%BF%AE/10/10_016.png)

ターゲットグループ
![10_017](./%E7%A0%94%E4%BF%AE/10/10_017.png)

