# opencv2

どんな処理を実装したのかという簡単な説明
・ガンマ補正(gamma correction
・ガウシアンブラー(gaussian blur
・RGB空間でR,G,Bのパラメータをそれぞれ個別に変更

使い方，実行の仕方，依存ライブラリとバージョン
・pythonのファイルをそのまま実行
・各処理のウインドウが3つでる
・それぞれのtrack barを操作して実行
・opencv(cv2) version:'3.4.1'

参考にしたサイトなどへのリンク
https://qiita.com/Kazuhito/items/c43e96ab16f400a35721
track bar の実装、ルックアップテーブルによるガンマ補正の実装方法
ページ中の以下のプログラムを利用
  # ガンマ値取得（0は強制的に0.1相当に引き戻し）
  gamma = cv2.getTrackbarPos("gamma(0.1)", "gammma correction") * 0.1
  if gamma == 0:
      gamma = 0.1
      cv2.setTrackbarPos("gamma(0.1)", "gammma correction", 1)

  # ガンマ補正用ルックアップテーブル
  look_up_table = np.zeros((256, 1), dtype = 'uint8')
  for i in range(len(look_up_table)):
      look_up_table[i][0] = (len(look_up_table)-1) * pow(float(i) / (len(look_up_table)-1), 1.0 / gamma)

  # ルックアップテーブルによるガンマ補正
  gamma_correction_image = cv2.LUT(frame, look_up_table)

http://rasp.hateblo.jp/entry/2016/01/24/214027
複数のトラックバーの設定

http://optie.hatenablog.com/entry/2018/03/03/141427
トーンカーブとプログラムについて

https://www.blog.umentu.work/python-opencv3%E3%81%A7%E7%94%BB%E7%B4%A0%E3%81%AErgb%E5%80%A4%E3%82%92%E5%85%A5%E3%82%8C%E6%9B%BF%E3%81%88%E3%82%8B/
RGBチャンネルへのアクセス
ページ内プログラムの以下の部分を参考
  # img_bgr[0] に青, img_bgr[1]に緑,img_bgr[2]に赤が入る。
  img_bgr = cv2.split(img_src)

  # 青->赤, 緑->青, 青->緑
  img_cng = cv2.merge((img_bgr[1],img_bgr[2],img_bgr[0]))

どの部分を参考，コピー，引用したのかを明確に書く


実行の様子のスクリーンショット動画サムネイルを埋め込む
Youtubeに動画をアップロードしてリンクを貼る
YouTube Link↓
https://www.youtube.com/watch?v=92cAU0OBDJ0&feature=youtu.be
