### 第7回課題

- 今回の課題の感想や疑問を課題とし報告してください。

[JVN](https://jvn.jp/) や CVSS は運用監視の業務をしていた時に利用していた為、話の内容は大まかには理解できたが、<br>
まだ、WAF など AWS サービスの理解や一般IT知識が不足していると感じた。<br>
また、検証環境でしか構築した経験しかなく、構築時に脆弱性に気を付けて構築した経験が少ないため、今後気を付けて構築していきたいと思った。


- 今皆さんが作っている環境は、どんな攻撃にたいして「脆弱」ですか？どのような対策が取れそうですか？ぜひ考えてみてください。

  ・HTTPS 化をしていないため、通信データを見られてしまう(自分の場合は従業員データを見られてしまう可能性がある)<br>
    →cloudfrontを設置してサイトをHTTPS化する [参考サイト(AWSでWebサイトをHTTPS化 )](https://recipe.kc-cloud.jp/archives/11408/)<br>
    
  ・WebサーバのパブリックIPを拒否していないため、不正アクセスされる可能性がある<br>
    →nginx の設定を変更(IP直指定のアクセスを拒否する)[参考サイト(nginxでIP直指定のアクセスを禁止)](https://hit.hateblo.jp/entry/elb/direct-ip/deny)<br>
    →EC2をプライベート環境に移動する。その後ELB経由でアクセスできるように設定する<br>
    [参考サイト(インスタンスを移動)](https://aws.amazon.com/jp/premiumsupport/knowledge-center/move-ec2-instance/)<br>
    [参考サイト(プライベートなEC2に一時的にSSHする3つの方法)](https://dev.classmethod.jp/articles/bastion-3way-rk/)<br>
    [参考サイト(パブリックなALBからプライベートなEC2にアクセスしてみた)](https://zenn.dev/mn87/articles/b6a5e0e5b5ee4c)
    
  ・ログインユーザが初期ユーザのままになっている。<br>
    →初期ユーザの使用を禁止し、他の任意のユーザーで運用する [参考サイト(EC2のデフォルトユーザーを禁止)](https://www.linuxmaster.jp/linux_skill/2021/04/amazon-linux2ec2ec2-user.html)
